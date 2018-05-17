import boto3
import os

from flask import Flask
from flask import render_template
from media.nameing import generate_name
from media.s3_storage import S3MediaStorage

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('upload_files.html')

@app.route("/make-animation")
def make_animation():
  return render_template("make_animation.html", invitaion="only limit is yourself")

@app.route("/upload", methods=['POST'])
def handle_upload():
  if 'uploaded_file' not in request.files:
    flash('No files')
    return redirect(request.url)
  uploaded_file = request.files['uploaded_file']
  ref_file = generate_name(uploaded_file.filename)
  media_storage.store(
    dest=ref_file
    source=uploaded_file
  )
  return "OK"

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)

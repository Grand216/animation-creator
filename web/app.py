
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('upload_files.html')

@app.route("/make-animation")
def make_animation():
  return render_template("make_animation.html", invitaion="only limit is yourself")

@app.route("/upload")
def handle_upload():
  return OK

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)

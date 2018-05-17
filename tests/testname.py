import unittest
import re

from media.naming import generate_name
class TestNamingGenerator(unittest.TestCase):

  def test_unique_name_generation(self):
    n1 = generate_name('omega.jpeg')
    n2 = generate_name('omega.jpeg')

    assert n1 != n2
  def test_name_generate_match_uuid(self):
    name = generate_name('omega.jpeg')
    regexp = re.compile(r'^uploads\/[0-9a-f-]{36}\/omega\.jpeg$')

    assert regexp.search(name)

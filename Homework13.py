#Homework 13 Assignment
#Jason Chan
#4/21/2025

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  """HTML Parser class that inherits from HTMLParser module and contains 4
  functions."""

  def __init__(self):
    """intitialize instance attributes that store text"""
    HTMLParser.__init__(self)
    self.data = ""


  def handle_data(self, data):
    """This method takes parsed data from a webpage that is not a tag and will store
    the data in a text variable that is initialized in the constructor. Special
    characters will be disregarded.
    """

    for char in data:
      if char not in string.punctuation:
        self.data += char
        # here you will add data to the text variable that you initialized in
        # the constructor. Each time the parser encounters data that is not tag,
        # it will call this method passing the data
        # Add clean data only. Disregard data that has special characters.
        # For that, check if any character in the word is in string.punctuation
        # If it is, return without adding the data to text

  def frequency(self, n):
    """this method should print the words that occur at least n times
    on the page"""
    char_above_n = {}
    for char in self.data:
      if self.data.count(char) >= n:
        char_above_n[char] = self.data.count(char)
    print("Words that occur at least", n, "times:")
    for key, value in char_above_n.items():
      print(key, value)



  def dump_data(self, filename):
    pass
        # write code to write the text extracted from the page to a file

if __name__ == '__main__':
  link = 'https://collegeofsanmateo.edu/wellnesscenter'
  from urllib.request import urlopen
  response = urlopen(link)
  html_page = response.read().decode().lower()
  wellness = html_page.count('wellness')
  print("'Wellness' occurs on the page", wellness, "times.")
  # Output: here you should see how many times the word 'wellness' occurs on the page
  from html.parser import HTMLParser
  parser = HTMLParser()
  parser.feed(html_page)
  # Here, add the code to test your class if this module is called as a
  # top-level module.
  # Make sure to add the call to frequency.
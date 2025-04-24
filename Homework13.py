#Homework 13 Assignment
#Jason Chan
#4/21/2025

import ssl  # Import the ssl module

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

import string #this is needed for frequency function (punctuation module needed)

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  """HTML Parser class that inherits from HTMLParser module and contains 4
  functions."""

  def __init__(self):
    """intitialize instance attributes that store text"""
    HTMLParser.__init__(self)
    self.data = ""


  def handle_data(self, data):
    """This method takes data from a HTML webpage that is not a tag and will store
    the data in a text variable. Special characters will be disregarded.
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
    data_list = self.data.split()
    char_above_n = {}
    for word in data_list:
      if data_list.count(word) >= n:
        char_above_n[word] = self.data.count(word)
    print("Words that occur at least", n, "times:")
    for key, value in char_above_n.items():
      print(key, value)



  def dump_data(self, filename):
    """This method dumps the cleaned data from a webpage into a text file"""
    with open(filename, "w") as file:
      file.write(self.data)
      # write code to write the text extracted from the page to a file

if __name__ == '__main__':
  link = 'https://collegeofsanmateo.edu/wellnesscenter'
  from urllib.request import urlopen
  response = urlopen(link)
  html_page = response.read().decode().lower()
  from html.parser import HTMLParser
  parser = MyHTMLParser()
  parser.feed(html_page)
  parser.frequency(10)

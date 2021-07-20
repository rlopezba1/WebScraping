from bs4 import BeautifulSoup  # BeautifulSoup4 package
from urllib.request import urlopen
import os

# Grab the HTML from a web page just like we did
# in the first example
my_address = "http://www.example.com"
html_page = urlopen(my_address)
html_text = html_page.read()

# Pass the HTML to the BeautifulSoup constructor.
# The second argument tells beautifulsoup which parser to use
soup = BeautifulSoup(html_text, "html.parser")

result = soup.get_text()
text = os.linesep.join([s for s in result.splitlines() if s])

print(text)
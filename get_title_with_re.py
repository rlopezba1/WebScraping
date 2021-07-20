# Import the urlopen function. We need this to read in the HTML
from urllib.request import urlopen
import re

# Set a URL that we'll try to grab some HTML from.
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Open the URL and read the HTML content into a string variable
html_page = urlopen(url)
html_text = str(html_page.read())


results =  re.search(r"<title>(.*)</title>", html_text)

print(results.group(1))
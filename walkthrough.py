from bs4 import BeautifulSoup
from urllib.request import urlopen

root_url = "https://richardadalton.github.io/scrapethissite/"
html_page = urlopen(root_url)
html_text = html_page.read()
soup = BeautifulSoup(html_text, "html.parser")

# Create a list to store our images in
# Store the images in the list
categories = soup.find_all("li", class_="category-name")

for category in categories:
    name = category.text
    category_url = category.find("a").attrs['href']
    print("Category {0} at url {1}".format(name, category_url))
    
    
    category_page = urlopen(root_url + category_url)
    html_text = category_page.read()
    soup = BeautifulSoup(html_text, "html.parser")
    
    stores = soup.find_all("li", class_="store-name")
    
    store_list = []
    for store in stores:
        print(store.text)

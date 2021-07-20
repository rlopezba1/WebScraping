from bs4 import BeautifulSoup
from urllib.request import urlopen

def scrape_category(category_url):
    html_page = urlopen(category_url)
    html_text = html_page.read()
    soup = BeautifulSoup(html_text, "html.parser")

    stores = soup.find_all("li", class_="store-name")

    store_list = []
    for store in stores:
        store_list.append(store.text)
    return store_list

def scrape_site(root_url):
    index_url = root_url + 'index.html'
    html_page = urlopen(index_url)
    html_text = str(html_page.read())
    soup = BeautifulSoup(html_text, "html.parser")

    categories = soup.find_all("li", class_="category-name")

    category_stores = {}
    for category in categories:
        name = category.text
        category_url = category.find("a").attrs['href']
        print("Getting Category {0}".format(name))
        category_stores[name] = scrape_category(root_url + category_url)
    return category_stores

print(scrape_site("https://richardadalton.github.io/scrapethissite/"))
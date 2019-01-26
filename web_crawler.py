import requests
from bs4 import BeautifulSoup

def webCrawler(max_page):
    page=1
    while page <= max_page:
        url =  'https://raleigh.craigslist.org/d/activity-partners/search/act' +str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'result-title hdrlnk'}):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1

def get_single_item(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'i-nsme'}):
        print(item_name.string)
    for link in soup.findAllll('a'):
        href = ("https://raleigh.craigslist.org/d/activity-partners/search/act" + link.get('href'))
        print(href)


webCrawler(10)

import requests
from bs4 import BeautifulSoup

def scrape_quran():
  url_stem = 'http://www.wright-house.com/religions/islam/'
  table_of_contents = requests.get('%sQuran.html' % url_stem).text

  contents_soup = BeautifulSoup(table_of_contents)
  scripture = []

  for link in contents_soup.find_all('a'):
    url = link.get('href')
    if url[:5] == 'Quran':
      scripture.append(get_quran_verse('%s%s' % (url_stem, url)))
      return scripture
  return scripture

def get_quran_verse(url):
  scripture_html = requests.get(url).text
  scripture_soup = BeautifulSoup(scripture_html)
  text = scripture_soup.get_text()

  ToC = 'Table of Contents'
  gtt = 'Go to the'

  start_index = text.index(ToC) + len(ToC)
  end_index = text.index(gtt)
  return text[start_index:end_index].strip()


scrapeture = scrape_quran()
print scrapeture


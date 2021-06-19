import requests
import re
from bs4 import BeautifulSoup

BASE_URL = "http://138.68.158.87:31601/"

def get_html_of_url(url):
    resp = requests.get(url)

    if (resp.status_code != 200):
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting ...')
        exit(1)
    
    return resp.content.decode(encoding="ISO-8859-1")

html = get_html_of_url(BASE_URL)
soup = BeautifulSoup(html, 'html.parser')
raw_text = soup.get_text()
all_words = re.findall(r'\w+', raw_text)

word_count = {}

for word in all_words:
    word_count[word] = word_count.setdefault(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

[ print(f'{item[0]}: {item[1]}') for item in sorted_words ]

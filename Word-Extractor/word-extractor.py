import click
from click.termui import prompt
import requests
import re
from bs4 import BeautifulSoup

def get_html_of_url(url):
    resp = requests.get(url)

    if (resp.status_code != 200):
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting ...')
        exit(1)
    
    return resp.content.decode(encoding="utf-8")

def map_word_ocurrences(all_words, min_length):
    word_count = {}

    for word in all_words:
        if len(word) < min_length:
            continue

        word_count[word] = word_count.setdefault(word, 0) + 1

    return word_count

def split_words_from(html):
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    all_words = re.findall(r'\w+', raw_text)

    return all_words

def sort_words(word_count):
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_words

@click.command()
@click.option('--url','-u',prompt='Web URL',help='URL of webpage to extract from.')
@click.option('--top_words','-tw',default=10, help='Number of top most frequent words to print (default: 10).')
@click.option('--length','-l',default=0, help='Minimum word lenght (default: 0, no limit).')
def main(url,length,top_words):
    """
    Count the number of occurrences of different words in a webpage
    """
    html = get_html_of_url(url)
    all_words = split_words_from(html)
    word_count = map_word_ocurrences(all_words,length)

    if len(word_count) == 0:
        print(f'No words found with in the specified length size. length: {length}. Exiting ...')
        exit(0)

    sorted_words = sort_words(word_count)
    min_value = min(len(sorted_words), top_words)

    top = 0
    while top < min_value:
        print(f'{sorted_words[top][0]}: {sorted_words[top][1]}')
        top += 1

if __name__ == "__main__":
    main()


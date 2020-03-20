import requests
from bs4 import BeautifulSoup
import urllib.parse


def fetchResults(searchTerm):
    query = urllib.parse.quote(searchTerm)
    print(query)

    googleUrl = 'https://www.google.com/search?q={}&num={}&hl={}'.format(query, 10, 'en')
    response = requests.get(googleUrl)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

fetchResults('aaa')

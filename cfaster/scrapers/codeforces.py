import requests as req
from bs4 import BeautifulSoup
from sys import exit

from .utils.files import file_saver
from .utils.urls import validate_url


def codeforces_scraper(url, **kwargs):
    if not validate_url(url, 'codeforces'):
        # TODO: logging
        exit(1)
    # TODO: documentation of the kwargs
    inputs, outputs = _scrap(url)
    file_saver(inputs, outputs)


def _scrap(url):
    res = req.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    tests = soup.find('div', {'class': 'sample-test'})
    inputs = tests.find_all('div', {'class': 'input'})
    outputs = tests.find_all('div', {'class': 'output'})
    inputs = [i.pre.text.strip() for i in inputs]
    outputs = [o.pre.text.strip() for o in outputs]
    return (inputs, outputs)

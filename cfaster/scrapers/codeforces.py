import requests as req
import logging
from bs4 import BeautifulSoup
from sys import exit

from .utils.files import file_saver
from .utils.urls import validate_url

logger = logging.getLogger(__name__)


def codeforces_scraper(url, **kwargs):
    if not validate_url(url, 'codeforces'):
        logger.error('URL passed is not a valid codeforces url')
        exit(1)
    # TODO: documentation of the kwargs
    inputs, outputs = _scrape(url)
    file_saver(inputs, outputs)


def _scrape(url):
    logger.info('Scraping ' + url)
    res = req.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    tests = soup.find('div', {'class': 'sample-test'})
    inputs = tests.find_all('div', {'class': 'input'})
    outputs = tests.find_all('div', {'class': 'output'})
    inputs = [i.pre.text.strip() + '\n' for i in inputs]
    outputs = [o.pre.text.strip() + '\n' for o in outputs]
    logger.debug(f'Number of inputs: {len(inputs)}')
    logger.debug(f'Number of outputs: {len(outputs)}')
    return (inputs, outputs)

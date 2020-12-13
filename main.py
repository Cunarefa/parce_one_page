import requests
from bs4 import BeautifulSoup
import json

HOST = 'https://www.avforums.com'  # main page url
URL = 'https://www.avforums.com/threads/samsung-q80t-qe55q80t-review-comments.2328417/'  # parsed page url
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
}


def get_html(url, params=None):  # get page html
    response = requests.get(url, params=params, headers=HEADERS)
    return response


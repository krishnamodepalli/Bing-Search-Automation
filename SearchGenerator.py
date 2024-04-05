import json
import os
import random as rn

import requests

# Constants
CATEGORIES = [
    'business',
    'entertainment',
    'general',
    'sports',
    'technology'
]
COUNTRIES = ['in', 'us', 'uk']


class SearchGenerator:
    NEWS_URL = 'https://newsapi.org/v2/top-headlines'

    def __init__(self, cat=None):
        self.category = cat

    def generate_searches(self, count: int = None) -> []:
        bing_api = os.environ['bingAPI']

        req_params = {
            'apiKey': bing_api,
            'country': rn.choice(COUNTRIES),
            'category': self.category or rn.choice(CATEGORIES),
            'pageSize': count
        }
        with requests.get(self.NEWS_URL, params=req_params) as response:
            if response.status_code != 200:
                return None
            data = json.loads(response.text)
        return [article['title'] for article in data['articles']]

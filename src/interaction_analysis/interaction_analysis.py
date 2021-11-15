import pandas as pd
import requests as rqt
import base64
from datetime import datetime, timedelta

class InteractionAnalysis():
    _accounts = []
    _hashtags = []
    _keywords = []
    _api_key = None
    _base_url = "https://api.twitter.com/"
    _auth_url = f"{_base_url}oauth2/token"

    def __init__(self, accounts=[], hashtags=[], keywords=[], start_date=None, end_date=datetime.today()):
        if len(accounts & hashtags & keywords) == 0:
            raise Exception(
                "Need at least one list of accounts, hashtags or keywords"
            )

        if not start_date:
            self._date_rage = 30
        elif not end_date:
            raise Exception("end_date can't be none")
        elif start_date > end_date:
            raise Exception("start_date can't be higher than end_date")
        else:
            self._date_rage = timedelta(end_date, start_date)

        self._accounts = accounts
        self._hashtags = hashtags
        self._keywords = keywords
        self._start_date = start_date
        self._end_date = end_date

    def set_client_credentials(self, key, secret):
        if len(key) < 1 or len(secret) < 1:
            raise Exception("Key and Secret can't be empty")
        key_secret = '{}:{}'.format(key, secret).encode('ascii')
        b64_encoded_key = base64.b64encode(key_secret)
        self._api_key = b64_encoded_key.decode('ascii')
        if not self.validate_credentials():
            raise Exception("Credentials didn't work")

    def validate_credentials(self):
        return True

    def analyze_accounts(self):
        pass

    def analyze_hashtags(self):
        pass

    def analyze_keywords(self):
        pass

    def plot_accounts_result(self):
        pass

    def plot_hashtags_result(self):
        pass

    def plot_keywords_result(self):
        pass

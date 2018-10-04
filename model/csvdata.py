import json
from urlparse import urlparse


class Csv:
    '''Common base class for all csv input'''

    def __init__(self, status, url, tld, inLink, statuscode, id=None):
        self.id = id
        self.status = status
        self.url = url
        self.tld = tld
        self.inLink = inLink
        self.statuscode = statuscode

    def split_url(self):
        if self.statuscode == 404:
            return self.url
        return urlparse(self.url).netloc

    def split_tld(self):
        # method whichs is supposed to cut out the Top-level-domain and create a new column for that
        # TODO: This method is needs to be implemented
        return "nothing"


def parse_csv_to_model(dp):
    json_output = dp.to_json(orient='records')
    return [Csv(**k) for k in json.loads(json_output)]

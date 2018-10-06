import json
from urlparse import urlparse

from tld import get_tld


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
        return get_tld(self.url)


def parse_csv_to_model(dp):
    json_output = dp.to_json(orient='records')
    return [Csv(**k) for k in json.loads(json_output)]

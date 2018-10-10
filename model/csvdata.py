import inspect
import json

from tld import get_tld, get_fld


class Csv:
    '''Common base class for all csv input'''

    def __init__(self, id=None, reach=None, url=None, tld=None, statuscode=None, globalrank=None):
        self.id = id
        self.globalrank = globalrank
        self.url = url
        self.tld = tld
        self.reach = reach
        self.statuscode = statuscode

    def split_url(self):
        if self.statuscode == 404:
            return self.url
        return get_fld(self.url, fix_protocol=True)

    def split_tld(self):
        return get_tld(self.url, fix_protocol=True)


def parse_csv_to_model(data_frame):
    json_output = data_frame.to_json(orient='records')
    return [Csv(**k) for k in json.loads(json_output)]


def check_column_with_model(data_frame):
    for column in data_frame.columns.values:
        if column not in inspect.getargspec(Csv.__init__).args:
            data_frame.drop(column, axis=1, inplace=True)
    return data_frame

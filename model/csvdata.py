import inspect
import json

from tld import get_tld, get_fld


# ------- CSVDATA.PY -------

"""
This module is a generic object class in order to handle all inputs as objects.

:copyright: (c)2018 by Michele Santoro, Steve Iva
:license: Apache 2.0, see LICENSE
"""


""" Common base class for all csv input"""
class Csv:

    def __init__(self, id=None, reach=None, url=None, tld=None, statuscode=None, globalrank=None):
        self.id = id
        self.globalrank = globalrank
        self.url = url
        self.tld = tld
        self.reach = reach
        self.statuscode = statuscode

    """
    Checks whether there is a URL with a status code of 404.
    If this is the case, the URL is left unchanged.
    If the status is other than 404, the appropriate URL will be cut down to the root domain.
    """

    def split_url(self):
        if self.statuscode == 404:
            return self.url
        return get_fld(self.url, fix_protocol=True)

    """Method for detecting the top-level domain field from the URL."""

    def split_tld(self):
        return '.' + get_tld(self.url, fix_protocol=True)


"""
Accepts raw data and creates a JSON from it.
In the next step, these in turn are converted to of a list of CSV objects and returned.
"""

def parse_csv_to_model(data_frame):
    json_output = data_frame.to_json(orient='records')
    return [Csv(**k) for k in json.loads(json_output)]


"""
Method that adjusts the incoming data with regard to the CSV object.
As soon as an entry from the CSV upload has values, that cannot be assigned to the CSV object,
the entry is deleted from the temporary data_frame and thus not is considered further in the main.py.
"""

def check_column_with_model(data_frame):
    for column in data_frame.columns.values:
        if column not in inspect.getargspec(Csv.__init__).args:
            data_frame.drop(column, axis=1, inplace=True)
    return data_frame

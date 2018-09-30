class Csv:
    'Common base class for all csv input'

    def __init__(self, status, url, tld, inLink, statuscode, index=None):
        self.index = index
        self.status = status
        self.url = url
        self.tld = tld
        self.inlink = inLink
        self.statuscode = statuscode

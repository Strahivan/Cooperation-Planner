class Csv:
    'Common base class for all csv input'

    def __init__(self, status, url, tld, inLink, statuscode, index=None):
        self.index = index
        self.status = status
        self.url = url
        self.tld = tld
        self.inlink = inLink
        self.statuscode = statuscode


    def splitURL(self):
        # method whichs is supposed to cut out the root domain
        # TODO: This method is currently in main.py, needs to be implemented here
        return "nothing"

    def checkStatusCode(self):
        # method whichs is supposed to check the statuscode, if it's a 404 return false
        # false means here that we don't have to split the URL (don't execute the method splitURL)
        # TODO: This method is currently in main.py, needs to be implemented here
        return "nothing"

    def splitTLD(self):
        # method whichs is supposed to cut out the Top-level-domain and create a new column for that
        # TODO: This method is needs to be implemented
        return "nothing"
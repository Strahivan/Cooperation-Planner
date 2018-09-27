class Csv:
   'Common base class for all csv input'

   def __init__(self, id, Status, URL, TLD, Inlink, Statuscode):
      self.id = id
      self.status = Status
      self.url = URL
      self.tld = TLD
      self.inlink = Inlink
      self.statuscode = Statuscode

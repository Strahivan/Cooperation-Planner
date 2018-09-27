class Csv:
   'Common base class for all csv input'

   def __init__(self, id, URL, Statuscode, TLD, Status, Inlink):
      self.id = id
      self.url = URL
      self.statuscode = Statuscode
      self.tld = TLD
      self.status = Status
      self.inlink = Inlink
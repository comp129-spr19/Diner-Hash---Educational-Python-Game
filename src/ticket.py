

class Ticket(object):
    
    def __init__(self, string):
        super(Ticket, self).__init__()
        self.key = string
        self.hash = None

    def set_hash(self, string):
        self.hash = string

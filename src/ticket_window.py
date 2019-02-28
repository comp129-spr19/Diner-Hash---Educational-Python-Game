from diner_sprite import (
    DinerSprite
)

from feedback import (
    show_info_feedback
)

from pygame import (
    display,
    image,
    key
)


class TicketWindow(DinerSprite):

    __IMAGE_FILE__ = "../imgs/ticketwindow.png"

    def __init__(self, x, y):
        super(TicketWindow, self).__init__(x, y)
        self.tickets = []

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def get_ticket(self):
        if self.tickets is not None and len(self.tickets) > 0:
            return self.tickets.pop()
        else:
            return None

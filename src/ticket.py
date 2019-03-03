from diner_sprite import (
    DinerSprite
)

from pygame import (
    display,
    image
)


class Ticket(DinerSprite):

    __IMAGE_FILE__ = "../imgs/ticket.png"
    
    def __init__(self, string, x, y):
        super(Ticket, self).__init__(x, y)
        self.key = string
        self.hash = None
        self.x = x
        self.y = y

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, offset):
        self.x += offset[0]
        self.y += offset[1]

        self.rect = self.rect.move(offset)

    def set_hash(self, string):
        self.hash = string

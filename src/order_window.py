from diner_sprite import (
    DinerSprite
)

from feedback import (
    show_order_feedback
)


from pygame import (
    display,
    image,
    key
)

from pygame.sprite import (
    spritecollide
)


class OrderWindow(DinerSprite):

    __IMAGE_FILE__ = "../imgs/TicketBooth.png"

    def __init__(self, x, y):
        super(OrderWindow, self).__init__(x, y)
        orders = []

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def on_event(self, keys):
        pass

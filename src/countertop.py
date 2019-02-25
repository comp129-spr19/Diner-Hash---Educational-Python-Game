from diner_sprite import (
    DinerSprite
)

from pygame import (
    display,
    image,
    key
)

from pygame.sprite import (
    spritecollide
)


class Countertop(DinerSprite):

    __IMAGE_FILE__ = "../imgs/countertop.png"

    def __init__(self, x, y):
        super(Countertop, self).__init__(x, y)
        self.food = None

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def on_event(self, keys):
        pass

from diner_sprite import (
    DinerSprite
)

from pygame import (
    image
)


class Number(DinerSprite):

    def __init__(self, x, y, f_type):
        super(Number, self).__init__(x, y)

        self.f_type = f_type

    def on_init(self):
        image_path = "../imgs/" + str(self.f_type.value) + ".png"
        self.image = image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

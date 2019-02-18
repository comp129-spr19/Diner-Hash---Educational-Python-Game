from diner_sprite import (
    DinerSprite
)

from food_type import (
    FoodType
)

from pygame import (
    image
)


class Food(DinerSprite):
    # class variables
    dict_image = {
        FoodType.BURGER: "../imgs/burger.png"
    }

    def __init__(self, x, y, f_type):
        super(Food, self).__init__(x, y)

        self.f_type = f_type

    def on_init(self):
        image_path = self.dict_image.get(self.f_type)
        self.image = image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, offset):
        self.x += offset[0]
        self.y += offset[1]

        self.rect = self.rect.move(offset)

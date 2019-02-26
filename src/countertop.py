from diner_sprite import (
    DinerSprite
)

from food import (
    Food
)

from food_type import (
    FoodType
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

    def __init__(self, x, y, food):
        super(Countertop, self).__init__(x, y)
        self.food = food

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        food_x = self.x + ((self.get_width() / 2) -
                           (self.food.get_width() / 2))
        food_y = self.y + ((self.get_height() / 2) -
                           (self.food.get_height() / 2))
        self.food.x = food_x
        self.food.y = food_y

    def on_event(self, keys):
        pass

    def add_food(self, food):
        self.food = Food

    def get_food(self):
        return self.food

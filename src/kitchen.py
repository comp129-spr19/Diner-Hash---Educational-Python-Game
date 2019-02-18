from food import (
    Food
)

from food_type import (
    FoodType
)

from pygame import (
    image,
    key
)

from pygame.sprite import (
    Group,

    spritecollide
)


class Kitchen:

    # internal constants
    __IMAGE_FILE__ = "../imgs/kitchen_floor.jpg"
    __IMAGE_X__ = 0
    __IMAGE_Y__ = 0

    def __init__(self):
        self.x = self.__IMAGE_X__    # x coordinate of image
        self.y = self.__IMAGE_Y__    # y coordinate of image
        self._image_surf = None
        self.food_orders = []
        self.food_group = Group()

    def on_init(self):
        self._image_surf = image.load(self.__IMAGE_FILE__).convert()

    def on_event(self, keys):
        pass

    def on_loop(self):
        pass

    def on_render(self, surface):
        surface.blit(self._image_surf, (self.x, self.y),
                     (self.x, self.y,
                     surface.get_width(), surface.get_height()))

    def on_cleanup(self):
        # TODO: do objects need to cleanup?
        pass

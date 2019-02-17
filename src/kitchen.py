from chef import (
    Chef
)

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

    __CHEF_START_X__ = 400  # chef starting x coordinate
    __CHEF_START_Y__ = 400  # chef starting y coordinate

    def __init__(self):
        self.x = self.__IMAGE_X__    # x coordinate of image
        self.y = self.__IMAGE_Y__    # y coordinate of image
        self._image_surf = None
        self.food_orders = []
        self.food_group = Group()

    def __init_chef__(self):
        self.chef = Chef(self.__CHEF_START_X__, self.__CHEF_START_Y__)
        self.chef.on_init()

    def __init_food__(self):
        # TODO: replace the x and y values dynamically for food
        food = Food(100, 200, FoodType.BURGER)
        food.on_init()
        self.food_group.add([food])

    def on_init(self):
        self._image_surf = image.load(self.__IMAGE_FILE__).convert()

        self.__init_chef__()    
        # This is for testing purposes, not final implementation of food
        self.__init_food__()

    def on_event(self, keys):
        self.chef.on_event(keys)
        pass

    def on_loop(self):
        sprite_collisions = spritecollide(self.chef, self.food_group, False)
        
        for sprite in sprite_collisions:
            self.chef.handle_collision(sprite)

    def on_render(self, surface):
        surface.blit(self._image_surf, (self.x, self.y),
                     (self.x, self.y,
                     surface.get_width(), surface.get_height()))

        self.chef.on_render(surface)
        
        for sprite in self.food_group:
            sprite.on_render(surface)

    def on_cleanup(self):
        # TODO: do objects need to cleanup?
        pass

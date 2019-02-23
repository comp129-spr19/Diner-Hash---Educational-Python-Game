from diner_sprite import (
    DinerSprite
)

from feedback import (
    show_info_feedback,
    show_pos_feedback,
    show_neg_feedback
)

# from feedback_msg.chef_feedback_msgs.py import (
#     GRAB_TICKET
# )

from food import (
    Food
)

from pygame import (
    # imported constants
    K_DOWN,
    K_LEFT,
    K_SPACE,
    K_RIGHT,
    K_UP,

    display,
    image,
    key
)

from pygame.sprite import (
    spritecollide
)


class Chef(DinerSprite):

    __IMAGE_FILE__ = "../imgs/chef.png"
    __SPEED__ = 8

    def __init__(self, x, y):
        super(Chef, self).__init__(x, y)

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.carry_food = None

    def on_event(self, keys):
        if (keys[K_RIGHT]):
            self.moveRight()

        if (keys[K_LEFT]):
            self.moveLeft()

        if (keys[K_UP]):
            self.moveUp()

        if (keys[K_DOWN]):
            self.moveDown()

        if (keys[K_SPACE]):
            self.handle_carry_food()

    def moveRight(self):
        self.x += self.__SPEED__
        self.rect = self.rect.move(self.__SPEED__, 0)

        self.move_carry_food(self.__SPEED__, 0)

    def moveLeft(self):
        self.x -= self.__SPEED__
        self.rect = self.rect.move(-self.__SPEED__, 0)

        self.move_carry_food(-self.__SPEED__, 0)

    def moveUp(self):
        self.y -= self.__SPEED__
        self.rect = self.rect.move(0, -self.__SPEED__)

        self.move_carry_food(0, -self.__SPEED__)

    def moveDown(self):
        self.y += self.__SPEED__
        self.rect = self.rect.move(0, self.__SPEED__)

        self.move_carry_food(0, self.__SPEED__)

    def handle_carry_food(self):
        if self.carry_food is None:
            self.pickup_food()
        else:
            self.drop_food()

    def pickup_food(self):
        from sprite_cluster import get_chef_collisions

        collisions = get_chef_collisions()

        for obj in collisions:
            if obj is not None and isinstance(obj, Food) and \
                    obj is not self.carry_food:
                self.carry_food = obj
                self.__center_food__()
                show_pos_feedback('Congratulations you picked up an item')
                break

    def drop_food(self):
        self.carry_food = None

    def move_carry_food(self, x_offset, y_offset):
        if self.carry_food is not None:
            self.carry_food.move((x_offset, y_offset))

    def __center_food__(self):
        # TODO: use // instead for integer?
        self.carry_food.set_coordinates(
            self.x + (self.get_width() / 2) -
            (self.carry_food.get_width() / 2),
            self.y + (self.get_height() / 2) -
            (self.carry_food.get_height() / 2))

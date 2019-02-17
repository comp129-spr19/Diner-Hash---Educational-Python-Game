from diner_sprite import (
     DinerSprite
)

from pygame import (
    # imported constants
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_UP,

    display,
    image,
    key
)


class Chef(DinerSprite):

    __IMAGE_FILE__ = "../imgs/chef.png"
    __SPEED__ = 1

    def __init__(self, x, y):
        super(Chef, self).__init__(x, y)

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()

    def on_event(self, keys):
        if (keys[K_RIGHT]):
            self.moveRight()

        if (keys[K_LEFT]):
            self.moveLeft()

        if (keys[K_UP]):
            self.moveUp()

        if (keys[K_DOWN]):
            self.moveDown()

    def handle_collsion(self, sprite):
        # Chef recoils in disgust!
        self.x = self.x + 50
        print("What is that!?")

    def moveRight(self):
        self.x = self.x + self.__SPEED__

    def moveLeft(self):
        self.x = self.x - self.__SPEED__

    def moveUp(self):
        self.y = self.y - self.__SPEED__

    def moveDown(self):
        self.y = self.y + self.__SPEED__

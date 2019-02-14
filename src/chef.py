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


class Chef:

    __IMAGE_FILE__ = "../imgs/chef.png"
    __SPEED__ = 1

    def __init__(self, x, y):
        self.x = x              # starting x coordinate of chef
        self.y = y              # starting y coordinate of chef
        self._image_surf = None

    def on_init(self):
        self._image_surf = image.load(self.__IMAGE_FILE__).convert_alpha()

    def on_event(self, keys):
        if (keys[K_RIGHT]):
            self.moveRight()

        if (keys[K_LEFT]):
            self.moveLeft()

        if (keys[K_UP]):
            self.moveUp()

        if (keys[K_DOWN]):
            self.moveDown()

    def on_loop(self):
        pass

    def on_render(self, surface):
        surface.blit(self._image_surf, (self.x, self.y))

    def moveRight(self):
        self.x = self.x + self.__SPEED__

    def moveLeft(self):
        self.x = self.x - self.__SPEED__

    def moveUp(self):
        self.y = self.y - self.__SPEED__

    def moveDown(self):
        self.y = self.y + self.__SPEED__

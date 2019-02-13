from pygame import (
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
        # TODO: handle key pressed events
        pass

    def on_loop(self):
        pass

    def on_render(self, surface):
        surface.blit(self._image_surf, (self.x, self.y))

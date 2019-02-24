from pygame import (
    Rect
)

from pygame.sprite import (
    Sprite
)


class DinerSprite(Sprite):

    def __init__(self, x, y):
        super(DinerSprite, self).__init__()

        self.x = x          # starting x corrdinate for sprite
        self.y = y          # starting y coordinate for sprite
        self.image = None
        self.rect = None

    def on_init(self):
        pass

    def on_event(self, keys):
        pass

    def on_loop(self):
        pass

    def on_render(self, surface):
        if self.image is not None:
            surface.blit(self.image, (self.x, self.y))

    def get_width(self):
        if self.image is not None:
            rect = self.image.get_rect()
            return rect.width
        else:
            return -1

    def get_height(self):
        if self.image is not None:
            rect = self.image.get_rect()
            return rect.height
        else:
            return -1

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

        if self.rect is not None:
            self.rect.x = x
            self.rect.y = y

from pygame import (
    display,
    draw,
    rect
)

from threading import (
    Timer
)

from system_utils import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)


class TextBox(object):
    __DISPLAY_TIME__ = 10  # in seconds

    text_box_width = WINDOW_WIDTH
    text_box_height = WINDOW_HEIGHT / 4

    def __init__(self, rect_color, rect_text):
        self.display = True
        self.rect_color = rect_color

        self.rect_text = rect_text
        self.x = WINDOW_WIDTH - self.text_box_width
        self.y = WINDOW_HEIGHT - self.text_box_height
        self.timer = Timer(self.__DISPLAY_TIME__, self.set_display_false)
        self.timer.start()

    def set_display_false(self):
        self.display = False

    def on_render(self, surface):
        draw.rect(surface, self.rect_color, (self.x, self.y,
                                             self.x + self.text_box_width,
                                             self.y + self.text_box_height))
        surface.blit(self.rect_text, (self.x, self.y))
        return self.display

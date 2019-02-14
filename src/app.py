from chef import (
    Chef
)

from kitchen import (
    Kitchen
)
from pygame.locals import *
from pygame import (
    # imported constants
    HWSURFACE,
    K_ESCAPE,
    QUIT,

    display,
    event,
    init,
    key,
    quit
)


class App:

    # internal constants
    __WINDOW_WIDTH__ = 800
    __WINDOW_HEIGHT__ = 800

    __C_START_X__ = 400  # chef starting x coordinate
    __C_START_Y__ = 400  # chef starting y coordinate

    def __init__(self):
        self._running = True
        self._display_surf = None

    def on_init(self):
        init()
        self._display_surf = display.set_mode(
            (self.__WINDOW_WIDTH__, self.__WINDOW_HEIGHT__), HWSURFACE)

        # initialize class variables
        self.kitchen = Kitchen()
        self.kitchen.on_init()

        self.chef = Chef(self.__C_START_X__, self.__C_START_Y__)
        self.chef.on_init()

        self._running = True

    def on_event(self, keys):
        if keys[K_ESCAPE]:
            self._running = False
        else:
            self.kitchen.on_event(keys)
            self.chef.on_event(keys)

    def on_loop(self):
        pass

    def on_render(self):
        # TODO: should kitchen only render once?
        self.kitchen.on_render(self._display_surf)
        self.chef.on_render(self._display_surf)

        # update display to register all changes
        display.flip()

    def on_cleanup(self):
        quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while (self._running):
            event.pump()
            keys = key.get_pressed()

            self.on_event(keys)

            if (keys[K_RIGHT]):
                self.chef.moveRight();

            if (keys[K_LEFT]):
                self.chef.moveLeft();

            if (keys[K_UP]):
                self.chef.moveUp();

            if (keys[K_DOWN]):
                self.chef.moveDown();

            if (keys[K_ESCAPE]):
                self._running = False

            

            self.on_loop()
            self.on_render()

        self.on_cleanup()

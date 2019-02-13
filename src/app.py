from kitchen import (
    Kitchen
)

from pygame import (
    # imported constants
    HWSURFACE,
    QUIT,

    display,
    event,
    init,
    quit
)


class App:

    # internal constants
    __WINDOW_WIDTH__ = 800
    __WINDOW_HEIGHT__ = 800

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

        self._running = True

    def on_event(self, e):
        if e.type == QUIT:
            self._running = False
        else:
            self.kitchen.on_event(e)

    def on_loop(self):
        pass

    def on_render(self):
        self.kitchen.on_render(self._display_surf)

    def on_cleanup(self):
        quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while (self._running):
            for e in event.get():
                self.on_event(e)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

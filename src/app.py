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
    __WINDOW_WIDTH__ = 640
    __WINDOW_HEIGHT__ = 480

    def __init__(self):
        self._running = True
        self._display_surf = None

    def on_init(self):
        init()
        self._display_surf = display.set_mode(
            (self.__WINDOW_WIDTH__, self.__WINDOW_HEIGHT__), HWSURFACE)
        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_cleanup(self):
        quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while (self._running):
            for e in event.get():
                self.on_event(e)

            self.on_loop()

        self.on_cleanup()

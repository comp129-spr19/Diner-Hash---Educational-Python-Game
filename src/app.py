from loading_screen import (
    LoadingScreen
)

from kitchen import (
    Kitchen
)

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

from system_utils import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

import feedback as fb

import sprite_cluster as sc


class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.kitchen = Kitchen()
        self.loading_screen = LoadingScreen()

        # initialize application entities
        fb.__init__()
        sc.__init__()

    def on_init(self):
        init()

        # initialize class variables
        self._display_surf = display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT), HWSURFACE)
        self.kitchen.on_init()
        self.loading_screen.on_init()
        self._running = True

        fb.on_init()
        sc.on_init()

    def on_event(self, keys, event):
        if keys[K_ESCAPE]:
            self._running = False
        else:
            self.kitchen.on_event(keys)
            sc.on_event(keys, event)

    def on_loop(self):
        self.kitchen.on_loop()
        sc.on_loop()

    def on_render(self):
        # TODO: should kitchen only render once?
        self.kitchen.on_render(self._display_surf)
        sc.on_render(self._display_surf)
        fb.on_render(self._display_surf)
        # update display to register all changes
        display.flip()

    def on_cleanup(self):
        quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        # run and unload loading screen
        self.loading_screen.run(self._display_surf)
        self.loading_screen = None

        while (self._running):
            event.pump()
            keys = key.get_pressed()

            self.on_event(keys, event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

from feedback_msgs.app_feedback_msgs import (
    WELCOME
)

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
    image,
    init,
    key,
    quit
)

from time import (
    sleep
)

import system_utils as su

import feedback as fb

import sprite_cluster as sc


class App:

    won_img = "../imgs/game_won.jpg"
    __DISPLAY_TIME__ = 5
    TOP_LEFT_X = 0
    TOP_LEFT_Y = 0

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
            (su.WINDOW_WIDTH, su.WINDOW_HEIGHT), HWSURFACE)
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

    def game_won(self):
        win_screen = image.load(self.won_img)
        self._switch_to_screen(win_screen, self._display_surf)
        sleep(self.__DISPLAY_TIME__)

    def _switch_to_screen(self, screen, surface):
        surface.blit(screen, (self.TOP_LEFT_X, self.TOP_LEFT_Y))
        display.flip()

    def on_cleanup(self):
        quit()

    def on_execute(self):
        global game_state

        if self.on_init() is False:
            self._running = False

        # run and unload loading screen
        su.game_state = su.GameState.LOADING
        self.loading_screen.run(self._display_surf)
        self.loading_screen = None
        # Displays intro message
        fb.show_info_feedback(WELCOME)

        su.game_state = su.GameState.MAIN_LOOP
        while (self._running and su.game_state == su.GameState.MAIN_LOOP):
            event.pump()
            keys = key.get_pressed()

            self.on_event(keys, event)
            self.on_loop()
            self.on_render()

        if su.game_state == su.GameState.WON:
            self.game_won()

        self.on_cleanup()

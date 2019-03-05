from pygame import (
    display,
    image
)

from time import (
    sleep
)


class LoadingScreen(object):
    # class constants
    __DISPLAY_TIME__ = 1  # in seconds
    __START_X__ = 0
    __START_Y__ = 0
    LOAD_PATH = '../imgs/loading_screens/'
    files = ['navigation.jpg', 'get_requests.jpg', 'hash_index.jpg',
             'access_index.jpg', 'return_value.jpg', 'exit_instructions.jpg']

    def __init__(self):
        super(LoadingScreen, self).__init__()
        self.images = None

    def on_init(self):
        array = []
        for file in self.files:
            file_path = self.LOAD_PATH + file
            array += [image.load(file_path)]
        self.images = array

    def run(self, surface):
        for img in self.images:
            self._switch_to_screen(img, surface)
            sleep(self.__DISPLAY_TIME__)

    def _switch_to_screen(self, screen, surface):
        surface.blit(screen, (self.__START_X__, self.__START_Y__))
        display.flip()

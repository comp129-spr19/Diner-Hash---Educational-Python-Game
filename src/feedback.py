from pygame import (
    rect,

    display
)

from pygame.font import (
    # class objects
    Font,

    SysFont,
    init
)

from text_box import (
    TextBox
)

from system_utils import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

from time import (
    clock
)

# initialize font environment
init()

# class constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
MAX_CHARS = 80
FONT = SysFont('Arial', 12, bold=True)

# feedback global variables
text_boxes = None


def __init__():
    global text_boxes
    global intro_screen_checker

    text_boxes = []
    intro_screen_checker = []


def show_game_intro():
    # # gamedisplay.fill(WHITE)
    # largeText = SysFont('Arial',155)
    # textSurf, textRect = text_objects("Testing", largeText)
    # textRect.centre = ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2))
    # # gamedisplay.blit(textSurf, textRect)
    intro_string = "Welcome"

    text = FONT.render(intro_string, True, BLACK, WHITE)
    tb = TextBox(WHITE, text)
    text_boxes.append(tb)

    # clock.tick(15)

def show_pos_feedback(string):
    _show_feedback(string, BLACK, GREEN)


def show_neg_feedback(string):
    _show_feedback(string, BLACK, RED)


def show_info_feedback(string):
    _show_feedback(string, WHITE, BLUE)


def _show_feedback(string, text_color, box_color):
    text = FONT.render(string, True, text_color, box_color)
    tb = TextBox(box_color, text)
    text_boxes.append(tb)


def on_render(surface):
    # TODO dynamically place text boxes
    for text_box in text_boxes:
        if not text_box.on_render(surface):
            text_boxes.remove(text_box)

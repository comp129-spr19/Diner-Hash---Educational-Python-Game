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
    text_boxes = []


def show_pos_feedback(string):
    # TODO use green fill here
    # render(text, antialias, color, background=None) -> Surface
    text = FONT.render(string, True, BLACK, GREEN)
    tb = TextBox(GREEN, text)

    text_boxes.append(tb)


def show_neg_feedback(string):
    # TODO use red fill here
    text = FONT.render(string, True, WHITE, RED)
    tb = TextBox(GREEN, text)

    text_boxes.append(tb)


def show_info_feedback(string):
    # TODO use blue outline (width=2) here
    text = FONT.render(string, True, WHITE, BLUE)
    tb = TextBox(GREEN, text)

    text_boxes.append(tb)


def show_order_feedback(string):
    # TODO use blue outline (width =2) right here
    text = FONT.render(string, True, WHITE, BLUE)
    tb = TextBox(GREEN, text)


def on_render(surface):
    # TODO dynamically place text boxes
    for text_box in text_boxes:
        text_box.on_render(surface)


# use this to create pos and neg feedback
# only difference is color, so this is an
# abstraction
def _show_feedback(color, string):
    pass

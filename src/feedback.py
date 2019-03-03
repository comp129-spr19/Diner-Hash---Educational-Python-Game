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

# initialize font environment
init()

# class constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

MAX_CHARS = 80
# TODO: Increase font size after implementing multi-line feedback
FONT = SysFont('Arial', 20, bold=True)

# feedback global variables
text_boxes = None


def __init__():
    global text_boxes

    text_boxes = []


def on_init():
    pass


def show_pos_feedback(string):
    _show_feedback(string, BLACK, GREEN)


def show_neg_feedback(string):
    _show_feedback(string, BLACK, RED)


def show_info_feedback(string):
    _show_feedback(string, BLACK, YELLOW)


def _show_feedback(string, text_color, box_color):
    text = FONT.render(string, True, text_color, box_color)
    tb = TextBox(box_color, text)
    text_boxes.append(tb)


def on_render(surface):
    # TODO dynamically place text boxes
    for text_box in text_boxes:
        if not text_box.on_render(surface):
            text_boxes.remove(text_box)


# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get rendered
# obtained from: https://www.pygame.org/wiki/TextWrap
def makeText(text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight &gt; rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] &lt; rect.width and i &lt; len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i &lt; len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

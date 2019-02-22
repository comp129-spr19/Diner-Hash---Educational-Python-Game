from color import (
	Color
)

from pygame import (
	rect,
)

from pygame.font import (
	# class objects
	Font,

	SysFont
)

# class constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
WHITE = (255, 255, 255)
FONT = SysFont('Arial', 12, bold=True)

# feedback global variables
text_boxes = None


def __init__(self):
	global text_boxes

	text_boxes = []

def show_pos_feedback(self, string):
	# TODO use green fill here


def show_neg_feedback(self, string):
	# TODO use red fill here


def show_info_feedback(self, string):
	# TODO use blue outline (width=2) here


def on_render(self, surface):
	# TODO dynamically place text boxes
	for text_box in self.text_boxes:
		text_box.on_render(surface)


# use this to create pos and neg feedback
# only difference is color, so this is an
# abstraction
def _show_feedback(self, color, string):
	pass
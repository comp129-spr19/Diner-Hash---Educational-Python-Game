from pygame import (
	display,
	draw,
	rect
)

from threading import (
	Timer
)

class TextBox(object):
	"""doctring for TextBox"""

	__DISPLAY_TIME__ = 10	# in seconds

	def __init__(self, rect_color, rect_text):
		self.display = True
		self.rect_color = rect_color
		self.rect_text = rect_text
		self.rect_text.x = display.width - self.rect_text.width
		self.rect_text.y = display.height - self.rect_text.height
		self.timer = Timer(self.__DISPLAY_TIME__, set_display_false)
		self.timer.start()

	def set_display_false(self):
		self.display = False

	def on_render(self, surface):
		draw.rect(surface, self.rect_color, self.rect)
		return self.display
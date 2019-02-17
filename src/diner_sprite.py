from pygame.sprite import (
	Sprite
)

class DinerSprite(Sprite):

	def __init__(self, x, y):
		super(DinerSprite, self).__init__()

		self.x = x			# starting x corrdinate for sprite
		self.y = y			# starting y coordinate for sprite
		self.image = None

	def on_init(self):
		pass
		
	def on_event(self, keys):
		pass

	def on_loop(self):
		pass

	def on_render(self, surface):
		if self.image is not None:
			surface.blit(self.image, (self.x, self.y))


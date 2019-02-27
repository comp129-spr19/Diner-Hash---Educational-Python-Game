from diner_sprite import (
    DinerSprite
)

from feedback import (
    show_neg_feedback,
    show_pos_feedback
)

from feedback_msgs.hasher_feedback_msgs import (
    NO_TICKET,
    TRANSLATED_TICKET
)

from food_type import (
    food_type_to_string,
    ticket_to_food_type
)

from pygame import (
    image
)


class Hasher(DinerSprite):

    __IMAGE_FILE__ = "../imgs/hasher.png"

    def __init__(self, x, y):
        super(Hasher, self).__init__(x, y)

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def translate_ticket(self, ticket):
        if ticket.key is not None:
            type = ticket_to_food_type.get(ticket.key)
            ticket.set_hash(food_type_to_string.get(type))
            show_pos_feedback(TRANSLATED_TICKET)
            return ticket
        else:
            show_neg_feedback(NO_TICKET)
            return None
        
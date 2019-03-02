from diner_sprite import (
    DinerSprite
)

from feedback import (
    show_neg_feedback,
    show_pos_feedback
)

from feedback_msgs.order_window_feedback_msgs import (
    INCORRECT_ORDER,
    CORRECT_ORDER,
    PICK_UP_FOOD_AND_TICKET,
    PICK_UP_FOOD,
    PICK_UP_TICKET,
    NO_HASH
)

from food_type import (
    FoodType,
    string_to_food_type
)

from pygame import (
    display,
    image,
    key
)

from pygame.sprite import (
    spritecollide
)


class OrderWindow(DinerSprite):

    __IMAGE_FILE__ = "../imgs/order_window.png"

    def __init__(self, x, y):
        super(OrderWindow, self).__init__(x, y)

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def deliver_order(self, food, ticket):
        if food is None and ticket is None:
            # No food or ticket
            show_neg_feedback(PICK_UP_FOOD_AND_TICKET)

        elif food is None and ticket is not None:
            # No food, but have a ticket
            show_neg_feedback(PICK_UP_FOOD)

        elif food is not None and ticket is None:
            # Food but no ticket
            food.kill()
            show_neg_feedback(PICK_UP_TICKET)

        elif food is not None and ticket is not None:
            # Have food and ticket
            if ticket.hash is None:
                # No ticket hash (they didn't take ticket to hasher)
                show_neg_feedback(NO_HASH)

            elif food.f_type == FoodType(ticket.hash):
                # Correct order - food and ticket match
                # TODO: add to score here
                show_pos_feedback(CORRECT_ORDER)

            else:
                show_neg_feedback(INCORRECT_ORDER)

            food.kill()

        ticket = None

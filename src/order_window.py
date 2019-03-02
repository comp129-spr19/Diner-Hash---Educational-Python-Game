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
    PICK_UP_TICKET
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
            # Tell them they need to pick up a ticket and food
            show_neg_feedback(PICK_UP_FOOD_AND_TICKET)
            
        elif food is None and ticket is not None:
            # Tell them to pick up the food
            # Set the ticket to none
            ticket = None
            show_neg_feedback(PICK_UP_FOOD)

        elif food is not None and ticket is None:
            # Kill the food
            food.kill()
            # Tell them they need to pick up a ticket before the food
            show_neg_feedback(PICK_UP_TICKET)

        elif food.f_type is FoodType(ticket.hash):
            # TODO: add to score here
            food.kill()
            show_pos_feedback(CORRECT_ORDER)

        else:
            # TODO: remove once key events are resolved
            show_neg_feedback(INCORRECT_ORDER)
            if food is not None:
                food.kill()
            ticket = None

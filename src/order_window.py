from diner_sprite import (
    DinerSprite
)

from feedback import (
    show_neg_feedback,
    show_pos_feedback
)

from feedback_msgs.order_window_feedback_msgs import (
    INCORRECT_ORDER,
    CORRECT_ORDER
)

from food_type import (
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
        if food is None or ticket is None:
            # TODO: provide feedback once key events are resolved
            return

        if food.f_type is string_to_food_type.get(ticket.hash):
            # TODO: add to score here
            food.kill()
            show_pos_feedback(CORRECT_ORDER)
        else:
            # TODO: remove once key events are resolved
            show_neg_feedback(INCORRECT_ORDER)
            if food is not None:
                food.kill()

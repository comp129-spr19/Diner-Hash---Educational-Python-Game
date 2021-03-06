from countertop import (
    Countertop
)

from diner_sprite import (
    DinerSprite
)

from feedback import (
    show_info_feedback,
    show_pos_feedback,
    show_neg_feedback
)

from feedback_msgs.chef_feedback_msgs import (
    ALREADY_GOT_FOOD,
    ALREADY_GOT_TICKET,
    GOT_FOOD,
    GOT_NO_TICKET,
    GOT_TRANSLATED_TICKET,
    NEED_TICKET,
    NO_MORE_FOOD
)

from food import (
    Food
)

from hasher import (
    Hasher
)

from order_window import (
    OrderWindow
)

from ticket import (
    Ticket
)

from ticket_window import (
    TicketWindow
)

from pygame import (
    # imported constants
    K_DOWN,
    K_LEFT,
    K_SPACE,
    K_RIGHT,
    K_UP,
    KEYDOWN,
    KEYUP,

    display,
    image,
    key,
    event
)

from pygame.sprite import (
    spritecollide
)


class Chef(DinerSprite):

    __IMAGE_FILE__ = "../imgs/chef.png"
    __SPEED__ = 4
    __CARRY_OFFSET_X__ = 35
    __CARRY_OFFSET_Y__ = 25

    def __init__(self, x, y):
        super(Chef, self).__init__(x, y)

    def on_init(self):
        self.image = image.load(self.__IMAGE_FILE__).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.carry_food = None
        self.carry_ticket = None

    def on_event(self, keys):
        if(keys[K_RIGHT]):
            self.moveRight()
        if(keys[K_LEFT]):
            self.moveLeft()
        if(keys[K_UP]):
            self.moveUp()
        if(keys[K_DOWN]):
            self.moveDown()

        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    self.handle_interaction()
            elif e.type == KEYUP:
                if e.key == K_SPACE:
                    pass

    def moveRight(self):
        self.x += self.__SPEED__
        self.rect = self.rect.move(self.__SPEED__, 0)

        self.move_carry_items(self.__SPEED__, 0)

    def moveLeft(self):
        self.x -= self.__SPEED__
        self.rect = self.rect.move(-self.__SPEED__, 0)

        self.move_carry_items(-self.__SPEED__, 0)

    def moveUp(self):
        self.y -= self.__SPEED__
        self.rect = self.rect.move(0, -self.__SPEED__)

        self.move_carry_items(0, -self.__SPEED__)

    def moveDown(self):
        self.y += self.__SPEED__
        self.rect = self.rect.move(0, self.__SPEED__)

        self.move_carry_items(0, self.__SPEED__)

    def handle_interaction(self):
        from sprite_cluster import get_chef_collisions

        collisions = get_chef_collisions()

        for obj in collisions:
            if isinstance(obj, Countertop):
                self.handle_countertop_interaction(obj)
            elif isinstance(obj, TicketWindow):
                self.handle_ticket_window_interaction(obj)
            elif isinstance(obj, OrderWindow):
                self.handle_order_window_interaction(obj)
            elif isinstance(obj, Hasher):
                self.handle_hasher_interaction(obj)
            else:
                continue

    def handle_countertop_interaction(self, countertop):
        if self.carry_food is None:
            self.carry_food = countertop.get_food()
            if self.carry_food is not None:
                # if chef is carrying food
                # have the chef carry the food
                self._center_food()
                show_info_feedback(GOT_FOOD)
            else:
                show_neg_feedback(NO_MORE_FOOD)
        else:
            show_neg_feedback(ALREADY_GOT_FOOD)

    def handle_ticket_window_interaction(self, window):
        if self.carry_ticket is None:
            self.carry_ticket = window.get_ticket()

            if self.carry_ticket is not None:
                self._center_ticket()
                show_info_feedback("This ticket key reads: " +
                                   self.carry_ticket.key + ".  Take it to the " +
                                   "hasher to find the value!")

            else:
                show_neg_feedback(GOT_NO_TICKET)
        else:
            # Chef already has a ticket
            show_neg_feedback(ALREADY_GOT_TICKET)

    def handle_order_window_interaction(self, window):
        window.deliver_order(self.carry_food, self.carry_ticket)

        # reset chef for next order
        self.carry_food = None
        self.carry_ticket = None

    def handle_hasher_interaction(self, hasher):
        if self.carry_ticket is not None:
            self.carry_ticket = hasher.translate_ticket(self.carry_ticket)
            if self.carry_ticket is not None:
                show_pos_feedback(GOT_TRANSLATED_TICKET +
                                  str(self.carry_ticket.hash))
        else:
            show_neg_feedback(NEED_TICKET)

    def move_carry_items(self, x_offset, y_offset):
        self.move_carry_food(x_offset, y_offset)
        self.move_carry_ticket(x_offset, y_offset)

    def move_carry_food(self, x_offset, y_offset):
        if self.carry_food is not None:
            self.carry_food.move((x_offset, y_offset))

    def move_carry_ticket(self, x_offset, y_offset):
        if self.carry_ticket is not None:
            self.carry_ticket.move((x_offset, y_offset))

    def _center_food(self):
        # TODO: use // instead for integer?
        self.carry_food.set_coordinates(
            self.x + (self.get_width() / 2) -
            (self.carry_food.get_width() / 2) - self.__CARRY_OFFSET_X__,
            self.y + (self.get_height() / 2) -
            (self.carry_food.get_height() / 2) + self.__CARRY_OFFSET_Y__)

    def _center_ticket(self):
        self.carry_ticket.set_coordinates(
            self.x + (self.get_width() / 2) -
            (self.carry_ticket.get_width() / 2) + self.__CARRY_OFFSET_X__,
            self.y + (self.get_height() / 2) -
            (self.carry_ticket.get_height() / 2) + self.__CARRY_OFFSET_Y__)
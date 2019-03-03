from chef import (
    Chef
)

from countertop import (
    Countertop
)

from diner_sprite import (
    DinerSprite
)

from food import (
    Food
)

from food_type import (
    FoodType
)

from hasher import (
    Hasher
)

from random import (
    randint
)

from number import (
    Number
)

from order_window import (
    OrderWindow
)

from pygame.sprite import (
    Group,

    spritecollide,
    collide_rect
)

from ticket import (
    Ticket
)

from ticket_window import (
    TicketWindow
)


chef = None
countertop_group = None
food_group = None
window_group = None
number_group = None
ticket_group = None

# Internal constants
__CHEF_START_X__ = 400          # chef starting x coordinate
__CHEF_START_Y__ = 200          # chef starting y coordinate
__HASHER_START_X__ = 25         # hasher starting x coordinate
__HASHER_START_Y__ = 200        # hasher starting y coordinate
__COUNTERTOP_WIDTH__ = 100      # TODO: FIND NON-HARD-CODED SOLUTION
__COUNTERTOP_START_X__ = 100    # countertop starting x coordinate
__COUNTERTOP_START_Y__ = 400    # countertop starting y coordinate
__TICKET_START_X__ = -600       # ticket starting x coordinate
__TICKET_START_Y__ = -600        # ticket starting y coordinate
__TICKET_WINDOW_X__ = 0       # ticket window starting x coordinate
__TICKET_WINDOW_Y__ = 0         # ticket window starting y coordinate
__ORDER_WINDOW_X__ = 600        # order window starting x coordinate
__ORDER_WINDOW_Y__ = 0         # order window starting y coordinate


def add_food(food):
    food_group.add([food])


def add_countertop(countertop):
    countertop_group.add([countertop])


def add_number(number):
    number_group.add([number])


def add_ticket(ticket):
    ticket_group.add([ticket])


def add_window(window):
    window_group.add([window])


def get_chef_collisions():
    global food_group
    global countertop_group
    global window_group

    collision_items = []

    countertop_collisions = spritecollide(chef, countertop_group, False)
    if countertop_collisions is not None:
        collision_items += countertop_collisions

    window_collisions = spritecollide(chef, window_group, False)
    if window_collisions is not None:
        collision_items += window_collisions

    return collision_items


def on_init():
    global chef
    global countertop_group
    global food_group
    global window_group
    global number_group

    chef.on_init()

    for countertop in countertop_group:
        countertop.on_init()

    for food in food_group:
        food.on_init()

    for number in number_group:
        number.on_init()

    for ticket in ticket_group:
        ticket.on_init()

    for window in window_group:
        window.on_init()


def on_event(keys, event):
    global chef
    global countertop_group
    global food_group

    chef.on_event(keys)

    for countertop in countertop_group:
        countertop.on_event(keys)

    for food in food_group:
        food.on_event(keys)

    for ticket in ticket_group:
        ticket.on_event(keys)

    for window in window_group:
        window.on_event(keys)


def on_loop():
    global chef
    global countertop_group
    global food_group
    global window_group

    chef.on_loop()

    for countertop in countertop_group:
        countertop.on_loop()

    for food in food_group:
        food.on_loop()

    for ticket in ticket_group:
        ticket.on_loop()

    for window in window_group:
        window.on_loop()


def on_render(surface):
    global chef
    global countertop_group
    global food_group
    global number_group

    # Order of rendering affects the layering of sprite

    for window in window_group:
        window.on_render(surface)

    chef.on_render(surface)

    for food in food_group:
        food.on_render(surface)

    for ticket in ticket_group:
        ticket.on_render(surface)

    for countertop in countertop_group:
        countertop.on_render(surface)

    for number in number_group:
        number.on_render(surface)


def __init__():
    __init_chef__()
    __init_food_group__()
    __init_number_group__()
    __init_countertop_group__()
    __init_ticket_group__()
    __init_window_group__()


def __init_chef__():
    global chef
    global __CHEF_START_X__
    global __CHEF_START_Y__

    chef = Chef(__CHEF_START_X__, __CHEF_START_Y__)


def __init_food_group__():
    global food_group
    food_group = Group()


def __init_countertop__():
    global countertop_group

    x = __COUNTERTOP_START_X__
    y = __COUNTERTOP_START_Y__

    for food_type in FoodType:
        food = []
        for food_count in range(0, 15):
            food.append(Food(0, 0, food_type))
        number = Number(0, 0, food_type)
        countertop = Countertop(x, y, food, number)

        for f in food:
            add_food(food)
        add_number(number)
        add_countertop(countertop)

        # increment x so next countertop is properly shifted
        # added some distance between countertops
        x = x + __COUNTERTOP_WIDTH__ + 50


def __init_countertop_group__():
    global countertop_group
    countertop_group = Group()
    __init_countertop__()


def __init_number_group__():
    global number_group
    number_group = Group()

def __init_ticket_group__():
    global ticket_group
    global __TICKET_START_X__
    global __TICKET_START_Y__
    ticket_group = Group()


def __init_window_group__():
    global window_group
    global __TICKET_WINDOW_X__
    global __TICKET_WINDOW_Y__
    window_group = Group()
    ticket_foods = ['Burger', 'Taco', 'Pizza', 'Hotdog']

    ticket_window = TicketWindow(__TICKET_WINDOW_X__, __TICKET_WINDOW_Y__)

    # TODO: remove hardcoded ticket call after demo

    # For loop will handle random ticket generation
    for tickets in range(0, 15):
        random_number = randint(0, 3)
        ticket = Ticket(ticket_foods[random_number], __TICKET_START_X__, __TICKET_START_Y__)
        ticket_window.add_ticket(ticket)
        add_ticket(ticket)

    order_window = OrderWindow(__ORDER_WINDOW_X__, __ORDER_WINDOW_Y__)

    hasher = Hasher(__HASHER_START_X__, __HASHER_START_Y__)

    add_window(ticket_window)
    add_window(order_window)
    add_window(hasher)

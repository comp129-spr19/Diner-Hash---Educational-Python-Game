from chef import (
    Chef
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

from pygame.sprite import (
    Group,

    spritecollide
)

from order_window import (
    OrderWindow
)


chef = None
countertop_group = None
food_group = None
orders = None
order_window = None
# window = Window()

# Internal constants
__CHEF_START_X__ = 400  # chef starting x coordinate
__CHEF_START_Y__ = 400  # chef starting y coordinate
__ORDER_WINDOW_X__ = 400  # Order window starting x coordinate
__ORDER_WINDOW_Y__ = 0  # Order window starting y coordinate


def add_food(food):
    food_group.add([food])


def get_food_group():
    return food_group


def add_countertop(countertop):
    countertop_group.add([countertop])


def get_countertop_group():
    return countertop_group


def add_order(order):
    global orders

    orders += [order]


def is_order(order):
    global orders

    return order in orders


def kill_food(food):
    global food_group

    if food is None:
        print("null food entry")
        return

    if food in food_group:
        food.kill()
    else:
        print("invalid food object provided")
        return


def get_chef_collisions():
    global chef
    global food_group
    global countertop_group

    collision_items = []

    food_collisions = spritecollide(chef, food_group, False)
    if food_collisions is not None:
        collision_items += food_collisions

    countertop_collisions = spritecollide(chef, countertop_group, False)
    if countertop_collisions is not None:
        collision_items += countertop_collisions

    return collision_items


def on_init():
    global chef
    global countertop_group
    global food_group
    global orders
    global order_window

    chef.on_init()
    order_window.on_init()

    for countertop in countertop_group:
        countertop.on_init()

    for food in food_group:
        food.on_init()

    for order in orders:
        order.on_init()


def on_event(keys):
    global chef
    global countertop_group
    global food_group
    global orders

    chef.on_event(keys)

    for countertop in countertop_group:
        countertop.on_event(keys)

    for food in food_group:
        food.on_event(keys)

    for order in orders:
        order.on_event(keys)


def on_loop():
    global chef
    global countertop_group
    global food_group
    global orders
    global order_window

    chef.on_loop()

    order_window.on_loop()

    for countertop in countertop_group:
        countertop.on_loop()

    for food in food_group:
        food.on_loop()

    for order in orders:
        order.on_loop()


def on_render(surface):
    global chef
    global countertop_group
    global food_group
    global orders

    chef.on_render(surface)

    order_window.on_render(surface)

    for countertop in countertop_group:
        countertop.on_render(surface)

    for food in food_group:
        food.on_render(surface)

    for order in orders:
        order.on_render(surface)


def __init__():
    __init_chef__()
    __init_food_group__()
    __init_countertop_group__()
    __init_orders__()
    __init_order_window__()

def __init_chef__():
    global chef
    global __CHEF_START_X__
    global __CHEF_START_Y__

    chef = Chef(__CHEF_START_X__, __CHEF_START_Y__)


def __init_food__():
    global food_group

    # TODO: remove after sprint 1
    food = Food(100, 200, FoodType.BURGER)

    add_food(food)


def __init_food_group__():
    global food_group
    food_group = Group()

    # TODO: remove after sprint 1 conclusion
    __init_food__()


def __init_countertop_group__():
    global countertop_group
    countertop_group = Group()


def __init_orders__():
    global orders
    orders = []

def __init_order_window__():
    global order_window
    global __ORDER_WINDOW_X__
    global __ORDER_WINDOW_Y__
    order_window = OrderWindow(__ORDER_WINDOW_X__, __ORDER_WINDOW_Y__)

from enum import (
    Enum
)


class FoodType(Enum):
    BURGER = 1
    TACO = 2
    PIZZA = 3
    HOTDOG = 4
    # TODO: add more food types


food_type_to_ticket = {
    FoodType.BURGER: "ON THE SLIDE",
    FoodType.TACO: "JUST JUAN",
    FoodType.PIZZA: "HOT PIE HOLD THE MAYO",
    FoodType.HOTDOG: "FRANK'S FURTER"
}


ticket_to_food_type = {
    "ON THE SLIDE": FoodType.BURGER,
    "JUST JUAN": FoodType.TACO,
    "HOT PIE HOLD THE MAYO": FoodType.PIZZA,
    "FRANK'S FURTER": FoodType.HOTDOG
}


food_type_to_string = {
    FoodType.BURGER: "Burger",
    FoodType.TACO: "Taco",
    FoodType.PIZZA: "Pizza",
    FoodType.HOTDOG: "Hotdog"
}

string_to_food_type = {
    "Burger": FoodType.BURGER,
    "Taco": FoodType.TACO,
    "Pizza": FoodType.PIZZA,
    "Hotdog": FoodType.HOTDOG
}


food_type_to_image = {
    FoodType.BURGER: "../imgs/burger.png",
    FoodType.TACO: "../imgs/taco.png",
    FoodType.PIZZA: "../imgs/pizza.png",
    FoodType.HOTDOG: "../imgs/hotdog.png"
}
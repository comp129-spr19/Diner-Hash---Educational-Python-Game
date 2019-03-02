from enum import (
    Enum
)


class FoodType(Enum):
    BURGER = 0
    TACO = 1
    PIZZA = 2
    HOTDOG = 3
    # TODO: add more food types


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

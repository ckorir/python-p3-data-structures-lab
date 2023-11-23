spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names
    pass

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        # Create variables for the Keys
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        # Assign emoji to heat level
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return {"name": food["name"], "cuisine": food["cuisine"], "heat_level": food["heat_level"]}
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        heat_emojis = "🌶" * heat_level

        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")
    pass

def get_average_heat_level(spicy_foods):
    # Get total for the heat levels
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    # Get the number of foods
    num_spicy_foods = len(spicy_foods)

    return total_heat_level / num_spicy_foods
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass

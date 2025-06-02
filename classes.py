# Base class for Nutrients
class Nutrient:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def get_ingredients(self):
        return self.ingredients


# Subclasses for each nutrient
class Protein(Nutrient):
    def __init__(self):
        super().__init__("Protein")
        self.ingredients = ["greek yogurt", "peanut butter", "protein powder", "milk", "tofu"]


class Fiber(Nutrient):
    def __init__(self):
        super().__init__("Fiber")
        self.ingredients = ["banana", "chia seeds", "oats", "berries", "apple"]


class VitaminC(Nutrient):
    def __init__(self):
        super().__init__("Vitamin C")
        self.ingredients = ["orange", "strawberries", "kiwi", "pineapple", "mango"]


class Iron(Nutrient):
    def __init__(self):
        super().__init__("Iron")
        self.ingredients = ["spinach", "kale", "pumpkin seeds", "tofu", "dark chocolate"]


class Potassium(Nutrient):
    def __init__(self):
        super().__init__("Potassium")
        self.ingredients = ["spinach", "avocado", "banana", "dried apricots", "yogurt"]


# Dictionary to map user input to nutrient classes
nutrient_classes = {
    "protein": Protein(),
    "fiber": Fiber(),
    "vitamin c": VitaminC(),
    "iron": Iron(),
    "potassium": Potassium()
}

# List of possible base types
base_types = ["water", "coconut water", "juice", "frozen fruit", "whole milk", "oat milk"]
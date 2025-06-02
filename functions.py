import classes

# Function to match user’s ingredients with those for the desired nutrients
'''
The function suggests smoothie ingredients based on desired nutrients, the user's available ingredients, and a chosen base.
nutrients_wanted[list[str]] argument is a list of nutrient names (strings) the user wants in their smoothie.
user_ingredients[set[str]] argument is a set of ingredient names (strings) that the user already has available.
base_choice[str] argument is a string specifying the user’s chosen liquid base (e.g., "almond milk", "yogurt").
'''
def suggest_smoothie(nutrients_wanted, user_ingredients, base_choice) -> str:
    smoothie_ingredients = set()

    for nutrient in nutrients_wanted:
        nutrient = nutrient.lower()
        if nutrient in nutrient_classes:
            for item in nutrient_classes[nutrient].get_ingredients():
                if item in user_ingredients:
                    smoothie_ingredients.add(item)
        else:
            print(f" '{nutrient}' is not recognized. Skipping.")

    if base_choice not in base_types:
        print(f" '{base_choice}' is not a recognized base. Choose from: {', '.join(base_types)}")
        base_choice = None

    if smoothie_ingredients:
        print("\n Suggested Smoothie Ingredients:")
        for ing in smoothie_ingredients:
            print(f"- {ing}")
        if base_choice:
            print(f"- Base: {base_choice}")
    else:
        print("\n No matching ingredients found for the nutrients and ingredients provided.")


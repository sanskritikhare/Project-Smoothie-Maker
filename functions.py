# Function to match user’s ingredients with those for the desired nutrients
def suggest_smoothie(nutrients_wanted, user_ingredients, base_choice):
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


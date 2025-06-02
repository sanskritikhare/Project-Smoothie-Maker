# Exception-safe input section
try:
    # User inputs
    nutrient_input = input("Enter the nutrients you want (comma separated, e.g., protein, fiber):\n> ")
    ingredients_input = input("Enter the ingredients you have (comma separated, e.g., banana, oats, milk):\n> ")
    base_input = input("Enter a base for your smoothie (e.g., water, coconut water, juice):\n> ")

    # Convert inputs to clean lists
    nutrients_wanted = [n.strip().lower() for n in nutrient_input.split(",")]
    user_ingredients = [i.strip().lower() for i in ingredients_input.split(",")]
    base_choice = base_input.strip().lower()

    # Suggest smoothie
    suggest_smoothie(nutrients_wanted, user_ingredients, base_choice)

except Exception as e:
    print("An error occurred:", e)

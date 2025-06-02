# Project-Smoothie-Maker
CSC 101 Final Project - Smoothie Maker - Sanskriti Khare &amp; Sachi Jain

classes.py:
This code defines a basic system for organizing smoothie ingredients by nutrient type.
It includes a base class Nutrient that stores a nutrient's name and a list of ingredients,
and several subclasses (Protein, Fiber, VitaminC, Iron, Potassium) that each represent a 
specific nutrient and include relevant ingredient lists. A dictionary maps nutrient names to 
their corresponding class instances, and a separate list holds possible base liquid options 
for smoothies.

functions.py:
suggest_smoothie, recommends smoothie ingredients based on the nutrients a user wants, 
the ingredients they already have, and their chosen liquid base. It checks each desired 
nutrient against a predefined list of ingredients, adds matches to the smoothie, and verifies 
if the chosen base is valid. It then prints out a list of suggested ingredients and the base, 
or notifies the user if no matches are found.

driver.py:
This section handles user input for building a custom smoothie. 
It asks the user to enter desired nutrients, available ingredients, and a smoothie base, 
then cleans and formats the inputs. It passes the data to the suggest_smoothie function and 
includes a try-except block to safely catch and report any unexpected errors during execution.
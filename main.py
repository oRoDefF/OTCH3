# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




from pprint import pprint
#ЗАДАНИЕ 1
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        count_ingredient = int(file.readline())
        ingredient_list = []
        for _ in range(count_ingredient):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredient_dict = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredient_list.append(ingredient_dict)
        file.readline()
        cook_book[dish_name] = ingredient_list

    pprint(cook_book, sort_dicts=False)

print()
print()

import copy
import re
with open("day21_input.txt", "r") as file:
    products = file.readlines()

products_split = []
for product in products:
    products_split.append([product[:product.index('(')-1].split(' '),product[(product.index('(')+10):-2].split(', ')])

set_of_allergens = set().union(*[splitprod[1] for splitprod in products_split])
set_of_all_products = set().union(*[splitprod[0] for splitprod in products_split])

possible_products = []
for allergen in set_of_allergens:
    potential_containing_products = [products[0] for products in products_split if allergen in products[1]]
    containing_products = set_of_all_products.intersection(*[list for list in potential_containing_products])
    possible_products.append([allergen, list(containing_products)])

# by inspection
allergens_dict = {
    'soy': 'cmbcm',
    'wheat': 'dvnbh',
    'nuts': 'bbbl',
    'shellfish': 'cbmjz',
    'fish': 'ttbrlvd',
    'peanuts': 'lmds',
    'eggs': 'htxsjf',
    'dairy': 'cfzdnz'
}

list_of_allergen_containing_foods = [allergens_dict[allergen] for allergen in set_of_allergens]

all_ingreds_lists = [products[0] for products in products_split]
all_ingreds = []
for list in all_ingreds_lists:
    all_ingreds += list

for food in list_of_allergen_containing_foods:
    while food in all_ingreds:
        all_ingreds.remove(food)

alpha_list_of_allergens = sorted(set_of_allergens)
part2_answer = ','.join([allergens_dict[aller] for aller in alpha_list_of_allergens])
class Day14:
    total_ore = 0
    ingredient_dict = {}
    product_dict = {}
    start_ore = 1000000000000

    def __init__(self):
        pass


def find_product(reaction):
    # print(reaction[2])
    chemicals = [c for c in reaction.split(" ")]
    # print(chemicals)
    product = chemicals[-1]
    quantity = chemicals[-2]
    # print(product)
    # print(quantity)
    return product, quantity


def find_ingredients(reaction):
    chemicals = [c for c in reaction.split(" ")]
    chemicals = chemicals[:-3]
    names = chemicals[1::2]
    quantities = chemicals[0::2]
    new_names = []
    if len(names) > 1:
        for name in names[:-1]:
            # print("name: " + name)
            new_name = remove_comma(name)
            new_names.append(new_name)
        new_names.append(names[-1])
        return new_names, quantities
    else:
        return names, quantities
    # print(chemicals)


def remove_comma(name):
    return name[0:-1]


def find_all_ore(chemical, needed_quantity, all_reactions):
    # print("chemical: " + chemical)
    # print("needed: " + str(needed_quantity))
    for reaction in all_reactions:
        product = find_product(reaction)
        product_name = product[0]
        product_quantity = int(product[1])

        if chemical == product_name:

            total_batch = product_quantity
            k = 1
            while total_batch < needed_quantity:
                k += 1
                total_batch += product_quantity
            if product_name in Day14.product_dict:
                Day14.product_dict[product_name] += total_batch
            else:
                Day14.product_dict[product_name] = total_batch
            ingredients = find_ingredients(reaction)
            ingredient_names = ingredients[0]
            ingredient_quantities = ingredients[1]
            # print("ingredients: " + str(ingredients))
            for i, ingredient in enumerate(ingredient_names):
                # print(ingredient)
                ingredient_quantity = k * int(ingredient_quantities[i])
                # print("ingredient_quantity: " + str(ingredient_quantity))
                if ingredient in Day14.product_dict:
                    # print(ingredient)
                    # print("product dict: " + str(Day14.product_dict))
                    if ingredient_quantity >= Day14.product_dict[ingredient]:
                        ingredient_quantity -= Day14.product_dict[ingredient]
                        Day14.product_dict[ingredient] = 0
                    else:
                        Day14.product_dict[ingredient] -= ingredient_quantity
                        # print("product dict: " + str(Day14.product_dict[ingredient]))
                        ingredient_quantity = 0

                Day14.product_dict[product_name] = total_batch - needed_quantity
                # print("first add product dict: " + str(Day14.product_dict))
                if ingredient in Day14.ingredient_dict:
                    Day14.ingredient_dict[ingredient] += ingredient_quantity
                else:
                    Day14.ingredient_dict[ingredient] = ingredient_quantity
                if ingredient == "ORE":
                    # print("ORE found")
                    # print(ingredient_quantity)
                    Day14.total_ore += int(ingredient_quantity)
                elif ingredient_quantity > 0:
                    # print("ingredient: " + ingredient)
                    more = True
                    find_all_ore(ingredient, ingredient_quantity, all_reactions)
            # print("total ore: " + str(Day14.total_ore))


if __name__ == '__main__':
    day14 = Day14()
    print("Im day 14 2019")
    file = "day14.txt"
    file = "day14_test5.txt"
    input_list = []
    with open(file, "r") as inputs:
        input_list = inputs.read().splitlines()
    print(input_list)
    # all_reactions = input_list
    # print(input_list[0])
    # find_ingredients(input_list[0])
    end_product = "FUEL"
    diff_list = []
    ore = 0
    k = 0
    while Day14.total_ore < 100000000:
        k += 1
        find_all_ore(end_product, 1, input_list)
    print("dict ore: " + str(Day14.ingredient_dict["ORE"]))
    print(Day14.product_dict)
    print(k)



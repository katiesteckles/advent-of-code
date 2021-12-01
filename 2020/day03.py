with open("day03_input.txt", "r") as file:
    trees = file.readlines()
trees = [x[:-1] for x in trees]


def slope_route(trees, across, down):
    route = []
    for i in range(int(len(trees) / down)):
        route.append(trees[i * down][(across * i) % len(trees[0])])
    return route

list_of_things = [[1,1],[3,1],[5,1],[7,1],[1,2]]

def count_trees(trees, things):
    items = [slope_route(trees, x[0], x[1]).count('#') for x in things]
    product = 1
    for x in items:
        product *= x
    return product

count_trees(trees, list_of_things)
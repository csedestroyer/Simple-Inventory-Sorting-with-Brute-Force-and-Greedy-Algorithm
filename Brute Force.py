import itertools

class Item:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

def knapsack_brute_force(items, limit):
    num_items = len(items)
    max_value = 0
    best_combination = []
    combinations = itertools.product([0, 1], repeat=num_items)

    for combination in combinations:
        total_value = 0
        total_weight = 0
        selected_items = []

        for i in range(num_items):
            if combination[i] == 1:
                total_value += items[i].rarity
                total_weight += 1
                selected_items.append(items[i])

        if total_weight <= limit and total_value > max_value:
            max_value = total_value
            best_combination = selected_items

    return best_combination

# Main code
items = [
    Item("N Sword", 10),
    Item("sand", 1),
    Item("N Pickaxe", 4),
    Item("N Shovel", 2),
    Item("N axe", 4),
    Item("Crossbow", 2),
    Item("E Bow", 10),
    Item("Golden Arrow", 6),
    Item("Golden Apple", 8),
    Item("Dirt", 1),
    Item("Arrow Of poison", 8),
    Item("Arrow", 7),
    Item("Diamond Sword", 8),
    Item("Diamond pickaxe", 3),
    Item("E Golden Apple", 10),
    Item("Shield", 10),
    Item("Dirt", 1),
    Item("End Crystal", 10),
    Item("Arrow of Weakness", 9)
]

limit = 9

selected_items = knapsack_brute_force(items, limit)
for item in selected_items:
    print(f"Selected item: {item.name}, Rarity: {item.rarity}")

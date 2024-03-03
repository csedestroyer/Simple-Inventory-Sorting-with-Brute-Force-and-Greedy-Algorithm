def knapsack_g(items, limit, item_limit):
    sorted_items = sorted(items, key=lambda x: x['kelangkaan'], reverse=True)
    knapsack = []
    weight = 0
    count = 0

    for item in sorted_items:
        if weight + item['berat'] <= limit and count < item_limit:
            knapsack.append(item)
            weight += item['berat']
            count += 1

    return knapsack

items = [
    {'nama': 'N Sword', 'kelangkaan': 10, 'berat': 4},
    {'nama': 'Sand', 'kelangkaan': 1, 'berat': 2},
    {'nama': 'N Pickaxe', 'kelangkaan': 4, 'berat': 3},
    {'nama': 'N Shovel', 'kelangkaan': 2, 'berat': 2},
    {'nama': 'N Axe', 'kelangkaan': 4, 'berat': 2},
    {'nama': 'Crossbow', 'kelangkaan': 2, 'berat': 7},
    {'nama': 'E Bow', 'kelangkaan': 10, 'berat': 3},
    {'nama': 'Golden Arrow', 'kelangkaan': 6, 'berat': 3},
    {'nama': 'Golden Apple', 'kelangkaan': 8, 'berat': 2},
    {'nama': 'Dirt', 'kelangkaan': 1, 'berat': 2},
    {'nama': 'Arrow of Poison', 'kelangkaan': 8, 'berat': 4},
    {'nama': 'Arrow', 'kelangkaan': 7, 'berat': 2},
    {'nama': 'Diamond Sword', 'kelangkaan': 8, 'berat': 4},
    {'nama': 'Diamond Pickaxe', 'kelangkaan': 3, 'berat': 3},
    {'nama': 'E Golden Apple', 'kelangkaan': 10, 'berat': 1},
    {'nama': 'Shield', 'kelangkaan': 10, 'berat': 4},
    {'nama': 'Dirt', 'kelangkaan': 1, 'berat': 2},
    {'nama': 'End Crystal', 'kelangkaan': 10, 'berat': 1},
    {'nama': 'Arrow Of Weakness', 'kelangkaan': 9, 'berat': 2},
]

limit = 20
item_limit = 9

knapsack = knapsack_g(items, limit, item_limit)
total_kelangkaan = sum(item['kelangkaan'] for item in knapsack)

print("Item yang diambil adalah:")
for item in knapsack:
    print(item['nama'])

print("Total kelangkaan:", total_kelangkaan)

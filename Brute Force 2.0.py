import itertools
import time

print("============TUBES STRATEGI ALGORITMA============\n")
print("=================Daftar Kelompok================\n")
print("1. Adisaputra Nur Aminta     -1301210419\n")
print("2. Daffa Afia Rizfazka       -1301213215\n")
print("3. Muhammad Dzaky Reynaldy   -1301213035\n")


def knapsack_greedy(items, limit, item_limit):
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

def knapsack_brute_force(items, limit, item_limit):
    max_kelangkaan = 0
    best_combination = []
    combinations = itertools.combinations(items, item_limit)

    for combination in combinations:
        total_berat = sum(item['berat'] for item in combination)
        if total_berat <= limit:
            total_kelangkaan = sum(item['kelangkaan'] for item in combination)
            if total_kelangkaan > max_kelangkaan:
                max_kelangkaan = total_kelangkaan
                best_combination = list(combination)

    return best_combination

def print_knapsack(knapsack):
    print("item pada inventory:")
    for item in knapsack:
        print(item['nama'])


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

while True:
    print("\n=== Menu ===")
    print("1. Greedy")
    print("2. Brute Force")
    print("3. Keluar")

    choice = input("Pilih metode yang ingin digunakan (1/2/3): ")

    if choice == '1':
        start_time = time.time()
        knapsack = knapsack_greedy(items, limit, item_limit)
        total_kelangkaan = sum(item['kelangkaan'] for item in knapsack)
        end_time = time.time()

        print_knapsack(knapsack)
        print("Total kelangkaan:", total_kelangkaan)
        print("Waktu eksekusi:", end_time - start_time, "detik")
    elif choice == '2':
        start_time = time.time()
        knapsack = knapsack_brute_force(items, limit, item_limit)
        total_kelangkaan = sum(item['kelangkaan'] for item in knapsack)
        end_time = time.time()

        print_knapsack(knapsack)
        print("Total kelangkaan:", total_kelangkaan)
        print("Waktu eksekusi:", end_time - start_time, "detik")
    elif choice == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

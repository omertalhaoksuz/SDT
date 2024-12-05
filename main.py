import random

def create_table():
    table = [random.randint(1, 100) for _ in range(5)]
    print("Unsorted table:", table)
    table.sort()
    print("Sorted table:", table)

if __name__ == "__main__":
    create_table()

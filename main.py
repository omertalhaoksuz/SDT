import random

def create_table():
    table = [random.randint(1, 100) for _ in range(5)]
    for item in table:
        print(item)

if __name__ == "__main__":
    create_table()


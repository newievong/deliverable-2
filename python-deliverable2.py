cost = 0
apple = 0
grape = 0
orange = 0


name = input("Welcome to GC fruit market! What is your name?")
print("Welcome" + name + "! Which fruit would you like to buy?")
fruit_options = ["Apple $2", "Grape $1", "Orange $3"]
print(f"1. {fruit_options[0]}")
print(f"2. {fruit_options[1]}")
print(f"3. {fruit_options[2]}")
select_fruit = int(input(">"))

if select_fruit == 1:
    cost += 2
    apple += 1
    print("You bought 1 apple at $2")
if select_fruit == 2:
    cost += 1
    grape += 1
    print("You bought 1 grape at $1")
if select_fruit == 3:
    cost += 3
    orange += 1
    print("You bought 1 orange at $3")
print("Would you like to buy another piece of fruit? y/n")
more_fruit = input(">")

while more_fruit == "y":
    select_fruit = int(input("Welcome" + name + "! Which fruit would you like to buy?"))
    if select_fruit == 1:
        cost += 2
        apple += 1
        print("You bought 1 apple at $2")
        print("Would you like to buy another piece of fruit? y/n")
        more_fruit = input(">")
    if select_fruit == 2:
        cost += 1
        grape += 1
        print("You bought 1 grape at $1")
        print("Would you like to buy another piece of fruit? y/n")
        more_fruit = input(">")
    if select_fruit == 3:
        cost += 3
        orange += 1
        print("You bought 1 orange at $3")
        print("Would you like to buy another piece of fruit? y/n")
        more_fruit = input(">")
else:
    tax = float(0.05 * cost)
    total = tax + cost
    print(f"Receipt for {name}")
    print(f"{apple} apple(s) at $2 apiece")
    print(f"{grape} grape(s) at $1 apiece")
    print(f"{orange} orange(s) at $3 apiece")
    print(f"Subtotal: ${cost}")
    print(f"5% Tax: ${tax}")
    print(f"Total: ${total}")










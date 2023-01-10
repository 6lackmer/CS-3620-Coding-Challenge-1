def part1():
    print("Part 1:")
    print("-------")

    p = int(input("Enter the principle amount: "))
    n = int(input("Enter the number of years: "))
    r = int(input("Enter the interest rate: "))

    simple_interest = (p * n * r) / 100

    print("Simple interest value:", simple_interest)
    print("\n\n")


def part2():
    print("Part 2:")
    print("-------")

    favorite_food_items = ["Steak", "Eggs", "Rice", "Bacon", "Sushi"]

    print(favorite_food_items[2])

    favorite_food_items.append("Ice Cream")
    favorite_food_items.append("Curry")
    favorite_food_items.append("Oatmeal")

    print(favorite_food_items)

    favorite_food_items.insert(2, "Tacos")
    print(favorite_food_items)
    print("\n\n")


def part3():
    print("Part 3:")
    print("-------")

    for i in range(5):
        print("I am a programmer")

    print()

    def square():
        for x in range(1, 10):
            print(pow(x, 2))

    square()


part1()
part2()
part3()

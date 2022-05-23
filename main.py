def display(collection):
    if len(collection) == 0:
        print("NO PIZZAS")
        return
    collection.sort()
    no_of_pizza = len(collection)
    print(f"------------------------------- PIZZA ({no_of_pizza}) -------------------------------")
    for i in collection:
        print(i)

    print()
    print(f"First Pizza is {collection[0]} .")
    print(f"Last Pizza is {collection[-1]} .")


def pizza_exists(element, collection):
    for item in collection:
        if element.lower() == item.lower():
            return True
    return False


def add_pizza(collection):
    print("Enter The Name of Pizza That You Want to add .")
    pizza = input("-:> ")
    if pizza_exists(pizza, collection):
        print("ERROR: This Pizza Already Exists .")
    else:
        collection.append(pizza)


pizzas = ["4 Cheese Pizza", "Cheese Burst Pizza", "Vegetarian Pizza", "Hawaii Pizza", "Calzone Pizza", "4 seasons "
                                                                                                       "Pizza"]
print("Do You Want to add Pizza 1 for Yes 0 For No .")
user_add_pizza = input("-:> ")
if user_add_pizza == "1":
    add_pizza(pizzas)

display(pizzas)

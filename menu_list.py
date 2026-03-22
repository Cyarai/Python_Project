while True: 

    menu = {"pizza": 5.00,
            "popcorn": 4.00,
            "fries": 3.00,
            "soda": 2.00,
            "water": 1.00}

    cart = []
    total = 0
    print("----------- Order List -----------")
    for key, value in menu.items():
        
        print(f"{key.title():15}: {value:.2f}")
    print("----------------------------------")

    while True:

        food_list = input("Select an item (Click 'q' to Check out): ").lower()
        if food_list == 'q':
            break
        elif menu.get(food_list) is not None:
            cart.append(food_list)
        else: 
            print("Iten are not in the Menu")


    print("------------You're Order-------------")
    for food_list in cart:
        price = menu.get(food_list)
        total += price
        print(f"Your Order is : {food_list.title()} ${price:.2f} ")
    print("-------------------------------------")


    print(f"You're total is : ${total:.2f}")

    order_again = input("Do you want to order again (yes or no): ").strip().lower()

    if order_again != 'yes':
        print("Thank you come again")
        break
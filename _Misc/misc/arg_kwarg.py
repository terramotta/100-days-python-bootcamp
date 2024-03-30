def order_pizza(size, *toppings, **delivery_details):
    print(f"Ordering a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print("\nDetails of the order are:")
    for key, value in delivery_details.items():
        print(f"- {key}: {value}")

order_pizza("large", "pepperoni", "mushrooms", delivery=True, tip=5.00)
# First input is assigned to size, and the rest are packed into a tuple called toppings
# Keyword arguments are packed into a dictionary called delivery_details



nums = [2, 5, 7, 1, 9]
print(nums)         # [2, 5, 7, 1, 9]
print(*nums)        # 2 5 7 1 9
# *nums é um argumento de desempacotamento, que desempacota a lista nums em seus elementos individuais



#pylint: disable-all
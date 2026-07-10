# Define the newu of restaurant menu items
menu = {
    'Pizza': 70,
    'Burger': 35,
    'Pasta': 50,
    'Salad': 70,
    'Sushi': 50,
    'Coffee': 40,
}

# Greet the user and display the menu 
print("Welcome to our restaurant!")
print("Pizza: Rs70\nBurger: Rs35\nPasta: Rs50\nSalad: Rs70\nSushi: Rs50\nCoffee: Rs40")

order_total = 0
# 70 + 35 = 105

item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1} has been added to your order")
    
else:
    print(f"Ordered item {item_1} is not available yet")
    
another_order = input("do you want to add another item? (yes/No)")   
if another_order == "Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet")
 
 
print(f"Your total order amount of items to pay is: Rs{order_total}")       

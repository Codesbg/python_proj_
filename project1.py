# define menu of restaurant

menue: dict[str, dict[str, int] | dict[str, int] | dict[str, int] | dict[str, int]]={
"Appetizers": {
        "Spring Rolls": 150,
        "Garlic Bread": 150,
        "Stuffed Mushrooms": 150,
        "Caesar Salad": 180
    },
    "Main Courses": {
        "Grilled Chicken": 800,
        "Spaghetti Bolognese": 600,
        "Vegetarian Pizza": 900,
        "Fish and Chips": 800
    },
    "Desserts": {
        "Chocolate Cake": 1200,
        "Cheesecake": 1100,
        "Ice Cream Scoop": 450,
        "Apple Pie": 450
    },
    "Beverages": {
        "Coca-Cola": 200,
        "Fresh Orange Juice": 200,
        "Latte": 300,
        "Espresso": 600,
        "Mineral Water": 90
    }
}
def is_item_in_menue(item, menue ):
    return any(item in menue[category] for category in menue)

#greet from coustumers
def greet_customer():
    print("Welcome to The Gourmet Haven!")
    print("We are delighted to have you here.")
greet_customer()

# display the menue
print("\nAppetizers :")
for appetizer,price in menue["Appetizers"].items():
    print(f" {appetizer}:- {price:.2f}")

print("\nMain Courses :")
for main_course,price in menue["Main Courses"].items():
    print(f" {main_course}:- {price:.2f}")

print("\nDesserts :")
for desert,price in menue["Desserts"].items():
    print(f" {desert}:- {price:.2f}")

print("\nBeverages:")
for bevarage,price in menue["Beverages"].items():
    print(f" {bevarage}:- {price:.2f}")

#now have order from menue and get the price total
order_total=0

item = input("\nPlease enter the name of the item you'd like to order: ")

if item in menue ["Appetizers"] :
    order_total += menue["Appetizers"][item]

if item in menue ["Main Courses"] :
    order_total += menue["Main Courses"][item]

if item in menue ["Desserts"] :
    order_total += menue["Desserts"][item]

if item in menue ["Beverages"] :
    order_total += menue["Beverages"][item]

elif not is_item_in_menue(item, menue):
    print("Enter something else which is present in our menu.")

print(f"Order total: {order_total}")


another_item = input("do you want another item ? (yes/no):")
if another_item == "yes":
    item2=input("enter your next item :")
    if item2 in menue["Appetizers"]:
        order_total += menue["Appetizers"][item2]

    if item2 in menue["Main Courses"]:
        order_total += menue["Main Courses"][item2]

    if item2 in menue["Desserts"]:
        order_total += menue["Desserts"][item2]

    if item2 in menue["Beverages"]:
        order_total += menue["Beverages"][item2]


new_order_total = order_total
print(new_order_total)

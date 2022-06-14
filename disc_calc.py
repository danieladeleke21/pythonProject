# Program to calculate the discount of items

print("Welcome to discount calculator")
try:
    item_types = float(input("Input the number of various Items you want to calculate:"))
except ValueError:
    print("Input a float value")

i = 1
while i <= item_types:
    item_name = input("Name of item " + str(i) +":")
    try:
        item_price = float(input("Input the price of " + item_name + " :"))
        no_item = float(input("Input the number of " + item_name+ " being calculated:"))
        discount = float(input("Input the discount of one " + item_name + " :"))
    except ValueError:
        print = ("Input a float value")
    final_price = item_price * no_item * (100 - discount) / 100
    print("Discount price of " + str(no_item)+ " " + item_name + " is "+ str(final_price))
    i += 1

print("Thanks for using Discount calculator")



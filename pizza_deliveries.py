print("Welcome to Python Pizza Deliveries!")
size= input("What size pizza do you want? S, M or L: ")
pepperoni= input("do you want pepperoni on your pizza? Y or N: ")
extra_cheese= input("Do you want extra cheese? Y or N: ")

bill= 0
if size == "S":
    bill += 15
    print("Small size pizza cost: $15.")
elif size == "M":
    bill += 20
    print("Medium size pizza cost: $20.")
elif size == "L":
    bill += 25
    print("Large size pizza cost: $25.")
else:
    print("You typed the wrong input.")

if pepperoni == "Y" or pepperoni == "y":
    if size == "S":
        bill += 2
        print("Adding pepperoni cost: $2.")
    elif size == "M" or size == "L":
        bill += 3
        print("Adding pepperoni cost: $3.")
elif pepperoni == "N" or pepperoni == "n":
    bill = bill
if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1
    print("Extra cheese cost: $1.")
elif extra_cheese == "N" or extra_cheese == "n":
    bill = bill

print(f"Your final bill is: ${bill}.")
print("Welcome to the rollercoaster!")
height= int(input("What is yur height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age= int(input("What is your age? "))
    if age < 12:
        bill= 5
        print("Child tickets are $5.")
    elif age >= 12 and age <= 18:
        bill= 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill=0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill= 12
        print("Adult tickets are $12.")
    
    Wants_photo= input("Do you want a photo take? Type y for Yes and n for No. ")
    if Wants_photo == "Y" or Wants_photo == "y":
        bill += 3
        print(f"Your final bill is ${bill}.")
    elif Wants_photo == "N" or Wants_photo == "n":
        print(f"Your final bill is ${bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")
weight= float(input("Enter your weight: "))
height= float(input("Enter your height: "))
bmi= weight / (height ** 2)
print("Your BMI is: " + str(round(bmi, 3)))
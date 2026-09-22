name = input("Enter your name: ")
name = name.title()
print("hello",name)
weight = float(input("What is your weight?"))
height = float(input("What is your height?"))
bmi = weight / (height/100)**2
print("Your BMI is:", bmi,"Thank you for using our BMI calculator!")
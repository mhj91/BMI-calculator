print("Welcome to the Body Mass Index Calculator\n")
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilograms: "))

bmi = weight / (height + height)

message = "\nPlease be informed that BMI is a bad measurement for weight issues and health in general.\nIf you experience weight related issues please contact a health professional for guidance.\n"

if 18.5<= bmi <24.9:
    print(message + "\nYour BMI is: " + str(bmi) + "\nYour BMI is in the category: Normal Weight.")
elif 25<= bmi <29.9:
    print(message + "\nYour BMI is: " + str(bmi) + "\nYour BMI is in the category: Overweight")
elif bmi >= 30: 
    print(message + "\nYour BMI is: " + str(bmi) + "\nYour BMI is in the category: Obesity.")
elif 15<= bmi <18.5:
    print(message + "\nYour BMI is: " + str(bmi) + "\nYour BMI is in the category: Underweight.")
elif 9 <= bmi <15:
    print(message + "\nYour BMI is: " + str(bmi) + "\nYour BMI is in the category: Severe Underweight.")

else: 
    print("Please try to type in your height and weight again. " + "\nIt is important that you write your height in meters.\nF.x. 1.75")

 

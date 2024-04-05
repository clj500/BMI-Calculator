import bmi

#Prompt user to enter height (in feet and inches) and store it
height = float(input("Enter height (in inches): "))

#Prompt user to enter weight (in lbs) and store it
weight = float(input("Enter weight (in lbs): "))

height = bmi.convertHeight(height)
weight = bmi.convertWeight(weight)
BMI = bmi.calculateBMI(weight, height)
category = bmi.categorize(BMI)

#Return BMI and Category
print(f'Your BMI is: {BMI:.2f}')
print("You are: " + category)

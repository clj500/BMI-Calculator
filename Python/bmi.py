#Convert height
def convertHeight(height):
    newHeight = height * 0.025
    newHeight = newHeight * newHeight
    return newHeight

#Convert weight
def convertWeight(weight):
    newWeight = weight * 0.45
    return newWeight

#Convert BMI
def calculateBMI(weight, height):
    return weight/height

#Identify category
def categorize(BMI):
    if BMI < 0:
        category = "Error"
    elif BMI < 18.5:
        category = "Underweight"
    elif BMI >= 18.6 and BMI < 25:
        category = "Normal Weight"
    elif BMI >= 25 and BMI < 30 :
        category = "Overweight"
    elif BMI >= 30 :
        category = "Obese"
    else:
        print("ERROR")

    return category

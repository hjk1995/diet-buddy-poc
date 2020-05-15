import json
with open('dishes.json', 'r') as f:
    dishes_dict = json.load(f)

def findNutrientsByDiet(dish, field):
    nutrientObj = {}
    for nutrient in dish['nutrients']:
        if nutrient['name'] == field:
            nutrientObj = nutrient
    return "Value: ",nutrientObj['value']," and Percentage: ",nutrientObj['percentage']

def dietByChoice():
    print("How would u like to have Diet??")
    for index, dish in enumerate(dishes_dict):
        print(index+1,". ",dish['name'])
    choice_2 = int(input("Choice:"))
    dishObject = dishes_dict[choice_2-1]
    print("Dish Name: ", dishObject['name'])
    print("Calories: ", dishObject['calories'])
    print("Cholestrol: ", findNutrientsByDiet(dishObject,'Cholestrol'))
    print("Sodium: ", findNutrientsByDiet(dishObject,'Sodium'))
    print("Potassium: ", findNutrientsByDiet(dishObject,'Potassium'))
    print("Carbohydrates: ", findNutrientsByDiet(dishObject,'Carbohydrates'))
    print("Fat: ", findNutrientsByDiet(dishObject,'Fat'))
    return dishObject
def dietByNutrients():
    return "Nutrients"

def selectChoice1(argument):
    switcher = {
        1: dietByChoice,
        2: dietByNutrients,
    }
    func = switcher.get(argument, lambda: "Invalid month")
    return func()

print("Hello!!!")
print("Welcome to Diet Mate")
print("Can you please Enter your Details??")
name = input("Name:")
height = float(input("Height (in Meter):"))
weight = float(input("Weight (in Kg):"))
age = int(input("Age:"))
gender = input("Gender:")
bmi = (weight/pow(height, 2))
print("Your BMI Value is",bmi)
if bmi < 18.5:
    print("You are Under Weight")
elif bmi >=18.5 and bmi<=25:
    print("You are Normal")
elif bmi >=25 and bmi <=30:
    print("You are Obese")
else:
    print("You are Over Weight")
print("How would u like to have Diet??")
print("1. Diet by Choice")
print("2. Diet by Nutrients")
choice_1 = int(input("Choice:"))
selectChoice1(choice_1)

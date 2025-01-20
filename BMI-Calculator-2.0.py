print("Welcome to the BMI Calculator 2.0!!!")
print("<<<<<<<<<<================>>>>>>>>>>")

weight = float(input("Enter your weight in kilograms(kg): "))
height = float(input("Enter your height in metres(m): "))

bmi = round(weight / height ** 2, 2)

if(bmi < 18.5):
    print(f"Your bmi is {bmi}, you are Underweight, Bulk up my friend!!!")
elif(bmi < 25):
    print(f"Your bmi is {bmi}, you have a Normal weight, keep it up!")
elif(bmi < 30):
    print(f"Your bmi is {bmi}, you are slightly Overweight, its not that hard to loose weight!")
elif(bmi < 35):
    print(f"Your bmi is {bmi}, you are Obese, Please start exercising!")
else:
    print(f"Your bmi is {bmi}, you are Critically Obese, Visit a fitness trainer in vicinity immediately!!!")
    
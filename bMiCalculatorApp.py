###Don't change the code below

height = float(input("enter your height in m: "))

weight = float(input("enter your weight in kg: "))

##Don't change the code above

###write your code below this line ;)

####create a bmi variable and set the bmi calculation into that use round to format the value

bmi = round (weight / pow(height,2))

if bmi < 18.5:
    print(f"Your BMI is {bmi} ,you are underweight")

elif bmi < 25:
    print(f"Your BMI is {bmi} ,you have a normal weight")

elif bmi < 30:
    print(f"Your BMI is {bmi} ,you are overweight")

elif bmi < 35:
    print(f"Your BMI is {bmi} ,you are obese")

else:
    print(f"Your BMI is {bmi} ,you are clinically obese")

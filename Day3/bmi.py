print("Welcome to the BMI calculator")
height=float(input("Enter the height in m."))
weight=float(input("Enter the weight in kg"))
bmi=weight/height**2
if bmi<18.5:
    print("Under weight")
elif bmi<25:
    print("Normal weight")
elif bmi<30:
    print("over weight")
elif bmi<35:
    print("obese")
else:
    print("clinically obese")
print("Welcome to the roller coaster ")
height=int(input("Enter your height in cms."))
if height>120:
    print("You are eligible.")
    age=int(input("Enter your age?"))
    if age >= 18:
        print("Give me 25")
        print("Have a thrilling journey")
    else:
        print("Give me 15")
        print("Have a thrilling journey")
else:
    print("Height should be equal to 18 and above")
# name=input("What is your name?")
# l=len(name)
# print("your name has" + l + " characters")

# EnvironmentErrorWhat is your name?Nithish
# Traceback (most recent call last):
#   File "practice1.py", line 3, in <module>
#     print("your name has" + l + " characters")
# TypeError: must be str, not int
# ---------------------------------------------------------

name=input("What is your name?")
l=str(len(name))
print("your name has " + l + " characters")


# correct output
# What is your name?Nithish
# your name has 7 characters
# PS D:\M.Tech\100_days_of_python\100-days-of-python\day2>
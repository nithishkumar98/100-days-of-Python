print("Welcome to the Pizza ordering System")
size=input("Enter the size of the pizza you want? S,M or L")
add_pepperoni=input("Do you want pepperoni? Y or N")
extra_cheese=input("Do you want extra cheese? Y or N")
sp=15
mp=20
lp=25
total=0
if size=="S":
    if add_pepperoni=="Y":
        total=sp+2
    else:
        total=sp
    if extra_cheese=="Y":
        total=total+1
    else:
        total=total

elif size=="M":
    if add_pepperoni=="Y":
        total=mp+3
    else:
        total=mp
    if extra_cheese=="Y":
        total=total+1
    else:
        total=total
elif size=="L":
    if add_pepperoni=="Y":
        total=lp+3
    else:
        total=lp
    if extra_cheese=="Y":
        total=total+1
    else:
        total=total

print(f"your bill amount is {total}")
            
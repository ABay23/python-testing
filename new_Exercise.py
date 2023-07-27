# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

year = 2400
# Write your code below this line 👇
print(year % 4)
print(year % 100)
print(year % 400)
print(year / 4)
print(year / 100)
print(year / 400)


# if year % 4 == 0 and year % 100 == 0 :
#     print("Leap year.")
# elif year % 100 != 0 and year % 400 == 0 :
#     print("Leap year.")
# else:
#     print("Not leap year.")

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
pie = 0
if size == "S":
    pie = 15
elif size == "M":
    pie = 20
else:
    pie = 25

if add_pepperoni == "Y":
    if size == "S":
        pie += 2
    else:
        pie += 3

if extra_cheese == "Y":
    pie += 1

print(f"Your final bill is: ${pie}.")

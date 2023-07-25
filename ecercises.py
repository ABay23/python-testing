
# # Division
# def reg_division(n, x):
#     res = n / x
#     print(res)


# reg_division(10, 5)

# # Floor division


# def floor_division(n, x):
#     res = n // x
#     print(res)


# # floor_division(15, 2)
# print(len(input("What is your name?")))

# namex = input("What is your name?")

# print(namex)


# # 1. Create a greeting for your program.
# print("Hi Welcome to the BNG")

# # 2. Ask the user for the city that they grew up in.
# city = input("Enter the name of the city you gre up in:\n")

# # 3. Ask the user for the name of a pet.
# pet = input("Enter the name of tyour pet:\n")


# # 4. Combine the name of their city and pet and show them their band name.
# print("Your Band Name is " + city + " " + pet)

# 5. Make sure the input cursor shows on a new line:

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

remaining = 90 - int(age)
print(remaining)

# * Tip Calculator Project
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print(("Welcome to the tip calculator.\n"))
total_bill = input("What was the total bill? $")
tip = input("What percentage ti would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

calc_tip = (int(total_bill) + (int(total_bill) * (int(tip)/100)))
result = (calc_tip / int(people))
print('{:.2f}'.format(result))

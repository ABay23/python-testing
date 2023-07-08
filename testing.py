# print("Hello World")
# a = 33
# print(f"This is the number I was looking for {40}, but this is not the number:{50} and we can add variables too: {a}")

# print('Hello My friends')

# def caraota_blanca():
#   print('Hey this is working!')
  
  
# caraota_blanca()

# x = 23
# y = 'John'

# print("%s is %d years Old" %(y, x))

# astring = "Hello world!"
# print(astring[3:7])
# print(astring[3:7:6])

# print(type(astring))

hours_of_the_day = 24
name_of_unit = "hours"
days_input = 0

def days_to_hours():
  try:
    days_as_number = int(days_input)
    if days_as_number > 0:
      total_hours = days_as_number * hours_of_the_day
      print (f"Your {days_as_number} days are going to be a total of: {total_hours} {name_of_unit}")
    elif days_as_number <= 0:
      print ("You need to enter a positive number greater than 0")
    else:
      print ("Please enter a number")
  except:
    print("Your input is not a valid Number")  

while days_input != "exit":
  user_input = input("Select the amount of days you want to calculate!\n")
  for days_input in user_input.split(","):
    print(days_input)
    days_to_hours()
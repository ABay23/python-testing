# class Robot:
#   # Use a constructor
#   def __init__(self, name, color, weight):
#     self.name = name
#     self.color = color
#     self.weight = weight
  
#   def introduce_self(self):
#     print("My name is " + self.name) # This is Java

# r1 = Robot()
# r1.name = "Ale"
# r1.color = "Blue"
# r1.weight = 30

# r2 = Robot()
# r2.name = "John"
# r2.color = "Red"
# r2.weight = 45

# r1 = Robot("Ale", "Blue", 44)
# r2 = Robot("Lou", "Red", 30)

# print(type(r1))

# r1.introduce_self()
# r2.introduce_self()

class Client:
  increment_amount = 1.05
  def __init__(self, name, last_name, email, open_account):
    self.name = name
    self.last_name = last_name
    self.email = email
    self.open_account = open_account
    
  def customer_info(self):
    print(f'Wellcome {self.name} {self.last_name} your accound was open with ${self.open_account}')
  
  def increase_amount(self):
    o_acc = int(self.open_account)
    new_amount =int(o_acc * self.increment_amount)
    print(f"Your New total is: ${new_amount}")
    
  # @classmethod
  # def from_string(cls, client_str):
  #   name, last_name, email, open_account = client_str.split("-")
  #   return cls(name, last_name, email, open_account)


# Inheritance from Client Class
class Developer(Client):
  increment_amount = 10
  
  def __init__(self, name, last_name, email, open_account, prog_lang):
    super().__init__(name, last_name, email, open_account)
    self.prog_lang = prog_lang

# client_str_1 = 'Alejandro-Bay-abay@gmail.com-76000'
# client_str_2 = 'Pedro-Taing-ptaing@gmail.com-50000'

# dev_str_1 = 'Alejandro-Bay-abay@gmail.com-76000'
# dev_str_2 = 'Pedro-Taing-ptaing@gmail.com-50000'

dev_str_1 = 'Alex', 'Bay', 'abay@gmail.com', 76000, 'Javascript'

# # name, last_name, email, open_account = client_str_1.split("-")
# Client_1 = Client.from_string(client_str_2)

# name, last_name, email, open_account = client_str_1.split("-")
# Dev_1 = Developer.from_string(dev_str_1)

# Client_1 = Client(new_emp_1)

# Client_1.customer_info()
# Client_1.increase_amount()
# Dev_1.customer_info()
# Dev_1.increase_amount()

dev_1 = Developer('Alex', 'Bay', 'abay@gmail.com', 76000, 'Javascript')

print(dev_1.customer_info())
print(dev_1.prog_lang)

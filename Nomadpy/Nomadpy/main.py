'''
# hello world
print("Hello world!")
'''

'''
# Variables
a = 2
b = 3
c = a + b
c = 1
print(c)
my_age = 88
'''

'''
# Booleans and Strings
my_name = "kido"
age = 12
dead = False
print("Hello my name is", my_name)
print("and I'm ", age, " years old")
'''

'''
# Functions
# Indentation
# Parameters
# Multiple Parameters
def say_hello(user_name, user_age):
  print("hello", user_name, "how are you?")
  print("you are", user_age, "years old")

say_hello("nico", 12)
say_hello("lynn", 13)
say_hello("lewis", 12)
say_hello("ralph", 15)

def say_bye():
  print("bye bye")

say_bye()
'''

'''
def tax_calculator(money):
    print(money * 0.35)

tax_calculator(1500000000000)
tax_calculator(150)
'''

'''
# Default Parameters
def say_hello2(user_name = "anonymous"):
  print("Hello", user_name)

say_hello2("nico")
say_hello2()
'''

# Return Values
def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

to_pay = tax_calc(150000000)
pay_tax(to_pay)
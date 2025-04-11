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
'''
# Return Values
def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

to_pay = tax_calc(150000000)
pay_tax(to_pay)
'''
'''
# If
a = 10

if a == 10:
  print("True!")
'''
'''
# Else & Elif
password_correct = True

if password_correct:
  print("Here is your money")
else:
  print("Wrong password")


winner = 10

if winner > 10:
  print("winner is greater than 10")
elif winner < 10:
  print("winner is less than 10")
else:
  print("winner is 10")
'''
'''
winner = 50

if winner != 10:
  print("If")
elif winner <= 25:
  print("Elif")
elif winner == 0:
  print("elif 2")
elif winner == 50:
  print("elif 3")
else:
  print("Else")
'''
'''
# And & Or
age = int(input("how old are you?")
         )
if age < 18:
  print("you can't drink")
elif age >= 18 and age <= 35:
  print("you drink beer!")
elif age == 60 or age == 70:
  print("Birthday party!")
else:
  print("Go ahead")
'''
'''
# Python Standard Library
from random import randint

user_choice = int(input("Choose number:"))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
  print("You won!")
elif user_choice > pc_choice:
  print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
  print("Higher! Computer chose", pc_choice)
'''

'''
# while
distance = 0

while distance < 20:
  print("I'm running:", distance, "km")
  distance = distance + 1
'''

'''
# Methods
name = "nico"

print(name.endswith("o"))
'''

'''
# Lists
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print(days_of_week[2])
'''

'''
# Tuples
days = ("Mon", "Tue", "Wed")

print(days[0])
'''

'''
# Dicts
player = {
  "Name": "nico",
  "Age": 12,
  "Alive": True,
  "fav_food": ["🍕", "🍔"]
}
player["fav_food"].append("🍜")
print(player.get("fav_food"))
print(player["fav_food"])
'''

'''
numbers = [5,3,1,5,7,3,"True",True, 12]

numbers.append(["🍕", "🍔"])
print(numbers[-1])

player = {
  "Name": "nico",
  "Age": 12,
  "Alive": True,
  "fav_food": ("🍕", "🍔"),
  "friend": {
    "name": "lynn",
    "fav_food": ["🍎"]
  }
}

print(player["friend"]["fav_food"])

player["fav_food"] = "🍎"
player.pop("Alive")
player['friend']['fav_food'].append('🍌')

print(player)
'''

'''
# For Loops
# URL Formatting
websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  print(website)
'''

'''
# Requests
# Status Codes
from requests import get

websites = (
  "google.com",
  "airbnb.com",
  "facebook.com"
)

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "OK"
  else:
    results[website] = "FAILED"

print(results)
'''

'''
# Why We Need OOP
def create_player_for_team(name, xp, team):
  pass

def create_player(name, xp, team):
  return {
    "name": name,
    "XP": xp,
    "team": team,
  }
  
def introduct_player(player):
  name = player["name"]
  team = player["team"]
  print(f"Hello! My name is {name} and I play for {team}")
  
nico = create_player("Nico", 1500, "Team X")
'''

'''
# Classes
class Puppy:
  def __init__(self):
    self.name = "Ruffus"
    self.age = 0.1
    self.breed = "Beagle"
    
ruffus = Puppy()
bibi = Puppy()
  
print(ruffus.name,
      ruffus.age,
      ruffus.breed
      )
'''

'''
# Methods
class Puppy:
  def __init__(self, name, breed):
    self.name = name
    self.age = 0.1
    self.breed = breed
  
  def __str__(self):
    return f"{self.breed} Puppy named {self.name}"
  
ruffus = Puppy(
  name = "Ruffus", 
  breed = "Beagle",
  )
bibi = Puppy(
  name = "Bibi", 
  breed = "Dalmatian"
  )

print(
  bibi,
  ruffus,
)
'''

'''
# Inheritance
class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
    
  def sleep(self):
    print("zzzzzz......")
    
class GuardDog(Dog):
  def __init__(self, name, breed):
    super().__init__(
      name, 
      breed, 
      5,
    )
    self.aggresive = True
    
  def rrrrrr(self):
    print("stay away!")
    
class Puppy(Dog):
  def __init__(self, name, breed):
    super().__init__(
      name, 
      breed, 
      0.1,
    )
    self.spoiled = True
    
  def woof_woof(self):
    print("Woof Woof!")
    
ruffus = Puppy(
  name = "Ruffus", 
  breed = "Beagle",
  )
bibi = GuardDog(
  name = "Bibi", 
  breed = "Dalmatian"
  )

ruffus.sleep()
bibi.rrrrrr()
'''

# Code Challenge
class Player:
  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team
    
  def introduce(self):
    print(f"Hello! I'm {self.name} and I play for {self.team}")
    
class Team:
  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []
  
  def show_players(self):
    for player in self.players:
      player.introduce()
      
  def add_player(self, name):
    new_player = Player(name, self.team_name)
    self.players.append(new_player)
    
  def remove_player(self, name):
    for player in self.players:
      if player.name == name:
        self.players.remove(player)
        print(f"{name}님이 {self.team_name}에서 제외되었습니다.")
        return
    print(f"{name}님은 {self.team_name}에 속해있지 않습니다.")

  def show_team_xp(self):
    total_xp = sum(player.xp for player in self.players)
    print(f"{self.team_name}은 총 {total_xp}포인트가 있어요.")

team_x = Team("Team X")
team_x.add_player('hanail')

team_blue = Team("Team Blue")
team_blue.add_player('hanami')

team_x.show_players()
team_blue.show_players()

team_x.show_team_xp()
team_x.remove_player('hanail')
team_x.remove_player('hanail')
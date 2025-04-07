#주스 메이커
def make_juice(fruit):
  return f"{fruit}+🥤"

def add_ice(juice):
  return f"{juice}+🧊"

def add_sugar(iced_juice):
  return f"{iced_juice}+🍬"

juice = make_juice("🍎")
print(juice)
cold_juice = add_ice(juice)
print(cold_juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)
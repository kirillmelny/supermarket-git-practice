# 1. Клас Товар (3 властивості, 2 методи)
class Product:
  def __init__(self, name, price, category):
    self.name = name
    self.price = price
    self.category = category
  def show(self):
    print(self.name, self.price)
  def discount(self, amount):
    self.price -= amount
# 2. Клас Знижка (2 властивості, 2 методи)
class Discount:
  def __init__(self, code, percent):
    self.code = code
    self.percent = percent
  def check(self, user_code):
    if self.code == user_code:
      return True
      return False
  def get_factor(self):
    return 1 - (self.percent / 100)
    

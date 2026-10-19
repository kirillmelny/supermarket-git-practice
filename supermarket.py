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
    
#Зміни від : Івасюнько Нікіта
# 3. Клас Покупець (4 властивості, 3 методи)
class Customer:
    def init(self, name, money, city, street):
        self.name = name
        self.money = money
        self.address = (city, street)  # TUPLE (Структура даних 1)
        self.cart = []                 # LIST (Структура даних 2)

    def add(self, product):
        self.cart.append(product)

    def get_sum(self):
        total = 0
        for product in self.cart:       # FOR
            total += product.price
        return total

    def pay(self, cost):
        if self.money >= cost:          # IF
            self.money -= cost
            return True
        return False


# 4. Клас Замовлення / Чек (4 властивості, 2 методи)
class Order:
    def init(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.status = "Нове"
        self.items = {}                # DICT (Структура даних 3)

    def process(self):
        total = self.customer.get_sum()
        for item in self.customer.cart: # FOR
            self.items[item.name] = item.price
            
        # Правило знижки для великого чека (feature/discount)
        if total > 2000:
            total *= 0.95  # додаткові 5% знижки за великий чек
            print("[АКЦІЯ] Застосовано знижку 5% за великий чек!")

        self.status = "Оплачено"
        return total

    def print_check(self, price):
        print("Замовлення №", self.order_id)
        print("Адреса доставки:", self.customer.address)
        print("Придбані товари:", self.items)
        print("До сплати (з урахуванням знижок):", price)

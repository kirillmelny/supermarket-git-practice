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
    def __init__(self, name, money, city, street):
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
    def __init__(self, order_id, customer):
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
# Зміни від: Олександра Дужака
# 5. Клас Супермаркет / Магазин (3 властивості, 2 методи)
class Supermarket:
    def init(self, name):
        self.name = name
        self.goods = []
        self.cats = set()              # SET (Структура даних 4)

    def add_goods(self, product):
        self.goods.append(product)
        self.cats.add(product.category)

    def show_all(self):
        print("Супермаркет:", self.name)
        print("Унікальні категорії товарів (Set):", self.cats)


# 6. Клас Симуляція (3 властивості, 2 методи)
class Simulation:
    def init(self):
        self.market = Supermarket("АТБ / Сільпо")
        self.user = Customer("Кіріл", 10000, "Вінниця", "Соборна")
        self.promo = Discount("SUPER2026", 10)

    def simulate(self):                 # Головний метод simulate()
        print("=== ПОЧАТОК СИМУЛЯЦІЇ СУПЕРМАРКЕТУ ===")
        p1 = Product("Молоко", 150, "Молочні продукти")
        p2 = Product("М'ясо", 1800, "М'ясні вироби")
        p3 = Product("Хліб", 40, "Випічка")

        self.market.add_goods(p1)
        self.market.add_goods(p2)
        self.market.add_goods(p3)
        self.market.show_all()

        # Покупець набирає кошик
        self.user.add(p1)
        self.user.add(p2)
        self.user.add(p3)

        order = Order(1, self.user)
        cost = order.process()

        # Промокод
        if self.promo.check("SUPER2026"):    # IF
            cost *= self.promo.get_factor()

        # Оплата
        if self.user.pay(cost):              # IF
            order.print_check(cost)
            print("Успіх! Залишок коштів у покупця:", self.user.money)
        else:
            print("Помилка: недостатньо коштів!")


# Запуск програми
if name == "main":
    sim = Simulation()
    sim.simulate()

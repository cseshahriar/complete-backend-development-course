""" OOP """
import csv


class Item:

    # class attributes
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=1):
        """ constructor or magic method """
        # Instance Attributes with Encapsulation
        self._name = name  # protected
        self.__price = price  # private
        self.quantity = quantity # public

        # action
        Item.all.append(self)

    # instance methods
    def calculate_total_price(self): # instance method received instance reference  # noqa
        return self.__price * self.quantity

    def apply_discount(self):
        print(self.__price)
        self.__price = self.__price * self.pay_rate
        print(self.__price)
        return self.__price

    @classmethod
    def instantiate_from_csv(cls):  # class method received class references
        with open('data.csv', 'r') as data_file:
            reader = csv.DictReader(data_file)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @property
    def get_name(self):
        return self._name

    def get_price(self):
        return self.__price




# object
obj = Item("Phone", 100.0)
print(obj._name, obj.quantity, type(obj))
print(f"total {obj.calculate_total_price()}")
print("discount", obj.apply_discount())

obj2 = Item('Samsung', 200.0, 2)
print(f"total {obj2.calculate_total_price()}")

print(Item.pay_rate)
print(obj.pay_rate)

Item.instantiate_from_csv()
print(Item.all)

print(obj.is_integer(5.01))
print(Item.is_integer(5.0))

print(obj.get_name)
print(obj.get_price())



#  inheritance
class Parent:
    def __init__(self, name):
        self.name = name


class Child(Parent):
    pass


obj3 = Child("Sirajul Haque")
print(obj3.name)


# polymorphisom

class Phone(Item):
    def __init__(self, name: str, price:float, quantity=1, broken_phone=0):
        super().__init__(name, price, quantity)
        self.broken_phone = broken_phone


class Keyboard(Item):
    def __init__(self, name: str, price:float, quantity=1, broken_keyboard=0):
        super().__init__(name, price, quantity)
        self.broken_phone = broken_keyboard


class Mouse(Item):
    def __init__(self, name: str, price:float, quantity=1, broken_mouse=0):
        super().__init__(name, price, quantity)
        self.broken_mouse = broken_mouse
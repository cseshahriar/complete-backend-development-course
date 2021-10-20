""" class """


class MyClass:
    x = 5  # class attr


obj = MyClass()
print(obj.x)


class Person:

    def __init__(self, param_name: str, param_age: int):  # constructor
        self.name = param_name  # instance attribute
        self.age = param_age  # instance attribute

    def get_name(self):
        print(f"Your name is {self.name}")

    def set_name(self, name: str):
        self.name = name


person_obj = Person('Shahriar', 25)  # object

print(person_obj.name)
person_obj.get_name()

person_obj.set_name('Salpin')
person_obj.get_name()
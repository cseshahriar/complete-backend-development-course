""" Inheritance """


class Person:

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name # protected
        self.__last_name = last_name  # private

    def print_name(self): # protected
        print(f"Your name is {self.first_name} {self.last_name}")

    def _print_name1(self): # protected
        print(f"Your name is {self.first_name} {self.last_name}")

    def __print_name1(self):  # private
        print(f"Your name is {self.first_name} {self.last_name}")


person = Person("Shahriar", "Hosen")
print(person._first_name)



class Student(Person): # Student child class and Person parent class

    def _print_name(self):  # protected
        print(f"Your name is {self.first_name} {self.last_name}")


student = Student("Salpin", "Murol")
print(student._first_name)

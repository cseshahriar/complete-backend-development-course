""" Abstract Class """
from abc import ABC, abstractmethod

import setuptools.wheel


class Employee(ABC):

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, salary: float):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, worked_hours: int, rate: float):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate


class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for employee in self.employee_list:
            print(f"{employee.full_name} \t {employee.get_salary()}")



payroll = Payroll()
payroll.add(FullTimeEmployee('Shahriar', 'Hosen', 40000))
payroll.add(FullTimeEmployee('Salpin', 'Murol', 40000))
payroll.add(HourlyEmployee('Salpin', 'Alam', 100, 150))

payroll.print()

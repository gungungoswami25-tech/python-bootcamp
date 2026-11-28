
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def pay(self):
        return self._salary

    def __str__(self):
        return f"{self.name} - Pay: {self.pay()}"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def pay(self):
        return super().pay() + self.bonus


class Intern(Employee):
    def __init__(self, name, hours):
        super().__init__(name, 0)
        self.hours = hours

    def pay(self):
        return self.hours * 200


class Company:
    def __init__(self):
        self.people = []

    def add(self, person):
        self.people.append(person)

    def show_all(self):
        for person in self.people:
            print(person.name, "-", person.pay())

    def total_payroll(self):
        total = 0

        for person in self.people:
            total = total + person.pay()

        return total


company = Company()

asha = Employee("Asha", 30000)
rohit = Manager("Rohit", 50000, 8000)
kabir = Intern("Kabir", 80)

company.add(asha)
company.add(rohit)
company.add(kabir)

print("Employee List:")

for person in company.people:
    print(person)

print("\nTotal Payroll:", company.total_payroll())

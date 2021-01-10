import abc
from typing import Dict, List

# 1 - Konto

class Konto:

    def __init__(self, inhaber: str):
        self._inhaber = inhaber
        self._kontostand = 0

    @property
    def kontostand(self):
        return self._kontostand

    def __repr__(self):
        return f'Kontoinhaber: {self._inhaber}, Kontostand: {self._kontostand}'

    def einzahlen(self, wert: float) -> float:
        if wert > 0:
            self._kontostand += wert

    def auszahlen(self, wert: float) -> float:
        if wert > 0:
            self._kontostand -= wert
        return wert

class GiroKonto(Konto):

    def __init__(self, inhaber: str, limit: float):
        super().__init__(inhaber)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def auszahlen(self, wert: float) -> float:
        if wert > self._kontostand + self._limit:
            w = self._kontostand + self._limit
            self._kontostand -= self._limit
            return w
        return super().auszahlen(wert)

class JugendGiroKonto(GiroKonto):

    def __init__(self, inhaber: str, limit: float, buchungslimit: float):
        super().__init__(inhaber, limit)
        self._buchungslimit = buchungslimit

    @property
    def buchungslimit(self):
        return self._buchungslimit

    def auszahlen(self, wert: float) -> float:
        if wert > self._buchungslimit:
            return super().auszahlen(self._buchungslimit)
        return super().auszahlen(wert)


class SparKonto(Konto):

    def __init__(self, inhaber: str):
        super().__init__(inhaber)

#    def auszahlen(self, wert: float) -> float:
#        if wert > 0:
#            w = self._kontostand - wert
#            if w > 0:
#                self._kontostand -= wert
#        return wert

    def auszahlen(self, wert: float) -> float:
        if wert < 0:
            return 0
        if wert > self.kontostand:
            w = self.kontostand
            self._kontostand = 0
            return w
        self._kontostand -= wert
        return wert

# 2 - MitarbeiterInnen

class Employee:

    def __init__(self, lastname: str, firstname: str, department: str, base_salary: float):
        self._lastname = lastname
        self._firstname = firstname
        self._department = department
        self._base_salary = base_salary

    def __repr__(self):
        return f'{self._lastname} {self._firstname}, {self._department}'

    def get_full_salary(self) -> float:
        return self._base_salary

class FixCommissionEmployee(Employee):

    def __init__(self, lastname: str, firstname: str, department: str, base_salary: float, additional_commission: float):
        super().__init__(lastname, firstname, department, base_salary)
        self._additional_commission = additional_commission

    def get_full_salary(self) -> float:
        return self._base_salary + self._additional_commission

class PercentCommissionEmployee(Employee):

    def __init__(self, lastname: str, firstname: str, department: str, base_salary: float, percent_commission: float):
        super().__init__(lastname, firstname, department, base_salary)
        self._percent_commission = percent_commission

    def get_full_salary(self) -> float:
        return self._base_salary + (self._base_salary / 100 * self._percent_commission)

class EmployeeManager:

    def __init__(self):
        self.__emp_list = []

    def __repr__(self):
        return f'{self.__emp_list}'

    def add_employee(self, emp: Employee):
        return self.__emp_list.append(emp)

    def calc_total_salary(self) -> float:
        total = 0
        for emp in self.__emp_list:
            total += emp.get_full_salary()
        return total

    def get_salary_by_department(self) -> Dict[str, float]:
        dep = {}
        for e in self.__emp_list:
            dep[e._department] = dep.get(e._department, 0) + e.get_full_salary()
        return dep

if __name__ == '__main__':

    a = Konto("Anton")
    b = GiroKonto("Berta", 500)
    c = JugendGiroKonto("Chris", 300, 150)
    d = SparKonto("Doris")

    a.einzahlen(500)
    b.einzahlen(200)
    c.einzahlen(150)
    d.einzahlen(100)

    b.auszahlen(200)
    b.auszahlen(600)
    c.auszahlen(160)
    d.auszahlen(110)

    print(d)
    print(b)
    print(c)

    e = Employee("Ertl", "Emil", "F", 2000)
    f = FixCommissionEmployee("Fux", "Fred", "F", 2000, 200)
    g = PercentCommissionEmployee("Gang", "Greg", "G", 2000, 10)
    mg = EmployeeManager()

    print(f.get_full_salary())
    print(g.get_full_salary())
    mg.add_employee(e)
    mg.add_employee(f)
    mg.add_employee(g)

    print(mg.calc_total_salary())
    print(mg.get_salary_by_department())
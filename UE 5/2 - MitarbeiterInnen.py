from typing import Dict, List

class Employee:

    def __init__(self, lastname: str, firstname: str, department: str, base_salary: float):
        self._lastname = lastname
        self._firstname = firstname
        self._department = department
        self._base_salary = base_salary

    def get_full_salary(self) -> float:
        return f'Gehalt {self._lastname}: {self._base_salary} EUR'

class FixCommissionEmployee(Employee):

    def __init__(self, lastname: str, firstname: str, department: str, base_salary: float, additional_commission: float):
        super(FixCommissionEmployee, self).__init__(lastname, firstname, department, base_salary)
        self._additional_commision = additional_commission

    def get_full_salary(self) -> float:
        g = self._base_salary + self._additional_commision
        return f'Gehalt {self._lastname}: {g} EUR'

class PercentCommissionEmployee(Employee):

    def __init__(self, lastname: str, firstname: str, department: str, base_salary: float, percent_commision: float):
        super(PercentCommissionEmployee, self).__init__(lastname, firstname, department, base_salary)
        self._percent_commission = percent_commision

    def get_full_salary(self) -> float:
        g = self._base_salary * (self._percent_commission / 100)
        h = self._base_salary + g
        return f'Gehalt {self._lastname}: {h} EUR'

class EmployeeManager:

    def __init__(self):
        self.__emp_list = []

    def add_employee(self, emp: Employee):
        self.__emp_list.append(emp)

    def calc_total_salary(self) -> float:
        total = 0
        for emp in self.__emp_list:
            total += emp.get_full_salary()
        return total

    def get_salary_by_department(self) -> Dict[str, float]:
        d = {}

        for e in self.__emp_list:
            d[e._department] = d.get(e._department, 0) + e.get_full_salary()

        return d


if __name__ == '__main__':

    a = Employee("Anders", "Andi", "C", 1900)
    print(a.get_full_salary())
    b = FixCommissionEmployee("Baer", "Bernd", "B", 1900, 500)
    print(b.get_full_salary())
    c = PercentCommissionEmployee("Casd", "Chris", "C", 1900, 10)
    print(c.get_full_salary())
    mg = EmployeeManager()
    mg.add_employee(Employee("Anders", "Andi", "C", 1900))
    mg.add_employee(FixCommissionEmployee("Baer", "Bernd", "B", 1900, 500))
    mg.add_employee(PercentCommissionEmployee("Casd", "Chris", "C", 1900, 10))
    #print(mg.calc_total_salary())
    print(mg.get_salary_by_department())
"""Podana jest implementacja klasy abstrakcyjnej TaxPayer. Utwórz klasę pochodną klasy TaxPayer o nazwie WorkerTaxPayer, która implementuje metodę calculate_tax() obliczającą wartość podatku według reguły:

do kwoty 80000 -> podatek w wysokości 17%

wszystko powyżej kwoty 80000 -> podatek w wysokości 32%



Następnie utwórz dwie instancję klasy WorkerTaxPayer o nazwach worker1 oraz worker2 i odpowiednio pensji 70000 oraz 95000. W odpowiedzi wywołując metodę calculate_tax() wydrukuj do konsoli wartość obliczonego podatku dla obu tych instancji.



Oczekiwany wynik:



11900.0
18400.0"""

from abc import ABC, abstractmethod


class TaxPayer(ABC):
    def __init__(self, salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax(self):
        pass


class StudentTaxPayer(TaxPayer):
    def calculate_tax(self):
        return self.salary * 0.15


class DisabledTaxPayer(TaxPayer):
    def calculate_tax(self):
        return self.salary * 0.12


class WorkerTaxPayer(TaxPayer):
    def calculate_tax(self):
        if self.salary < 80000:
            return self.salary * 0.17
        else:
            return 80000 * 0.17 + (self.salary - 80000) * 0.32


worker1 = WorkerTaxPayer(70000)
worker2 = WorkerTaxPayer(95000)
print(worker1.calculate_tax())
print(worker2.calculate_tax())

"""Podana jest implementacja klasy abstrakcyjnej TaxPayer. Utwórz klasę pochodną klasy TaxPayer o nazwie DisabledTaxPayer, która implementuje metodę calculate_tax() obliczającą wartość minimalną z podanych dwóch:

12% podatku od wynagrodzenia (atrybut salary)

5000.0



Następnie utwórz instancję klasy DisabledTaxPayer o nazwie disabled i pensji 50000. W odpowiedzi wywołując metodę calculate_tax() wydrukuj do konsoli wartość obliczonego podatku.



Oczekiwany wynik:



5000.0"""

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
        return min(self.salary * 0.12, 5000.0)


disabled = DisabledTaxPayer(50000)
print(disabled.calculate_tax())

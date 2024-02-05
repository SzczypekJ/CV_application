"""Podana jest implementacja klasy abstrakcyjnej TaxPayer. Utwórz klasę pochodną klasy TaxPayer o nazwie StudentTaxPayer, która implementuje metodę calculate_tax() obliczającą wartość 15%-ego podatku od wynagrodzenia (atrybut salary).



Następnie utwórz instancję klasy StudentTaxPayer o nazwie student i pensji 40000. W odpowiedzi wywołując metodę calculate_tax() wydrukuj do konsoli wartość obliczonego podatku.



Oczekiwany wynik:



6000.0"""

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


student = StudentTaxPayer(40000)
print(student.calculate_tax())

"""Podana jest implementacja klasy abstrakcyjnej TaxPayer oraz klas pochodnych:

StudentTaxPayer

DisabledTaxPayer

WorkerTaxPayer



Utwórz listę o nazwie tax_payers i przypisz do niej cztery obiekty odpowiednio:

klasy StudentTaxPayer z pensją 50000

klasy DisabledTaxPayer z pensją 70000

klasy WorkerTaxPayer z pensją 68000

klasy WorkerTaxPayer z pensją 120000



Następnie iterując po liście wywołaj metodę calculate_tax() na obiektach listy i wydrukuj do konsoli wysokość wymaganego podatku.



Oczekiwany wynik:



7500.0
8400.0
11560.0
26400.0"""

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


tax_payers = [StudentTaxPayer(50000), DisabledTaxPayer(
    70000), WorkerTaxPayer(68000), WorkerTaxPayer(120000)]

for i in tax_payers:
    print(i.calculate_tax())

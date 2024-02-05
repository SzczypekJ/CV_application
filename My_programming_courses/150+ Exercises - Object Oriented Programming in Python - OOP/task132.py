"""Zdefiniuj klasę abstrakcyjną o nazwie TaxPayer. W metodzie __init__() przekaż możliwość ustawienia atrybutu instancji (bez walidacji) o nazwie salary (pensja). Następnie zaimplementuj metodę abstrakcyjną o nazwie calculate_tax() (wykorzystaj dekorator @abstractmethod)."""

from abc import ABC, abstractmethod


class TaxPayer(ABC):
    def __init__(self, salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax(self):
        pass

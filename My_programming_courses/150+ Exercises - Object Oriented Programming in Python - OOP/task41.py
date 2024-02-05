"""Zdefiniowana jest klasa o nazwie OnlineShop z atrybutami klasy ustawionymi odpowiednio:

sector na wartość 'electronics'

sector_code na wartość 'ELE'

is_public_company na wartość False



Zaimplementuj funkcję (atrybut wywoływalny klasy) o nazwie get_sector(), która zwróci wartość atrybutu sector klasy OnlineShop. Wystarczy tylko zaimplementować funkcję. Zaimplementowane testy jednostkowe sprawdzają poprawność rozwiązania."""


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False

    def get_sector(self):
        return self.sector


online = OnlineShop()
print(online.get_sector())

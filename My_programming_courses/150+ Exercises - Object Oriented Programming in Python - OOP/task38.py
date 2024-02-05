"""Zdefiniowana jest klasa o nazwie OnlineShop z atrybutami klasy ustawionymi odpowiednio:

sector na wartość 'electronics'

sector_code na wartość 'ELE'

is_public_company na wartość False



Wykorzystując funkcję wbudowaną delattr() usuń atrybut klasy o nazwie sector_code. W odpowiedzi wydrukuj pozostałe nazwy atrybutów klasy OnlineShop zdefiniowane przez użytkownika w formie listy tak jak pokazano poniżej.



Oczekiwany wynik:



['sector', 'is_public_company']"""


from traceback import print_tb


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


delattr(OnlineShop, 'sector_code')
attr = [attr
        for attr in OnlineShop.__dict__.keys()
        if not attr.startswith("_")]

print(attr)

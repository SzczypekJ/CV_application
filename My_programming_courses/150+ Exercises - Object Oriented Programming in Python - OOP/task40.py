"""Zdefiniowana jest klasa o nazwie OnlineShop z atrybutami klasy ustawionymi odpowiednio:

sector na wartość 'electronics'

sector_code na wartość 'ELE'

is_public_company na wartość False



Poza klasą zaimplementuj funkcję o nazwie describe_attrs(), który wyświetli nazwy wszystkich atrybutów klasy zdefiniowanych przez użytkownika wraz z ich wartościami tak jak pokazano poniżej. W odpowiedzi wywołaj funkcję describe_attrs().



Oczekiwany wynik:



sector -> electronics
sector_code -> ELE
is_public_company -> False"""

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False

def describe_attrs():
    for attr, value in OnlineShop.__dict__.items():
        if not attr.startswith('__'):
            print(attr, '->', value)

describe_attrs()
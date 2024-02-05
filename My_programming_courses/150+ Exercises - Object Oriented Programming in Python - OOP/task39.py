"""Zdefiniowana jest klasa o nazwie OnlineShop z atrybutami klasy ustawionymi odpowiednio:

sector na wartość 'electronics'

sector_code na wartość 'ELE'

is_public_company na wartość False



Wyświetl wszystkie zdefiniowane przez użytkownika nazwy atrybutów klasy OnlineShop wraz z ich wartościami tak jak pokazano poniżej.



Oczekiwany wynik:



sector -> electronics
sector_code -> ELE
is_public_company -> False"""


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False

# solution 1
# attr = [attr
#         for attr in OnlineShop.__dict__.values()]


# print(f"sector -> {attr[1]}")
# print(f"sector_code -> {attr[2]}")
# print(f"is_public_company -> {attr[3]}")

# solution 2
for attr, value in OnlineShop.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
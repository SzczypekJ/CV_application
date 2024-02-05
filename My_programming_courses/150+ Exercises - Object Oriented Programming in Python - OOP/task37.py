"""Zdefiniowana jest klasa o nazwie OnlineShop z atrybutami klasy ustawionymi odpowiednio:

sector na wartość 'electronics'

sector_code na wartość 'ELE'

is_public_company na wartość False



Wykorzystując instrukcję del usuń atrybut klasy o nazwie sector_code. W odpowiedzi wydrukuj pozostałe nazwy atrybutów klasy OnlineShop zdefiniowane przez użytkownika w formie listy tak jak pokazano poniżej.



Oczekiwany wynik:



['sector', 'is_public_company']"""


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


# solution 1
del(OnlineShop.sector_code)

lst = []
for i in OnlineShop.__dict__.keys():
    if not i.startswith('_'):
        lst.append(i)

print(lst)

# solution 2
# del OnlineShop.sector_code
# attrs = [
#     attr
#     for attr in OnlineShop.__dict__.keys()
#     if not attr.startswith('_')
# ]
# print(attrs)
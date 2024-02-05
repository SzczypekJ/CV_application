"""Zaimplementuj klasę o nazwie OnlineShop z atrybutami klasy ustawionymi odpowiednio:

sector na wartość 'electronics'

sector_code na wartość 'ELE'

is_public_company na wartość False



Następnie wykorzystując notację kropkową dodaj w locie atrybut klasy o nazwie country i ustaw jego wartość na 'Poland'. W odpowiedzi wydrukuj nazwy atrybutów klasy OnlineShop zdefiniowane przez użytkownika w formie listy tak jak pokazano poniżej.



Oczekiwany wynik:



['sector', 'sector_code', 'is_public_company', 'country']"""


class OnlineShop:
    sector = "electronics"
    sector_code = "ELE"
    is_public_company = False


# solution 1
setattr(OnlineShop, "country", "Poland")

lst = []
for i in OnlineShop.__dict__.keys():
    if not i.startswith('_'):
        lst.append(i)

print(lst)

# solution 2
# OnlineShop.country = 'Poland'
# attrs = [
#     attr
#     for attr in OnlineShop.__dict__.keys()
#     if not attr.startswith('_')
# ]
# print(attrs)

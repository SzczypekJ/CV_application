"""Zaimplementowana jest klasa Client. Utworzono cztery poniższe instancje klasy Client:



client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@gmail.com')
client3 = Client('Mike', 'sales@yahoo.com')
client4 = Client('Lisa', 'info@gmail.com')


Następnie wyszukaj wszystkich klientów posiadających w nazwie adresu mailowego słówko 'sales'. W odpowiedzi wydrukuj imiona znalezionych klientów jako listę.



Oczekiwany wynik:



['Donald', 'Mike']"""


class ClientList(list):
    def search_email(self, value):
        result = [client for client in self if value in client.email]
        return result


class Client:
    all_clients = ClientList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self):
        return f"Client(name='{self.name}', email='{self.email}')"


client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@gmail.com')
client3 = Client('Mike', 'sales@yahoo.com')
client4 = Client('Lisa', 'info@gmail.com')
# sol 1
lst = []
for i in Client.all_clients.search_email("sales"):
    lst.append(i.name)
print(lst)
# sol 2
# result = [
#     client.name
#     for client in Client.all_clients.search_email('sales')
# ]
 
# print(result)
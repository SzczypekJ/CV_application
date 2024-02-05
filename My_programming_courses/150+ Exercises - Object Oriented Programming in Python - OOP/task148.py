"""Zaimplementowana jest klasa Client. Utwórz cztery poniższe instancje klasy Client:



client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@gmail.com')
client3 = Client('Mike', 'sales@yahoo.com')
client4 = Client('Lisa', 'info@gmail.com')


Następnie wyszukaj wszystkich klientów posiadających konto na poczcie gmail. W odpowiedzi wydrukuj znalezionych klientów do konsoli tak jak pokazano poniżej.



Oczekiwany wynik:



Client(name='Tom', email='sample@gmail.com')
Client(name='Donald', email='sales@gmail.com')
Client(name='Lisa', email='info@gmail.com')"""


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

for i in Client.all_clients.search_email("gmail"):
    print(i)

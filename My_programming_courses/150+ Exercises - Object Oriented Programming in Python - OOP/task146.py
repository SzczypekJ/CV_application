"""Zaimplementuj klasę o nazwie Client, która będzie posiadać atrybut klasy o nazwie all_clients (jako lista). Następnie metoda __init__() ustawi dwa poniższe atrybuty instancji (bez walidacji) i doda tę instancję do listy all_clients (atrybut klasy Client):

name

email



Dodaj także metodę __repr__() będącą formalną reprezentacją obiektu klasy Client.



Kolejno utwórz trzech klientów wykonując poniższy kod:



client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@yahoo.com')
client3 = Client('Mike', 'sales-contact@yahoo.com') 


W odpowiedzi wydrukuj atrybut all_clients klasy Client do konsoli.



Oczekiwany wynik:



[Client(name='Tom', email='sample@gmail.com'), Client(name='Donald', email='sales@yahoo.com'), Client(name='Mike', email='sales-contact@yahoo.com')]"""


class Client:
    all_clients = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self):
        return f"Client(name='{self.name}', email='{self.email}')"


client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@yahoo.com')
client3 = Client('Mike', 'sales-contact@yahoo.com')
print(Client.all_clients)

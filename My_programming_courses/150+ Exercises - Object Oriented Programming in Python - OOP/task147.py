"""Zaimplementowana jest klasa Client. Zwróć uwagę na atrybut klasy all_clients. Atrybut jest specjalną listą. Spróbuj zaimplementować specjalną klasę rozszerzającą klasę wbudowaną list o nazwie ClientList, która oprócz standardowych metod dla klasy wbudowanej list posiadać będzie metodę search_email() pozwalającą zwrócić listę instancji klasy Client zawierających szukany tekst w adresie email.



Przykładowo, poniższy kod:



client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@gmail.com')
client3 = Client('Mike', 'sales@yahoo.com')
client4 = Client('Lisa', 'info@gmail.com')
print(Client.all_clients.search_email('sales'))


zwróci:



[Client(name='Donald', email='sales@gmail.com'), Client(name='Mike', email='sales@yahoo.com')]


W odpowiedzi dokończ implementację metody search_email() i wywołaj podany kod."""


class ClientList(list):
    def search_email(self, value):
        result = [
            client 
            for client in self 
            if value in client.email]
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
print(Client.all_clients.search_email('sales'))

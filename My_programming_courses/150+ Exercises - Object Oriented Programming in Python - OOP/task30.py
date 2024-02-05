"""Zdefiniuj klasę o nazwie Container, która nie posiada żadnych atrybutów ani metod. Następnie utwórz instancję tej klasy o nazwie container. W odpowiedzi wyświetl do konsoli typ atrybutu słownikowego __dict__ dla klasy Container oraz dla instancji container.



Oczekiwany wynik:



<class 'mappingproxy'>
<class 'dict'>"""


class Container:
    pass


container = Container()

print(type(Container.__dict__))
print(type(container.__dict__))

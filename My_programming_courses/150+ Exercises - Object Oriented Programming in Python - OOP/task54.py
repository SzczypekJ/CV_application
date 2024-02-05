"""Zaimplementuj klasę o nazwie Bucket, która przy tworzeniu instancji będzie przyjmować dowolną liczbę nazwanych argumentów (keyword arguments - użyj **kwargs). Nazwa przekazanego argumentu to nazwa atrybutu instancji, zaś wartość dla argumentu to wartość dla atrybutu instancji.



Przykład:



[IN]: bucket = Bucket(apple=3.5)
[IN]: print(bucket.__dict__)


[OUT]: {'apple': 3.5}


Następnie utwórz obiekt klasy Bucket o nazwie bucket dodając poniższe atrybuty wraz z ich wartościami:

apple = 3.5

milk = 2.5

juice = 4.9

water = 2.5



W odpowiedzi wydrukuj wartość atrybutu __dict__ dla obiektu bucket do konsoli.



Oczekiwany wynik:



{'apple': 3.5, 'milk': 2.5, 'juice': 4.9, 'water': 2.5}"""


class Bucket:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)


bucket = Bucket(apple=3.5, milk=2.5, juice=4.9, water=2.5)
print(bucket.__dict__)

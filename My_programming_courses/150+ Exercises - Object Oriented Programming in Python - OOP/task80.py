"""Zadeklaruj klasę o nazwie Circle, która będzie posiadać atrybut instancji radius - promień koła. Ustaw go jako właściwość do odczytu i do modyfikacji (nie dokonuj żadnej walidacji ustawionej wartości). W rozwiązaniu użyj dekoratora @property.



Następnie utwórz instancję klasy o nazwie circle i promieniu 3. W odpowiedzi wyświetl atrybut __dict__ instancji circle do konsoli.



Oczekiwany wynik:



{'_radius': 3}"""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value


circle = Circle(3)
print(circle.__dict__)

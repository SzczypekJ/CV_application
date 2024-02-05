"""Utwórz klasę o nazwie CustomDict rozszerzającą wbudowaną klasę dict. Dodaj metodę o nazwie is_any_str_value() zwracającą wartość logiczną True w przypadku, gdy utworzony słownik zawiera co najmniej jedną wartość w słowniku typu str, przeciwnie False.



Przykład działania I:



[IN]: cd = CustomDict(python='mid')
[IN]: print(cd.is_any_str_value())


[OUT]: True


Przykład działania II:



[IN]: cd = CustomDict(price=119.99)
[IN]: print(cd.is_any_str_value())


[OUT]: False


W ćwiczeniu wystarczy tylko zaimplementować klasę CustomDict. Zaimplementowane testy jednostkowe sprawdzają poprawność rozwiązania.

"""


class CustomDict(dict):
    def is_any_str_value(self):
        for key, value in self.items():
            if isinstance(value, str):
                return True
        return False


cd = CustomDict(python='mid')
print(cd.is_any_str_value())
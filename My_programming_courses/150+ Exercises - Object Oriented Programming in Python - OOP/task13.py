"""Napisz program, który tworzy zmienną x o wartości 10. Następnie zdefiniuj funkcję func1(), która tworzy nową zmienną lokalną y o wartości 5 i zwraca jej wartość. Następnie zdefiniuj nową funkcję func2(), która tworzy nową zmienną lokalną y o wartości 2, wywołuje funkcję func1() i mnoży zwracaną wartość przez zmienną lokalną y. Na koniec wywołaj funkcję func2() i wynik wydrukuj do konsoli.



Twój program demonstruje koncepcję reguły LEGB i możliwość posiadania wielu zmiennych o tej samej nazwie w różnych zakresach.



Oczekiwany wynik:



10"""

x = 10


def func1():
    y = 5
    return y


def func2():
    y = 2
    return y * func1()


print(func2())

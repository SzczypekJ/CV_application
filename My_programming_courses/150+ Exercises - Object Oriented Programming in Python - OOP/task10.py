"""Napisz program, który tworzy zmienną x o wartości 10. Następnie zdefiniuj funkcję func1(), która wyświetla wartość zmiennej x. Kolejno zdefiniuj nową funkcję func2(), która tworzy nową zmienną lokalną x o wartości 5 i wywołuje funkcję func1(). Na koniec wywołaj funkcję func2() i zaobserwuj wynik.



Twój program demonstruje koncepcję reguły LEGB oraz kolejność, w jakiej Python wyszukuje zmienne w różnych zakresach.



Oczekiwany wynik:



10
"""

x = 10


def func1():
    print(x)


def func2():
    x = 5
    func1()


func2()

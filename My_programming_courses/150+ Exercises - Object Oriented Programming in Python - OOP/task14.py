"""Napisz program, który tworzy zmienną x o wartości 10. Następnie zdefiniuj funkcję func1(), która tworzy nową zmienną lokalną x o wartości 5 i zwraca jej wartość. Następnie zdefiniuj nową funkcję func2(), która tworzy nową zmienną lokalną x o wartości 2, wywołuje funkcję func1() i mnoży zwracaną wartość przez zmienną globalną x. Na koniec wywołaj funkcję func2() i wynik wydrukuj do konsoli.



Ten program demonstruje koncepcję reguły LEGB i możliwość dostępu do zmiennych w różnych zakresach.



Oczekiwany wynik:



50"""



x = 10

def func1():
    x = 5
    return x

def func2():
    x = 2
    return func1() *  globals()['x']

print(func2())


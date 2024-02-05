"""Napisz program, który tworzy zmienną x o wartości 10. Następnie zdefiniuj funkcję func1(), która tworzy nową zmienną lokalną x o wartości 5 i wyświetla jej wartość. Następnie zdefiniuj nową funkcję func2(), która wywołuje funkcję func1() i wyświetlającą wartość zmiennej globalnej x. Na koniec wywołaj funkcję func2() i zaobserwuj wynik.



Twój program demonstruje koncepcję reguły LEGB oraz różnicę między zmiennymi lokalnymi i globalnymi.



Oczekiwany wynik:



5
10"""

x = 10


def func1():
    x = 5
    print(x)


def func2():
    func1()
    print(x)


func2()

"""Napisz program, który tworzy zmienną x o wartości 10. Następnie zdefiniuj funkcję func1(), która tworzy nową zmienną lokalną x o wartości 5 i definiuje inną funkcję inner_func() modyfikującą wartość zmiennej x na 7 w otaczającym zakresie używając instrukcji nonlocal. Kolejno wywołaj funkcję inner_func() z wnętrza funkcji func1() i wydrukuj wartość zmiennej x zdefiniowanej wewnątrz funkcji func1().

Następnie zdefiniuj nową funkcję func2(), która wyświetla wartość zmiennej globalnej x. Na koniec wywołaj func1() i func2() i zaobserwuj wynik.



Ten program demonstruje użycie instrukcji nonlocal do modyfikowania zmiennych w otaczającym zakresie z wnętrza funkcji zagnieżdżonej.



Oczekiwany wynik:



7
10"""
x = 10


def func1():
    x = 5

    def inner_func():
        nonlocal x
        x = 7
    inner_func()
    print(x)


def func2():
    print(x)


func1()
func2()

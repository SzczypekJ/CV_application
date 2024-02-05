"""Napisz program, który tworzy zmienną x o wartości 10. Następnie zdefiniuj funkcję func1(), która modyfikuje zmienną globalną x za pomocą instrukcji global i ustawia jej wartość na 5. Następnie zdefiniuj nową funkcję func2(), która drukuje wartość zmiennej globalnej x. Na koniec wywołaj func1() i func2() i zaobserwuj wyniki.



Ten program demonstruje użycie instrukcji global do modyfikowania zmiennych globalnych z wnętrza funkcji.



Oczekiwany wynik:



5"""

x = 10

def func1():
    globals()['x'] = 5

def func2():
    print(x)

func1()
func2()
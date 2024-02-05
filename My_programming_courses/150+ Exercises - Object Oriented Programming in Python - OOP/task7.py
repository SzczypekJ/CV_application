"""Podana jest zmienna globalna o nazwie counter oraz niepoprawnie zaimplementowana funkcja update_counter(), która za zadanie ma aktualiować wartość zmiennej counter. Popraw implementację funkcji update_counter() tak, aby z poziomu tej funkcji mieć możliwość modyfikacji wartości zmiennej globalnej counter. Następnie wywołaj funkcję update_counter().



Oczekiwany wynik:



2"""

counter = 1


def update_counter(counter):
    counter += 1
    print(counter)


update_counter(counter)

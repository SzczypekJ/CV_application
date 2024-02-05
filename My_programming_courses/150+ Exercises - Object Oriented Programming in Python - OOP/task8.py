"""Podane są dwie zmienne globalne o nazwach:

counter

dot_counter



Podana jest także niepoprawnie zaimplementowana funkcja update_counters(), która za zadanie ma aktualizować wartości tych zmiennych globalnych. Popraw implementację funkcji update_counters() tak, aby z poziomu tej funkcji mieć możliwość modyfikacji wartości podanych zmiennych globalnych. Następnie wywołaj funkcję update_counters() 40-krotnie przy pomocy składania list (list comprehension).



W odpowiedzi wydrukuj wartość zmiennych globalnych counter oraz dot_counter tak jak pokazano poniżej.



Oczekiwany wynik:



40
........................................"""

counter = 0
dot_counter = ''


def update_counters():
    global counter, dot_counter
    counter += 1
    dot_counter += '.'
    return counter, dot_counter



[update_counters() for _ in range(40)]
print(counter)
print(dot_counter)
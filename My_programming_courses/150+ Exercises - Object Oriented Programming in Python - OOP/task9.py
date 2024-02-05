"""Podana jest funkcja display_info(), która posiada niepoprawnie zaimplementowaną funkcję wewnętrzną update_counter(). Popraw implementację tej funkcji tak, aby mieć możliwość modyfikacji zmiennych nielokalnych: counter oraz dash_counter z poziomu funkcji wewnętrznej update_counter(). W odpowiedzi wywołaj funkcję display_info() z argumentem number_of_updates ustawionym na 50.



Oczekiwany wynik:



50
--------------------------------------------------"""


def display_info(number_of_updates=1):
    counter = 0
    dash_counter = ''

    def update_counter():
        nonlocal counter, dash_counter
        counter += 1
        dash_counter += '-'

    [update_counter() for _ in range(number_of_updates)]

    print(counter)
    print(dash_counter)


display_info(50)

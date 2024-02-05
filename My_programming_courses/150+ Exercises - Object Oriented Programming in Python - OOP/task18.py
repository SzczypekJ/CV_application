"""Zaimplementuj funkcję o nazwie display_info(), która przyjmuje obowiązkowy argument company i określa on nazwę firmy. Funkcja powinna mieć też możliwość przyjmowania argumentów nazwanych (**kwargs), które będą zawierać informacje o innych danych dotyczących firmy (na przykład cena jej akcji na giełdzie).

Funkcja ma za zadanie drukować do konsoli nazwę firmy oraz, jeśli użytkownik przekaże argument price to wyświetla także cenę w formacie $ {cena} (patrz poniżej).



Przykład wywołania I:



[IN]: display_info(company='Apple')


[OUT]: Company name: Apple


Przykład wywołania II:



[IN]: display_info(company='Apple', price=114)


[OUT]
Company name: Apple
Price: $ 114


W odpowiedzi wywołaj funkcję display_info() tak jak pokazano poniżej:



display_info(company='CD Projekt', price=100)


Oczekiwany wynik:



Company name: CD Projekt
Price: $ 100"""

# solution 1
def display_info(company, **kwargs):
    print("Company name:", company)
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: $ {value}")


display_info(company='CD Projekt', price=100)

# solution 2
# def display_info(company, **kwargs):
#     print(f'Company name: {company}')
#     if 'price' in kwargs:
#         print(f"Price: $ {kwargs['price']}")
 
 
# display_info(company='CD Projekt', price=100)

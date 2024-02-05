"""Wykorzystując klasę classmethod (zrób to w klasyczny sposób) zaimplementuj klasę o nazwie Person, która będzie posiadać metodę klasy o nazwie show_details() wyświetlającą do konsoli tekst:



'Running from Person class.'


Nazwę klasy postaraj się przekazać używając odpowiedniego atrybutu klasy Person, nie podawaj jej w sposób bezpośredni. W odpowiedzi wywołaj metodę klasy show_details().



Oczekiwany wynik:



Running from Person class."""

# solution 1


class Person:
    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')


Person.show_details()

# solution 2
# class Person:
#     def show_details(cls):
#         print(f'Running from {cls.__name__} class.')
        
#     show_details = classmethod(show_details)
 
 
# Person.show_details()

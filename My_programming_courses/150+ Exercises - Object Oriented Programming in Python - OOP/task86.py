"""Zaimplementuj klasę o nazwie Container, która będzie posiadać metodę klasy o nazwie show_details() wyświetlającą do konsoli tekst:



'Running from Container class.'


Wykorzystaj w rozwiązaniu dekorator @classmethod. Nazwę klasy postaraj się przekazać używając odpowiedniego atrybutu klasy Container, nie podawaj jej w bezpośredni sposób. W odpowiedzi wywołaj metodę klasy show_details().



Oczekiwany wynik:



Running from Container class."""


class Container:
    @classmethod
    def show_details(cls):
        print("Running from " + cls.__name__ + " class.")
        # print(f'Running from {cls.__name__} class.')


Container.show_details()

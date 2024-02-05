"""Zaimplementowana jest klasa Container. Utwórz instancję tej klasy o nazwie container i wywołaj metodę klasy show_details() z poziomu tej instancji.



Oczekiwany wynik:



Running from Container class."""


class Container:
    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')


container = Container.show_details()

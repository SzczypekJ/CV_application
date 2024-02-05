"""Zdefiniowane są poniższe klasy. Użyj odpowiedniej metody do wyświetlenia MRO - Method Resolution Order dla klasy Worker i wynik wydrukuj do konsoli.



Uwaga: Rozwiązanie, które przekazuje użytkownik znajduje się w pliku o nazwie exercise.py, natomiast kod sprawdzający (który jest niewidoczny dla użytkownika) wykonywany jest z pliku o nazwie evaluate.py z poziomu, którego importowane są klasy. Dlatego zamiast nazwy modułu __main__ w odpowiedzi otrzymamy nazwę modułu w którym klasa ta jest zaimplementowana, czyli exercise.



Oczekiwany wynik:



[<class 'exercise.Worker'>, <class 'exercise.Person'>, <class 'exercise.Department'>, <class 'object'>]"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:
    def __init__(self, dept_name, short_dept_name):
        self.dept_name = dept_name
        self.short_dept_name = short_dept_name


class Worker(Person, Department):
    def __init__(self, first_name, last_name, age, dept_name):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name)


if __name__ == "__main__":
    print(Worker.mro())

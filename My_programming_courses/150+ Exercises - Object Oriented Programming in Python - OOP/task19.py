"""Napisz program, który definiuje funkcję concatenate_strings() pobierającą dowolną liczbę argumentów nazwanych przy użyciu składni **kwargs i łączącą ich wartości w pojedynczy łańcuch oddzielony łańcuchem separatora określonym jako argument domyślny - delimiter - ustawiony na znak , (przecinek).



W odpowiedzi wywołaj funkcję concatenate_strings() z poniższymi zestawami argumentów i wyniki wydrukuj do konsoli zachowując poniższą kolejność:

concatenate_strings(first_name='John', last_name='Doe', age=30)

concatenate_strings()

concatenate_strings(first_name='Mary', gender='Female')

concatenate_strings('-', first_name='Bob', gender='Male', age=5)



Oczekiwany wynik:



John,Doe,30
 
Mary,Female
Mary-Female-5


Ten program demonstruje użycie składni **kwargs w celu przekazania dowolnej liczby argumentów nazwanych w funkcji.

"""

# solution 1


def concatenate_strings(delimiter=",", **kwargs):
    concatenated_strings = []
    for key, value in kwargs.items():
        concatenated_strings.append(str(value))

    result = delimiter.join(concatenated_strings)
    print(result)


concatenate_strings(first_name='John', last_name='Doe', age=30)
concatenate_strings()

concatenate_strings(first_name='Mary', gender='Female')

concatenate_strings('-', first_name='Bob', gender='Male', age=5)

# solution 2
# def concatenate_strings(delimiter=',', **kwargs):
#     values = [str(value) for value in kwargs.values()]
#     return delimiter.join(values)


# print(concatenate_strings(first_name='John', last_name='Doe', age=30))
# print(concatenate_strings())
# print(concatenate_strings(first_name='Mary', gender='Female'))
# print(concatenate_strings('-', first_name='Bob', gender='Male', age=5))

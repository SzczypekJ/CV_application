"""Zaimplementuj funkcję o nazwie stick(), która przyjmie dowolną liczbę gołych argumentów i zwróci obiekt typu str będący sklejeniem wszystkich argumentów typu str przekazanych do funkcji znakiem '#'.



Przykład wywołania:



[IN]: stick('sport', 'summer', 4, True)


[OUT]: 'sport#summer'


W odpowiedzi wywołaj funkcję stick() na poniższe sposoby (wynik wydrukuj do konsoli):

stick('sport', 'summer')

stick(3, 5, 7)

stick(False, 'time', True, 'workout', [], 'gym')



Oczekiwany wynik:



sport#summer
 
time#workout#gym"""


def stick(*args):
    args = [arg for arg in args if isinstance(arg, str)]
    result = '#'.join(args)
    return result


print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))

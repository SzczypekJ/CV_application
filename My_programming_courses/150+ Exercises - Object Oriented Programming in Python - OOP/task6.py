"""Wykorzystując moduł wbudowany builtins zaimportuj funkcję wbudowaną sum(). Następnie wyświetl jej dokumentację i wywołaj ją na poniższej liście drukując wynik do konsoli.



[-4, 3, 2]


Oczekiwany wynik:



Help on built-in function sum in module builtins:
 
sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
 
1"""

from builtins import sum

help(sum)
print(sum([-4, 3, 2]))

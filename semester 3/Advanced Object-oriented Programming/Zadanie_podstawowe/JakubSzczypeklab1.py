#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from typing import List, Tuple, Callable, Set, Dict, NamedTuple


# Funkcja powinna zwracać wartość parametru `x`, przy czym `x` powinien być typu
#   całkowitego oraz mieć domyślną wartość 0.
#
# Dodaj odpowiednie podpowiedzi typu.
#
# ĆWICZENIE NA: podpowiedzi typu, argumenty domyślne
def f_default_arg_immutable(x: int = 0) -> int:
    return x


# Funkcja powinna przyjmować dwa argumenty:
#   (1) liczbę całkowitą oraz
#   (2) listę elementów typu całkowitego.
# Przekazanie listy jest opcjonalne, jeśli funkcja została wywołana z jednym
#   argumentem, powinno to zostać potraktowane jako przekazanie pustej listy.
# Jeśli przekazana lista zawiera mniej niż 3 elementy, na jej koniec należy
#   dołączyć element `x`.
# Funkcja powinna zwracać listę po ewentualnych modyfikacjach.
#
# Dodaj odpowiednie podpowiedzi typu.
#
# ĆWICZENIE NA: podpowiedzi typu, argumenty domyślne, len(), list.append()
def f_default_arg_mutable(x: int, data: List[int] = None) -> List:
    if not data:
        data = []
        data.append(x)
        return data
    elif len(data) < 3:
        data.append(x)
        return data
    else:
        return data


# Funkcja powinna zwracać trzyelementową krotkę zawierającą kolejno:
#   (1) pierwszy element listy `data`
#   (2) ostatni element listy `data`
#   (3) listę zawierającą elementy `data` od pierwszego do przedostatniego
# Przyjmij, że otrzymana lista zawsze zawiera co najmniej jeden element (nie
#   musisz tego sprawdzać ręcznie).
#
# ĆWICZENIE NA: krotka, indeksy (m.in indeksy ujemne), slicing
def f_indexing_and_slicing(data: list[int]) -> Tuple[int, int, List[int]]:
    x = (data[0], data[-1], data[:-1])
    return x


# Funkcja powinna zwrócić reprezentację listy wartości zmiennoprzecinkowych w postaci:
#       "<v1> - <v2> - ... - <vn>"
#   gdzie `<vi>` oznacza i-tą wartość podaną z dokładnością do dwóch miejsc po przecinku.
#   Przykładowo, dla listy [0.356, 1, 0.2] funkcja powinna zwrócić:
#       "0.36 - 1.00 - 0.20"
#
# Uzupenij podpowiedzi typwów.
#
# ĆWICZENIE NA: in, slicing, str.format(), konkatenacja łańcuchów znaków
def f_str_formatting(array) -> str:
    x = ""
    for i in array:
        x += "{0:.2f} - ".format(i)
    x = x[:-3]    #usuwam na końcu "" dwie spacje i pauzę
    return x



# Funkcja powinna zamienić miejscami pierwszy i ostatni element listy `data`
#   za pomocą JEDNEJ instrukcji (bez używania zmiennych pomocniczych)!
#
# ĆWICZENIE NA: tuple packing, tuple unpacking
def f_swap(data: List[int]) -> None:
    new_data = data[0], data[-1]
    data[-1], data[0] = new_data
    pass


# Funkcja powinna zwrócić płytką kopię listy `l_in`.
#
# ĆWICZENIE NA: płytka kopia listy
def f_shallow_copy(l_in: List[int]) -> List[int]:
    x = l_in[:]
    return x


# Funkcja powinna zwrócić funkcję zwracającą wartość argumentu powiększoną o 1.
#
# ĆWICZENIE NA: lambda
def f_lambda() -> Callable[[int], int]:
    return lambda x: x + 1


# Funkcja powinna zwrócić wartość wyrażenia logicznego:
#   "x należy do przedziału obustronnie otwartego (1, 4)
#       lub (b1 jest prawdziwe i b2 jest fałszywe)"
#
# Uzupenij podpowiedzi typwów.
#
# ĆWICZENIE NA: wyrażenia logiczne, operatory logiczne
def f_logic(x, b1, b2) -> bool:
    return (1 < x < 4) or (b1 and not b2)



# Funkcja powinna zwrócić listę składającą się z `n` elementów o wartości 1.
#
# ĆWICZENIE NA: operator `*` dla list
def f_list_creation(n: int) -> List[int]:
    list = [1]
    return list * n



# Funkcja powinna zwrócić dwuelementową krotkę  zawierającą kolejno:
#   (1) sumę liczb od 2 do 10 z pominięciem 5 i 7
#   (2) zbiór (typ `set`) zawierający te klucze słownika `dct`, których wartość
#       zawiera się w przedziale obustronnie domkniętym [1, 5]
#
# ĆWICZENIE NA: comprehensions, range(), in, not in, dict.items(), set
def f_comprehensions(dct: Dict[int, int]) -> Tuple[int, Set[int]]:
    first:set = 0
    for x in range(2,11):
        if x != 5 and x != 7:
            first += x
    second = set()
    for key,value in dct.items():
        if 1 <= value < 6:
            second.add(key)
    return first, second
# Zdefiniuj nazwaną krotkę `Point`, która służy do reprezentowania punktu na
#   płaszczyźnie (powinna zawierać składowe `x` i `y`, obie typu zmiennoprzecinkowego).
#
# ĆWICZENIE NA: nazwana krotka
class Point(NamedTuple):
    x: float
    y: float



class TestFunctions(unittest.TestCase):
    def test_f_default_arg_immutable(self):
        self.assertEqual(f_default_arg_immutable(), 0)
        self.assertEqual(f_default_arg_immutable(1), 1)

    def test_f_default_arg_mutable(self):
        self.assertListEqual(f_default_arg_mutable(1), [1])
        self.assertListEqual(f_default_arg_mutable(1), [1])
        self.assertListEqual(f_default_arg_mutable(2, [1]), [1, 2])
        self.assertListEqual(f_default_arg_mutable(4, [1, 2, 3]), [1, 2, 3])

    def test_f_indexing_and_slicing(self):
        self.assertTupleEqual(f_indexing_and_slicing([1, 2, 3]), (1, 3, [1, 2]))

    def test_f_str_formatting(self):
        self.assertEqual(f_str_formatting([0.356, 1, 0.2]), "0.36 - 1.00 - 0.20")

    def test_f_swap(self):
        array = [1, 2, 3]
        f_swap(array)
        self.assertListEqual(array, [3, 2, 1])

    def test_f_shallow_copy(self):
        array_in = [1, 2, 3]
        array_out = f_shallow_copy(array_in)
        self.assertIsNot(array_in, array_out)
        self.assertListEqual(array_in, array_out)

    def test_f_lambda(self):
        f = f_lambda()
        self.assertEqual(f(1), 2)

    def test_f_logic(self):
        self.assertTrue(f_logic(3, False, True))
        self.assertTrue(f_logic(1, True, False))
        self.assertFalse(f_logic(1, False, True))
        self.assertFalse(f_logic(1, False, False))
        self.assertFalse(f_logic(1, True, True))
        self.assertFalse(f_logic(4, True, True))

    def test_f_list_creation(self):
        self.assertListEqual(f_list_creation(3), [1, 1, 1])

    def test_f_comprehensions(self):
        self.assertTupleEqual(f_comprehensions({0: 0, 1: 1, 2: 4, 4: 5, 9: 6}),
                              (42, {1, 2, 4}))

    def test_point(self):
        self.assertTrue(issubclass(Point, tuple))
        self.assertTrue(hasattr(Point, 'x'))
        self.assertTrue(hasattr(Point, 'y'))
        Point(x=0.1, y=0.5)


if __name__ == '__main__':
    unittest.main()
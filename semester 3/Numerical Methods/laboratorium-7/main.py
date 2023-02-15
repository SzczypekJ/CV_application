import numpy as np
import scipy as sp
from scipy import linalg
from  datetime import datetime
import pickle

from typing import Union, List, Tuple


def spare_matrix_Abt(m: int,n: int):
    """Funkcja tworząca zestaw składający się z macierzy A (m,n), wektora b (n,)  i pomocniczego wektora t (m,) zawierających losowe wartości
    Parameters:
    m(int): ilość wierszy macierzy A
    n(int): ilość kolumn macierzy A
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (m,n) i wektorem (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(m, int) and isinstance(n, int):
        if m > 0 and n > 0:
            t = np.linspace(0, 1, m)
            b = np.cos(4 * t)
            A = np.vander(t, n, increasing=True)
            return A, b
        else:
            return None
    else:
        return None


def square_from_rectan(A: np.ndarray, b: np.ndarray):
    """Funkcja przekształcająca układ równań z prostokątną macierzą współczynników na kwadratowy układ równań. Funkcja ma zwrócić nową macierz współczynników  i nowy wektor współczynników
    Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (n,n) i wektorem (n,)
             Jeżeli dane wejściowe niepoprawne funkcja zwraca None
     """
    if isinstance(A, np.ndarray) and isinstance(b, np.ndarray):
        A_t = A.transpose()
        A_new = np.dot(A_t, A)
        b_new = np.dot(A_t, b)
        return A_new, b_new
    else:
        return None




def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray):
    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

      Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      x: wektor x (n,) zawierający rozwiązania równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania

      Results:
      (float)- wartość normy residuom dla podanych parametrów
      """
    if isinstance(A, np.ndarray) and isinstance(x, np.ndarray) and isinstance(b, np.ndarray):
        if len(A) == len(b) and len(x) == len(A[0]):
            r = b - np.matmul(A, np.transpose(x))
            return np.linalg.norm(r) 
        else:
            return None
    else:
        return None
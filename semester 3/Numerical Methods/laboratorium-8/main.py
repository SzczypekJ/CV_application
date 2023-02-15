import numpy as np
from numpy.lib.index_tricks import fill_diagonal
import scipy as sp
import pickle

from typing import Union, List, Tuple, Optional


def diag_dominant_matrix_A_b(m: int) -> Tuple[np.ndarray, np.ndarray]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Macierz A ma być diagonalnie zdominowana, tzn. wyrazy na przekątnej sa wieksze od pozostałych w danej kolumnie i wierszu
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: macierz diagonalnie zdominowana o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(m, int):
        if m > 0:
            A = np.random.randint(0, 9, size = (m, m))
            b = np.random.randint(0, 9, size = (m,))
            sum_ver = np.sum(np.abs(A), axis = 1)
            sum_col = np.sum(np.abs(A), axis = 0)
            A = A + np.diag(sum_ver + sum_col)
            return A, b
        else:
            return None
    else:
        return None

def is_diag_dominant(A: np.ndarray) -> bool:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest diagonalnie zdominowana
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(A, np.ndarray) and len(A.shape) == 2 and A.shape[0] == A.shape[1]:
        sum_ver = np.sum(np.abs(A), axis = 1)
        sum_col = np.sum(np.abs(A), axis = 0)
        for i in range(len(A[0])):
            if np.abs(A[i][i]) >= (sum_ver[i] - np.abs(A[i][i])) or np.abs(A[i][i]) >= (sum_col[i]- np.abs(A[i][i])):
                return True
            else:
                break
        return False
    else:
        return None


def symmetric_matrix_A_b(m: int) -> Tuple[np.ndarray, np.ndarray]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: symetryczną macierz o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(m ,int) and m > 0:
        A = np.random.randint(0, 9, size = (m, m))
        b = np.random.randint(0, 9, size = (m,))
        for i in range(m):
            for j in range(m):
                A[i][j] = A[j][i]
        return A,b
    else:
        return None

def is_symmetric(A: np.ndarray) -> bool:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest symetryczna
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(A, np.ndarray) and len(A.shape) == 2 and A.shape[0] == A.shape[1]:
        # True jeżeli odpowiadające elementy różnią się od siebie o max 1e-05
        return np.allclose(A, A.T, 1e-05, 1e-05)
    else:
        return None



def solve_jacobi(A: np.ndarray, b: np.ndarray, x_init: np.ndarray,
                 epsilon: Optional[float] = 1e-8, maxiter: Optional[int] = 100) -> Tuple[np.ndarray, int]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych
    Parameters:
    A np.ndarray: macierz współczynników
    b np.ndarray: wektor wartości prawej strony układu
    x_init np.ndarray: rozwiązanie początkowe
    epsilon Optional[float]: zadana dokładność
    maxiter Optional[int]: ograniczenie iteracji
    
    Returns:
    np.ndarray: przybliżone rozwiązanie (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    int: iteracja
    """
    if all(isinstance(i, np.ndarray) for i in [A, b, x_init]) and isinstance(epsilon, float) and isinstance(maxiter, int):
        if maxiter > 0 and epsilon > 0 and A.shape[0] == A.shape[1] and b.shape[0] == A.shape[1] and b.shape[0] == x_init.shape[0]:
            D = np.diag(np.diag(A))
            LU = A - D
            x = x_init
            for i in range(maxiter):
                x_new = np.dot(np.linalg.inv(D), b - np.dot(LU, x))
                       
                if np.linalg.norm(x_new - x) < epsilon:
                    return x_new, i
                x = x_new
            return x, maxiter
    else:
        return None
            
def random_matrix_Ab(m:int):
    """Funkcja tworząca zestaw składający się z macierzy A (m,m) i wektora b (m,)  zawierających losowe wartości
    Parameters:
    m(int): rozmiar macierzy
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (m,m) i wektorem (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(m, int) and m > 0:
        A = np.random.rand(m,m)
        b = np.random.rand(m,)
        return A,b
    else:
        return None
    
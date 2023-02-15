import numpy as np
import scipy
import pickle

from typing import Union, List, Tuple

import numbers
import math

def absolut_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray]) -> Union[int, float, np.ndarray]:
    """Obliczenie błędu bezwzględnego. 
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach/macierzach biblioteki numpy.
    
    Parameters:
    v (Union[int, float, List, np.ndarray]): wartość dokładna 
    v_aprox (Union[int, float, List, np.ndarray]): wartość przybliżona
    
    Returns:
    err Union[int, float, np.ndarray]: wartość błędu bezwzględnego,
                                       NaN w przypadku błędnych danych wejściowych
    """
    if isinstance(v, (int, float, List, np.ndarray)) and isinstance(v_aprox, (int, float, List, np.ndarray)):
        if isinstance(v, (numbers.Number)) and isinstance(v_aprox, (numbers.Number)):
            return np.abs(v - v_aprox)
        else:
            if isinstance(v, np.ndarray) and isinstance(v_aprox, np.ndarray):
                if np.size(v) == np.size(v_aprox):
                    return np.abs(np.subtract(v, v_aprox))
                if np.size(v) == np.size(v_aprox[0]):
                    return np.abs(np.subtract(v, v_aprox))
                else:
                    return float('Nan')
            if isinstance(v, List) and isinstance(v_aprox, List):
                if any(v):
                    if len(v) == len(v_aprox):
                        return np.abs(np.subtract(v, v_aprox))
                else:
                    return float('Nan')
            else:
                return np.abs(np.subtract(v, v_aprox))
    else:
        return float('Nan')
            

def relative_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray]) -> Union[int, float, np.ndarray]:
    """Obliczenie błędu względnego.
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach/macierzach biblioteki numpy.
    
    Parameters:
    v (Union[int, float, List, np.ndarray]): wartość dokładna 
    v_aprox (Union[int, float, List, np.ndarray]): wartość przybliżona
    
    Returns:
    err Union[int, float, np.ndarray]: wartość błędu względnego,
                                       NaN w przypadku błędnych danych wejściowych
    """
    if isinstance(v, (int, float, List, np.ndarray)) and isinstance(v_aprox, (int, float, List, np.ndarray)):
        if isinstance(v, (numbers.Number)) and isinstance(v_aprox, (numbers.Number)):
            if v != 0:
                return np.abs(v - v_aprox) / np.abs(v)
            else:
                return float('Nan')
        else:
            if isinstance(v, np.ndarray) and isinstance(v_aprox, np.ndarray):
                if np.size(np.where(v == 0)) == 0:
                    if np.size(v) == np.size(v_aprox):
                        return np.abs(np.subtract(v, v_aprox)) / np.abs(v)
                    if np.size(v) == np.size(v_aprox[0]):
                        return np.abs(np.subtract(v, v_aprox)) / np.abs(v)
                    else:
                        return float('Nan')
                else:
                    return float('Nan')
            if isinstance(v, List) and isinstance(v_aprox, List):
                if np.size(np.where(v == 0)) == 0:
                    if len(v) == len(v_aprox):
                        return np.abs(np.subtract(v, v_aprox)) / np.abs(v)
                    else:
                        return float('Nan')
                else:
                    return float('Nan')
            else:
                    if type(v) == int and v != 0:
                        return np.abs(np.subtract(v,v_aprox)) / np.abs(v) 
                    if type(v) == List and np.size(np.where(v == 0)) == 0:
                        return np.abs(np.subtract(v,v_aprox)) / np.abs(v) 
                    else:
                        return float('Nan')
    else:
        return float('Nan')


def p_diff(n: int, c: float) -> float:
    """Funkcja wylicza wartości wyrażeń P1 i P2 w zależności od n i c.
    Następnie zwraca wartość bezwzględną z ich różnicy.
    Szczegóły w Zadaniu 2.
    
    Parameters:
    n Union[int]: 
    c Union[int, float]: 
    
    Returns:
    diff float: różnica P1-P2
                NaN w przypadku błędnych danych wejściowych
    """
    if type(n) == int and isinstance(c, numbers.Number):
        b = 2**n
        P1 = b - b + c
        P2 = b + c - b
        return np.abs(P1-P2)
    else:
        return float('Nan')



def exponential(x: Union[int, float], n: int) -> float:
    """Funkcja znajdująca przybliżenie funkcji exp(x).
    Do obliczania silni można użyć funkcji scipy.math.factorial(x)
    Szczegóły w Zadaniu 3.
    
    Parameters:
    x Union[int, float]: wykładnik funkcji ekspotencjalnej 
    n Union[int]: liczba wyrazów w ciągu
    
    Returns:
    exp_aprox float: aproksymowana wartość funkcji,
                     NaN w przypadku błędnych danych wejściowych
    """
    if type(n) == int and n > 0 and isinstance(x, numbers.Number) and x > 0:
        e_power_x = 0
        for i in range(n):
            e_power_x += 1 / math.factorial(i) * x**i
        return e_power_x
    else:
        return float('Nan')


def coskx1(k: int, x: Union[int, float]) -> float:
    """Funkcja znajdująca przybliżenie funkcji cos(kx). Metoda 1.
    Szczegóły w Zadaniu 4.
    
    Parameters:
    x Union[int, float]:  
    k Union[int]: 
    
    Returns:
    coskx float: aproksymowana wartość funkcji,
                 NaN w przypadku błędnych danych wejściowych
    """
    if isinstance(x, numbers.Number) and isinstance(k, int):
        if k < 0:
            return float('Nan')
        if k == 0:
            return 1
        elif k == 1:
            return np.cos(x)
        else:
            return 2 * np.cos(x) * coskx1(k-1, x) - coskx1(k-2, x)
    else:
        return float('Nan')
            


def coskx2(k: int, x: Union[int, float]) -> Tuple[float, float]:
    """Funkcja znajdująca przybliżenie funkcji cos(kx). Metoda 2.
    Szczegóły w Zadaniu 4.
    
    Parameters:
    x Union[int, float]:  
    k Union[int]: 
    
    Returns:
    coskx, sinkx float: aproksymowana wartość funkcji,
                        NaN w przypadku błędnych danych wejściowych
    """
    if isinstance(x, numbers.Number) and isinstance(k, int):
        if k < 0:
            return float('Nan')
        if k == 0:
            return 1, 0
        elif k == 1:
            return np.cos(x), np.sin(x)
        else:
            return np.cos(x) * coskx2(k - 1, x)[0] - np.sin(x) * coskx2(k -1, x)[1], np.sin(x) * coskx2(k - 1, x)[0] + np.cos(x) * coskx2(k -1, x)[1]
    else:
        return float('Nan')

def pi(n: int) -> float:
    """Funkcja znajdująca przybliżenie wartości stałej pi.
    Szczegóły w Zadaniu 5.
    
    Parameters:
    n Union[int, List[int], np.ndarray[int]]: liczba wyrazów w ciągu
    
    Returns:
    pi_aprox float: przybliżenie stałej pi,
                    NaN w przypadku błędnych danych wejściowych
    """
    if isinstance(n, int):
        if n <= 0:
            return float('Nan')
        x = 0
        for i in range(1, n+1):
            x += 1 / i**2
        return np.sqrt(6 * x)
    else:
        return float('Nan')
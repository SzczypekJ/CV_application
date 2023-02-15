import numpy as np
import scipy
import pickle
import typing
import math
import types
import pickle 
from inspect import isfunction


from typing import Union, List, Tuple

def fun(x):
    return np.exp(-2*x)+x**2-1

def dfun(x):
    return -2*np.exp(-2*x) + 2*x

def ddfun(x):
    return 4*np.exp(-2*x) + 2


def bisection(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą bisekcji.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(epsilon, float) and isinstance(iteration, int) and callable(f):
        if f(a)*f(b) < 0:
            for i in range(iteration):
                x1 = (a + b) / 2
                
                if np.abs(f(x1)) <= epsilon:
                    return x1, i

                else:
                    if np.abs(a - b) < epsilon:
                        return x1, i
                    else:
                        if f(a)*f(x1) < 0:
                            b = x1
                        if f(x1)*f(b) < 0:
                            a = x1
            x2 = (a + b) / 2                
            return x2, iteration
       
    else:
        return None


def secant(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą siecznych.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(epsilon, float) and isinstance(iteration, int) and callable(f):
        if epsilon > 0 and iteration > 0:

            if f(a) * f(b) < 0:
                a0 = a
                b0 = b
                for i in range(iteration):
                    x = (f(a0)*b0 - f(b0)*a0) / (f(a0) - f(b0))

                    if f(x)*f(a0) > 0:
                        a0 = x
                    if f(x)*f(b0) > 0:
                        b0 = x

                    if np.abs(f(x)) <= epsilon or np.abs(b - a) < epsilon:
                        return x, i
                
                x_max = (f(a0)*b0 - f(b0)*a0) / (f(a0) - f(b0))
                return x_max, iteration

            else:
                return None
    else:
        return None
            

def newton(f: typing.Callable[[float], float], df: typing.Callable[[float], float], ddf: typing.Callable[[float], float], a: Union[int,float], b: Union[int,float], epsilon: float, iteration: int) -> Tuple[float, int]:
    ''' Funkcja aproksymująca rozwiązanie równania f(x) = 0 metodą Newtona.
    Parametry: 
    f - funkcja dla której jest poszukiwane rozwiązanie
    df - pochodna funkcji dla której jest poszukiwane rozwiązanie
    ddf - druga pochodna funkcji dla której jest poszukiwane rozwiązanie
    a - początek przedziału
    b - koniec przedziału
    epsilon - tolerancja zera maszynowego (warunek stopu)
    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(epsilon, float) and isinstance(iteration, int) and callable(f) and callable(df) and callable(ddf):
        if epsilon > 0 and iteration > 0:           
            a_b = np.linspace(a, b, 1000)
            df_wartosci = df(a_b)
            ddf_wartosci = ddf(a_b)
            
            if not ((np.all(np.sign(df_wartosci) < 0) or np.all(np.sign(df_wartosci) > 0)) and
                    (np.all(np.sign(ddf_wartosci) < 0) or np.all(np.sign(ddf_wartosci) > 0))):
                return None

            if f(a) * ddf(a) > 0:
                x = a

            else:
                x = b

            if f(a) * f(b) < 0:
                for i in range(iteration):
                    x_n = x - f(x) / df(x)

                    if np.abs(x_n - x) < epsilon:
                        return x_n, i

                    x = x_n
                    
                return x, iteration
    else:
        return None

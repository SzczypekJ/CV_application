import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from numpy.core._multiarray_umath import ndarray
from numpy.polynomial import polynomial as P
import pickle

# zad1
def polly_A(x: np.ndarray):
    """Funkcja wyznaczajaca współczynniki wielomianu przy znanym wektorze pierwiastków.
    Parameters:
    x: wektor pierwiastków
    Results:
    (np.ndarray): wektor współczynników
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    
    if isinstance(x, np.ndarray):
        r = P.polyfromroots(x)
        return r
    else:
        return None

def roots_20(a: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray): wektor współczynników i miejsc zerowych w danej pętli
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """

    if isinstance(a, np.ndarray) and a.shape[0] != 0:
        a = np.array(a, dtype=float)

        rand_samp = np.random.random_sample(a.shape[0]) * 1e-10
        a += rand_samp

        return a, P.polyroots(a)
    else:
        return None
# zad 2

def frob_a(wsp: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray, np.ndarray, np. ndarray,): macierz Frobenusa o rozmiarze nxn, gdzie n-1 stopień wielomianu,
    wektor własności własnych, wektor wartości z rozkładu schura, wektor miejsc zerowych otrzymanych za pomocą funkcji polyroots

                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    
    if isinstance(wsp, np.ndarray):
        l = len(wsp) - 1
        m1 = np.eye(l)
        m0 = np.zeros((l, 1))
        frob = np.concatenate((m0, m1), axis=1)
        frob = np.concatenate((frob, np.reshape(-wsp, (1, wsp.shape[0]))), axis=0)

        return frob, np.linalg.eigvals(frob), scipy.linalg.schur(frob), P.polyroots(wsp)

    return None
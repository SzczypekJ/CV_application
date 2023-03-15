import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not (isinstance(category, int) or isinstance(category, str)):
        return None

    txt = """
        SELECT film.title as title, language.name as languge, category.name as category
        FROM film
        INNER JOIN language ON language.language_id = film.language_id
        INNER JOIN film_category ON film_category.film_id = film.film_id
        INNER JOIN category ON category.category_id = film_category.category_id
        WHERE {Category}
        ORDER BY film.title, language.name
    """.format(**{"Category": {int: "category.category_id = {}".format(category),
                               str: "category.name = \'{}\'".format(category)}[type(category)]})
    
    df = pd.read_sql(txt, con=connection)
    
    return df
    
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not(isinstance(category, int) or isinstance(category, str)):
        return None
    
    txt = """
        SELECT film.title as title, language.name as languge, category.name as category
        FROM film
        INNER JOIN language ON language.language_id = film.language_id
        INNER JOIN film_category ON film_category.film_id = film.film_id
        INNER JOIN category ON category.category_id = film_category.category_id
        WHERE {Category}
        ORDER BY film.title, language.name
    """.format(**{"Category": {int: "category.category_id = {}".format(category),
                               str: "lower(category.name) = lower(\'{}\')".format(category)}[type(category)]})
    
    df = pd.read_sql(txt, con=connection)
    
    return df
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not(isinstance(title, str)):
        return None
    
    txt = """
        SELECT actor.first_name as first_name, actor.last_name as last_name
        FROM actor
        INNER JOIN film_actor ON film_actor.actor_id = actor.actor_id
        INNER JOIN film ON film.film_id = film_actor.film_id
        WHERE film.title SIMILAR TO '{TITLE}'
        ORDER BY actor.last_name, actor.first_name
    """.format(**{"TITLE": title})
    
    df = pd.read_sql(txt, con=connection)
    
    return df
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not(isinstance(words, list)):
        return None
    
    WORDS = "|".join(["((^| ){}( |$))".format(word.lower()) for word in words])
    txt = """
        SELECT film.title as title
        FROM film
        WHERE lower(film.title) ~ \'{WORD_CHOICE}\'
    """.format(**{"WORD_CHOICE": WORDS})
    
    df = pd.read_sql(txt, con=connection)
    
    return df







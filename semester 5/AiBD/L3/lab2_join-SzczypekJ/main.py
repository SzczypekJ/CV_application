import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego id kategorii.
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if not isinstance(category_id, int):
        return None
    
    txt = """
        SELECT film.title as title, language.name as languge, category.name as category
        FROM category
        INNER JOIN film_category ON category.category_id = film_category.category_id
        INNER JOIN film ON film.film_id = film_category.film_id
        INNER JOIN language ON language.language_id = film.language_id
        WHERE category.category_id = {Category_id} 
        ORDER BY film.title, language.name
    """.format(**{"Category_id": category_id})
    
    df = pd.read_sql(txt, con=connection)

    return df
    
def number_films_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów w zadanej kategori przez id kategorii.
    Przykład wynikowej tabeli:
    |   |category   |count|
    |0	|Action 	|64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(category_id, int):
        return None
    
    txt = """
        SELECT category.name as category, count(film.film_id) as count
        FROM film
        INNER JOIN film_category ON film_category.film_id = film.film_id
        INNER JOIN category ON category.category_id = film_category.category_id
        WHERE category.category_id = {Category_id}
        GROUP BY category.name
    """.format(**{"Category_id": category_id})
    
    df = pd.read_sql(txt, con=connection)
    
    return df

def number_film_by_length(min_length: Union[int,float] = 0, max_length: Union[int,float] = 1e6 ) :
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów o dla poszczegulnych długości pomiędzy wartościami min_length a max_length.
    Przykład wynikowej tabeli:
    |   |length     |count|
    |0	|46 	    |64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    min_length (int,float): wartość minimalnej długości filmu
    max_length (int,float): wartość maksymalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if not ( (isinstance(min_length, int) or isinstance(min_length, float))
        and ((isinstance(max_length, int) or isinstance(max_length, float)))
        and (min_length < max_length)):
            return None
    
    txt = """
        SELECT film.length as length, count(film.film_id) as count
        FROM film
        WHERE film.length
        BETWEEN {Min_length} AND {Max_length}
        GROUP BY film.length
        ORDER BY film.length
    """.format(**{"Min_length": min_length, "Max_length": max_length})
                  
    df = pd.read_sql(txt, con=connection)
    
    return df

def client_from_city(city:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o listę klientów z zadanego miasta przez wartość city.
    Przykład wynikowej tabeli:
    |   |city	    |first_name	|last_name
    |0	|Athenai	|Linda	    |Williams
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    city (str): nazwa miaste dla którego mamy sporządzić listę klientów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(city, str):
        return None
    
    txt = """
        SELECT city.city , customer.first_name, customer.last_name
        FROM customer
        INNER JOIN address ON address.address_id = customer.address_id
        INNER JOIN city ON city.city_id = address.city_id
        WHERE city.city = \'{City}\'
        ORDER BY customer.last_name , customer.first_name
    """.format(**{"City": city})
    
    df = pd.read_sql(txt, con=connection)
    
    return df

def avg_amount_by_length(length:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o średnią wartość wypożyczenia filmów dla zadanej długości length.
    Przykład wynikowej tabeli:
    |   |length |avg
    |0	|48	    |4.295389
    
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    length (int,float): długość filmu dla którego mamy pożyczyć średnią wartość wypożyczonych filmów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not (isinstance(length, int) or isinstance(length, float)):
        return None
    
    txt = """ 
        SELECT f.length as length, avg(pay.amount) as avg
        FROM film f
        INNER JOIN inventory inv ON f.film_id = inv.film_id
        INNER JOIN rental ren ON ren.inventory_id = inv.inventory_id
        INNER JOIN payment pay ON pay.rental_id = ren.rental_id
        WHERE f.length = {Length}
        GROUP BY f.length
    """.format(**{"Length": length})

    df = pd.read_sql(txt, con= connection)
    return df

def client_by_sum_length(sum_min:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o sumaryczny czas wypożyczonych filmów przez klientów powyżej zadanej wartości .
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |sum
    |0  |Brian	    |Wyman  	|1265
    
    Tabela wynikowa powinna być posortowane według sumy, imienia i nazwiska klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    sum_min (int,float): minimalna wartość sumy długości wypożyczonych filmów którą musi spełniać klient
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not (isinstance(sum_min , int) or isinstance(sum_min, float)):
        return None
    
    txt = """
        SELECT customer.first_name as first_name , customer.last_name as last_name , sum(film.length) as sum
        FROM customer
        INNER JOIN rental ON rental.customer_id = customer.customer_id
        INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
        INNER JOIN film ON film.film_id = inventory.film_id
        GROUP BY customer.customer_id
        HAVING sum(film.length) > {Sum_min}
        ORDER BY sum(film.length), customer.last_name, customer.first_name
    """.format(**{"Sum_min": sum_min})
    
    df = pd.read_sql(txt, con=connection)
    
    return df

def category_statistic_length(name:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o statystykę długości filmów w kategorii o zadanej nazwie.
    Przykład wynikowej tabeli:
    |   |category   |avg    |sum    |min    |max
    |0	|Action 	|111.60 |7143   |47 	|185
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    name (str): Nazwa kategorii dla której ma zostać wypisana statystyka
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(name, str):
        return None
            
    txt = """SELECT category.name as category, avg(film.length) as avg, sum(film.length) as sum, min(film.length) as min, max(film.length) as max
        FROM category
        INNER JOIN film_category on category.category_id = film_category.category_id
        INNER JOIN film on film.film_id = film_category.film_id
        WHERE category.name = \'{Name}\'
        GROUP BY category.name
        """.format(**{"Name": name})

    df = pd.read_sql(txt, con= connection)
    return df
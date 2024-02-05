"""Zdefiniowana jest funkcja stock_info(). Przykładowe wywołanie funkcji:



[IN]: print(stock_info('Apple', 'USA', 115, '$'))


Company: Apple
Country: USA
Price: $ 115


Używając odpowiedniego atrybutu funkcji stock_info() wyświetl do konsoli nazwy wszystkich argumentów tej funkcji.



Oczekiwany wynik:



('company', 'country', 'price', 'currency')"""


import inspect


def stock_info(company, country, price, currency):
    return (
        f'Company: {company}\nCountry: {country}'
        f'\nPrice: {currency} {price}'
    )


# Enter your solution here
# solution 1
print(tuple(inspect.signature(stock_info).parameters.keys()))
# solution 2
print(stock_info.__code__.co_varnames)

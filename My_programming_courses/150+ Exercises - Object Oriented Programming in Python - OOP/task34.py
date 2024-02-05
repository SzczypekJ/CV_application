"""Poniżej zdefiniowana jest klasa o nazwie Phone. Wykorzystując notację kropkową (dot notation) zmodyfikuj wartość atrybutów:

brand na 'Samsung'

model na 'Galaxy'



W odpowiedzi wydrukuj wartości atrybutów brand oraz model do konsoli tak jak pokazano poniżej.



Oczekiwany wynik:



brand: Samsung
model: Galaxy"""


class Phone:
    brand = 'Apple'
    model = 'iPhone X'


Phone.brand = "Samsung"
Phone.model = "Galaxy"

print(f"brand: {Phone.brand}")
print(f"model: {Phone.model}")

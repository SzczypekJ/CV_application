"""Poniżej zdefiniowana jest klasa o nazwie Laptop. Wykorzystując funkcję wbudowaną setattr() zmodyfikuj wartość atrybutów:

brand na 'Acer'

model na 'Predator'



W odpowiedzi wykorzystując funkcję wbudowaną getattr() oraz print() wydrukuj wartości atrybutów brand oraz model do konsoli tak jak pokazano poniżej.



Oczekiwany wynik:



brand: Acer
model: Predator"""


class Laptop:
    brand = 'Lenovo'
    model = 'ThinkPad'


setattr(Laptop, 'brand', 'Acer')
setattr(Laptop, 'model', 'Predator')

print(f"brand: {Laptop.brand}")
print(f"model: {Laptop.model}")

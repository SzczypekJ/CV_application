"""Zaimplementuj klasę o nazwie TechStack, która ma jeden atrybut chroniony instancji o nazwie _tech_names. Następnie wykorzystując dekorator @property utwórz właściwość o nazwie tech_names (właściwość do odczytu, modyfikacji i usuwania). Nie dokonuj żadnej walidacji.



Utwórz instancję klasy o nazwie tech_stack i wartości atrybutu tech_names:

'python,java,sql'



Wydrukuj zawartość atrybutu tech_names do konsoli. Następnie dokonaj modyfikacji tego atrybutu na wartość: 'python,sql'.



I także wydrukuj zawartość atrybutu tech_names do konsoli. Kolejno usuń atrybut tech_names instancji tech_stack. Wydrukuj zawartość atrybutu słownikowego __dict__ instancji tech_stack do konsoli.



Oczekiwany wynik:



python,java,sql
python,sql
{}
"""
class TechStack:
    def __init__(self, tech_names):
        self._tech_names = tech_names
    
    @property
    def tech_names(self):
        return self._tech_names

    @tech_names.setter
    def tech_names(self, value):
        self._tech_names = value
    
    @tech_names.deleter
    def tech_names(self):
        del self._tech_names

tech_stack = TechStack('python,java,sql')
print(tech_stack.tech_names)

tech_stack.tech_names = 'python,sql'
print(tech_stack.tech_names)

del tech_stack.tech_names
print(tech_stack.__dict__)
"""Zdefiniuj klasę Container, która będzie posiadać metodę statyczną (użyj klasy staticmethod - zrób to w klasyczny sposób) o nazwie get_current_time() zwracającą aktualny czas w formacie '%H:%M:%S', np. '09:45:10'."""

import time

# solution 1
class Container:

    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S')


cont = Container()
print(cont.get_current_time())

# solution 2
# class Container:
#     def get_current_time():
#         return time.strftime('%H:%M:%S', time.localtime())
 
#     get_current_time = staticmethod(get_current_time)
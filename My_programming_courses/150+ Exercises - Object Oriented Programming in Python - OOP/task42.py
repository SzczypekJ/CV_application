"""Zaimplementuj klasę HouseProject z atrybutami klasy odpowiednio:

number_of_floors = 3

area = 100



Następnie zaimplementuj funkcję (atrybut wywoływalny klasy) o nazwie describe_project() która wyświetli podstawowe informacje o projekcie w formacie takim jak podano poniżej:



Floor number: 3
Area: 100


W odpowiedzi wywołaj funkcję describe_project().



Oczekiwany wynik:



Floor number: 3
Area: 100"""

# solution 1
class HouseProject:
    number_of_floors = 3
    area = 100

    def describe_project(self):
        print("Floor number:", self.number_of_floors)
        print("Area:", self.area)

project = HouseProject()
project.describe_project()


# solution 2
# class HouseProject:
#     number_of_floors = 3
#     area = 100
 
#     def describe_project():
#         print(
#             f'Floor number: {HouseProject.number_of_floors}\n'
#             f'Area: {HouseProject.area}'
#         )
 
 
# HouseProject.describe_project()
"""
Задание 2
Описать класс,  который  хранит список всех своих экземпляров, доступ к которому можно получить с помощью метода
getInstances().
class MyClass():
	__instances = []
	…
A =  MyClass()
B =  MyClass()
for obj in MyClass.getInstances()):
	…
"""



class MyClass:
    __instances = []

    def __init__(self):
        MyClass.__instances.append(self)

    def getInstances():
        return MyClass.__instances


A = MyClass()
B = MyClass()
for obj in MyClass.getInstances():
    print(obj)

"""
Задание 1
Даны три  пары точек:
1.	A1(xa1, ya1), A2(xb2, yb2)
2.	B1(xb1, yb1), B2(xb2, yb2)
3.	С1(xс1, yс1), С2(xс2, yс2)
Через данные пары точек проходят прямые a, b, c соответственно.
Определить отношение между  прямыми (три прямые параллельны; две прямые параллельны; три прямые пересекаются и т.д.).
Если три прямые пересекаются, более чем в одной точке, то они образуют треугольник.
Вычислить площадь этого треугольника.

Входные данные
Шесть пар чисел типа float по четыре числа в строке — координаты точек, через которые проходят прямые.

Вывод
В первой строке вывести отношение между прямыми.
Варианты:
"a || b || c", если три прямые параллельны
"a || b" или "a || с" или "b || с", если только две прямые параллельны
"a /\ b /\ c", если три прямые пересекаются
Во второй строке вывести площадь треугольника, если три прямые пересекаются, более  чем в одной точке.
В остальных случаях вывести 0.
Пример
Входные данные
1.0 1.0 2.0 1.5
1.0 1.5 2.0 2.0
2.0 3.0 3.0 1.5

Вывод
a || b
0

Код должен быть переносимым и пригодным для многоразового использования (подразумевается создание функций, для поиска точки пересечения прямых и т.п.).
Код должен быть хорошо структурирован. Будет оцениваться архитектурная составляющая.
"""


# y=kx+b
# a=[x1,y1,x2,y2]
# equation(a)=[x1,y1,x2,y2,k,b]
#               0  1  2  3 4 5
def equation(a):
    if (a[0] - a[2]) != 0:
        # k =    ( y2   -  y1) / ( x2  -  x1)
        a.append((a[3] - a[1]) / (a[2] - a[0]))
    else:
        a.append(0)
    a.append(a[1] - a[4] * a[0])
    return a


# точка пересечения прямых a , b
# a,b = [x1,y1,x2,y2,k,b]
# interseption(a,b) =[x,y]
def intersection(a, b):
    return [(a[5] - b[5]) / (a[4] - b[4]), (b[4]*a[5]-a[4]*b[5])/(a[4]-b[4])]


# a,b = [x1,y1,x2,y2,k,b]
def parallelism(a, b):
    print(a)
    print(b)
    return a[4] == b[4]


# a = [[x0,y0],[x1,y1],[x2,y2]]
def area(a):
    return 0.5 * abs((a[0][0] - a[2][0]) * (a[1][1] - a[2][1]) - (a[1][0] - a[2][0]) * (a[0][1] - a[2][1]))


x = []
print('Введите координаты.')
for i in range(3):
    x.append([float(j) for j in input().split()])
    equation(x[i])
print(x)

if parallelism(x[1], x[2]) and parallelism(x[0], x[1]):
    print("a || b || c \n0")
elif parallelism(x[0], x[1]):
    print("a || b \n0")
elif parallelism(x[1], x[2]):
    print("b || c \n0")
elif parallelism(x[0], x[2]):
    print("a || c \n0")
elif intersection(x[0], x[1]) != intersection(x[0], x[2]):
    print("a /\ b /\ c \n" + str(area([intersection(x[0], x[1]), intersection(x[0], x[2]), intersection(x[1], x[2])])))
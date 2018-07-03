"""
Задание 4
Пусть две точки A и B являются симметричными относительно прямой d, если отрезок АВ перпендикулярен прямой d, и
расстояние от точек A и B до прямой d одинаково.
Дано множество точек на плоскости, количество точек чётное:
(x1, y1), …, (xn, yn)
Определить, существует ли прямая d, параллельная одной из осей координат, которая разбивает данное множество на два
подмножества, таких что для каждой точки A(xi, yi)  из первого подмножества существует точка B(xj yj), которая
симметрична точке  A относительно прямой d.
Если  прямая существует, вывести  "YES", иначе "NO".
"""
import numpy as np
from task3 import decorator

@decorator
def symmetryCheck(pointsX, axis):
    x = np.array(pointsX)
    average = sum(x[:, axis]) / len(x[:, axis])
    check = True
    for point in pointsX:
        if axis == 0:
            symmetryPoint = [(average + average - point[0]), point[1]]
        else:
            symmetryPoint = [point[0], (average + average - point[1])]
        if not (symmetryPoint in pointsX):
            check = False
    return check

points = []
point = input()
while point:
    points.append([float(j) for j in point.split()])
    point = input()

if symmetryCheck(points, 0) or symmetryCheck(points, 1):
    print("YES")
else:
    print("NO")

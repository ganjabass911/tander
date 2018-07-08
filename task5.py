# coding=utf-8
"""
Задание 5 *
Дано множество отрезков, представляющих собой рёбра дорожного графа (файл data.xls).

F_VerticeId — id первой вершины ребра
T_VerticeId - id второй вершины ребра
dist — вес ребра (расстояние)
F_POINT_X — долгота вершины F_VerticeId
F_POINT_Y - широта вершины F_VerticeId
T_POINT_X - долгота вершины T_VerticeId
T_POINT_Y - широта вершины T_VerticeId

На входе программа должна получать координаты двух точек, причём:
38,9774837690821 <  долгота < 39,0283642309179
45,0549145480683 < широта < 45,0908534519317
Эти точки необязательно являются вершинами графа. Они могут находиться вблизи дорог.

Необходимо построить кратчайший маршрут по дорогам между двумя точками, которые были даны на входе, и вывести расстояние
между этими точками по дорогам.
Визуализировать результат. То есть необходимо нанести на карту все дороги из файла data.xls, и полученный кратчайший
маршрут выделить каким-либо цветом, отличным от цвета других дорог.

"""
import math
import os
import simplekml
import xlrd


# столбец матрицы ( матрица, индекс столбца)
def generatorCollumn(matrix, colnum):
    return [init[colnum] for init in matrix]


# получение точек
def generatorPoints(data):
    gen = {}
    for i in range(len(data)):
        if i != 0:
            branche = data[i]
            if not (branche[0] in gen):
                gen.update({int(branche[0]): [branche[2], branche[3]]})
            if not (branche[1] in gen):
                gen.update({int(branche[0]): [branche[4], branche[5]]})
    return gen


file = xlrd.open_workbook('data.xls', formatting_info=True)
sheet = file.sheet_by_index(0)
# кортеж исходной таблицы
data = tuple(sheet.row_values(rownum) for rownum in range(sheet.nrows))

# словарь точек
points = generatorPoints(data)


def borderPoints(points):
    left = 180
    right = 0
    bottom = 90
    top = 0
    for point in points:
        left = min(left, points.get(point)[0])
        right = max(right, points.get(point)[0])
        bottom = min(bottom, points.get(point)[1])
        top = max(top, points.get(point)[1])
    return {'left': left, 'right': right, 'bottom': bottom, 'top': top}


border = {'left': 38.7518678245754, 'right': 38.8036140188757, 'bottom': 45.0968821926186, 'top': 45.1335440675189}


# проверка ввода
def initCheck():
    while True:
        x = float(input())
        if border.get('left') <= x <= border.get('right') or border.get('bottom') <= x <= border.get('top'):
            return x
        else:
            print('Ошибка! Введте корректные данные!')


# Ввод
def init():
    print('Введите координаты первой точки: долгота широта')
    a = [initCheck(), initCheck()]

    print('Введите координаты второй точки')
    b = [initCheck(), initCheck()]
    return a, b


# поиск ближайшей точки
def findPoint(a, points):
    x = list(points.keys())[0]
    # print(x)
    a.append(x)
    distance = math.sqrt((points.get(x)[0] - a[0]) ** 2 + (points.get(x)[1] - a[1]) ** 2)
    for point in points:
        dist1 = math.sqrt((points.get(point)[0] - a[0]) ** 2 + (points.get(point)[1] - a[1]) ** 2)
        if distance > dist1:
            a[2] = point
            distance = dist1


# def floidBellman(point1, point2, data, n):
#     # m - количество ребер
#     # n - количество вершин
#
#     d = [math.inf for i in range(n)]
#     d[0] = 0
#     for i in range[n]:
#         for j in range:
#             if branch!=data[0]:
#                 if d


file = xlrd.open_workbook('data.xls', formatting_info=True)
sheet = file.sheet_by_index(0)
# кортеж исходной таблицы
data = tuple(sheet.row_values(rownum) for rownum in range(sheet.nrows))

# словарь точек
points = generatorPoints(data)
mx = 0
for point in points:
    mx = max(mx, point)

# a, b = init()
a, b = [38.98, 45.07], [39, 45.05]

findPoint(a, points)
findPoint(b, points)
#
# # a[2][0]id точки близкой к нужной точке А
# kml = simplekml.Kml()
# kml.newpoint(name="A", coords=[(points.get(a[2]))])  # lon, lat, optional height
# kml.newpoint(name="B", coords=[(points.get(b[2]))])
# kml.newpoint(name="a", coords=[(38.98, 45.07)])
# kml.newpoint(name="b", coords=[(39, 45.05)])
# kml.newpoint(name="0", coords=[(points.get(list(points.keys())[0]))])
# kml.save("1.kml")



print(border)
k = simplekml.Kml()
k.newpoint(name="lt", coords=[(border.get('left'), border.get('top'))])
k.newpoint(name="lb", coords=[(border.get('left'), border.get('bottom'))])
k.newpoint(name="rt", coords=[(border.get('right'), border.get('top'))])
k.newpoint(name="rb", coords=[(border.get('right'), border.get('bottom'))])
k.newlinestring(name="left", description="llllllllll",
                  coords=[(border.get('left'), border.get('top')), (border.get('left'), border.get('bottom'))])
k.newlinestring(name="right", description="rrrrrrrrr",
                  coords=[(border.get('right'), border.get('top')), (border.get('right'), border.get('bottom'))])
k.newlinestring(name="top", description="ttttttttttt",
                  coords=[(border.get('left'), border.get('top')), (border.get('right'), border.get('top'))])
k.newlinestring(name="bottom", description="bbbbbbbbbbbb",
                  coords=[(border.get('left'), border.get('bottom')), (border.get('right'), border.get('bottom'))])
k.save("border.kml")
"""
проблема в неверном условии:
38,9774837690821 <  долгота < 39,0283642309179
45,0549145480683 < широта < 45,0908534519317
"""

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

# края точек в data.xml
border = {'left': 38.7518678245754, 'right': 38.8036140188757, 'bottom': 45.0968821926186, 'top': 45.1335440675189}


# столбец матрицы ( матрица, индекс столбца)
def generatorCollumn(matrix, colnum):
    return [init[colnum] for init in matrix]


# чтение таблицы из файла
def dataInit(file):
    sheet = xlrd.open_workbook(file, formatting_info=True).sheet_by_index(0)

    # data = {}
    # for rownum in range(sheet.nrows):
    #     if rownum != 0:
    #         p = int(sheet.row_values(rownum)[0]), int(sheet.row_values(rownum)[1])
    #         data.update({p: [float(sheet.row_values(rownum)[2]),
    #                          float(sheet.row_values(rownum)[3]), float(sheet.row_values(rownum)[4]),
    #                          float(sheet.row_values(rownum)[5]), sheet.row_values(rownum)[6]]})
    # return data
    # try:
    #     list1 =float(sheet.row_values(4)[6].split())
    # except ValueError as e:
    #     print( "error", e)

    return tuple([int(sheet.row_values(rownum)[0]),
                  int(sheet.row_values(rownum)[1]),
                  float(sheet.row_values(rownum)[2]),
                  float(sheet.row_values(rownum)[3]),
                  float(sheet.row_values(rownum)[4]),
                  float(sheet.row_values(rownum)[5]),
                  float(sheet.row_values(rownum)[6])] for rownum in range(sheet.nrows) if rownum != 0)

    # кортеж исходной таблицы


# получение точек
def generatorPoints(data):
    gen = {}
    for road in data:
        if not (road[0] in gen):
            gen.update({int(road[0]): [road[2], road[3]]})
        if not (road[1] in gen):
            gen.update({int(road[1]): [road[4], road[5]]})
    return gen


# нахождение границ
def borderPoints(points):
    left = 180
    right = 0
    bottom = 90
    top = 0
    for point in points:
        left = mmm(left, points.get(point)[0])
        right = max(right, points.get(point)[0])
        bottom = mmm(bottom, points.get(point)[1])
        top = max(top, points.get(point)[1])
    return {'left': left, 'right': right, 'bottom': bottom, 'top': top}


# Ввод
def init():
    # проверка ввода
    def initCheck():
        while True:
            x = float(input())
            if border.get('left') <= x <= border.get('right') or border.get('bottom') <= x <= border.get('top'):
                return x
            else:
                print('Ошибка! Введте корректные данные!')

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


# не работает должным образом
def floidBellman(point1, data):
    # m - количество ребер
    # n - количество вершин

    points = dict.fromkeys(generatorPoints(data).keys(), 200000)
    points.update({point1: 0})
    for point in points:
        if point != point1:
            for road in data:
                if points.get(road[1]) > (points.get(road[0]) + float(road[6])):
                    points.update({road[1]: points.get(road[0]) + float(road[6])})
                if points.get(road[0]) > points.get(road[1]) + float(road[6]):
                    points.update({road[0]: points.get(road[1]) + float(road[6])})

    return points


# соседние вершины, в которые идут ребра
def waysTo(data):
    ways = {}
    for way in data:
        if not ways.get(way[0]):
            ways.setdefault(way[0], [way[1]])
        else:
            c = list(ways.get(way[0]))
            c.append(way[1])
            ways.update({way[0]: c})
        # if not ways.get(way[1]):
        #     ways.setdefault(way[1], [way[0]])
        # else:
        #     c = list(ways.get(way[1]))
        #     c.append(way[0])
        #     ways.update({way[0]: c})
    return ways


# соседние вершины, из которых идут ребра
def waysFrom(data):
    ways = {}
    for way in data:
        if not ways.get(way[1]):
            ways.setdefault(way[1], [way[0]])
        else:
            c = list(ways.get(way[1]))
            c.append(way[0])
            ways.update({way[0]: c})
    return ways


def dijkstra(point1, point2, data):
    dist = dict.fromkeys(generatorPoints(data).keys(), 10000)

    # Соседние вершины
    wt = waysTo(data)
    dist.update({point1: 0})
    parents = dict.fromkeys(generatorPoints(data).keys(), False)
    mark = parents.copy()

    # пути
    roads = {(road[0], road[1]): road[6] for road in data}
    # roads.update({(road[1], road[0]): road[6] for road in data})
    v = point1
    if wt.get(v):
        for j in wt.get(v):
            now = dist.get(v)
            p = v, j
            to = now + roads.get(p)

            if dist.get(j) > to:
                dist.update({j: to})
                parents.update({v: j})
    for i in dist.keys():

        # выбирается вершина с наименьшей величиной dist.get(j)
        for j in dist.keys():
            if not (mark.get(j)) and (v == point1 or dist.get(j) < dist.get(v)):
                v = j
        # if dist.get(v) ==100:
        #     continue

        # вершина помечается
        mark.update({v: True})
        # просматриваем все ребра (v,to) и пытаемся улучшить значение dist.get(to)
        if wt.get(v):
            for j in wt.get(v):
                way=v,j
                newadd = roads.get(way)
                if newadd:
                    now = dist.get(v)
                    p = v, j

                    frome=dist.get(j)
                    to = dist.get(v) + roads.get(way)
                    if frome > dist.get(v) + roads.get(way):
                        dist.update({j: to})
                        parents.update({v: j})

    return dist


data = dataInit('data.xls')
# словарь точек
points = generatorPoints(data)

# a, b = init()
# a, b = [38.75337683, 45.11878547], [38.8036140188757, 45.0968821926186]
a, b = 51362963, 51986257
ways=waysTo(data)
while True:
    print(ways.get(a))
    roads = {(road[0], road[1]): road[6] for road in data}
    w=[(a,b) for b in ways.get(a)]
    print([roads.get(i) for i in w])
    a=int(input())

# findPoint(a, points)
# findPoint(b, points)

# roads = floidBellman(a[2], data)
roads = dijkstra(a, b, data)
mmm = 10000
# vl = (list(roads.values()))
# for i in vl:
#     if i != 0:
#         mmm = min(mmm, i)
print(roads.get(b))
# kml = simplekml.Kml()
# for road in data:
#     # kml.newpoint(coords=[(points.get(point))])
#     kml.newlinestring(description=str(road[6]),
#                       coords=[(road[2], road[3]), (road[4], road[5])]).style.linestyle.color = simplekml.Color.blue
#
# kml.save("5.kml")
"""
проблема в неверном условии:
38,9774837690821 <  долгота < 39,0283642309179
45,0549145480683 < широта < 45,0908534519317

    
    
    точки в файле 
    """

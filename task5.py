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
# from geopy.geocoders import Nominatim
# location = Nominatim().reverse("45.1186483816458, 38.7546263112622")
# print(location.address)
# %pylab inline
import matplotlib.pylab as plt
# from mpl_toolkit
import xlrd
import numpy as np
import geopy.geocoders as geo


def collumn(matrix, colnum):
    return [init[colnum] for init in matrix]

'''basemap'''
file = xlrd.open_workbook('data.xls', formatting_info=True)
sheet = file.sheet_by_index(0)
# for rownum in range(sheet.nrows):
#     row=sheet.row_values(rownum)
#     for c_el in row:
#         print(c_el)
# print(sheet.row_values(0)[0])
points = []
# np.append(points, [[sheet.row_values(0)[0], sheet.row_values(0)[2], sheet.row_values(0)[3]]], axis=0)
# print(points)
for rownum in range(sheet.nrows):
    if rownum != 0:
        if not (sheet.row_values(rownum)[0] in collumn(points, 0)):
            points.append([sheet.row_values(rownum)[0], sheet.row_values(rownum)[2], sheet.row_values(rownum)[3]])
            print(geo.Nominatim().reverse(str(sheet.row_values(rownum)[3]) + ", " + str(sheet.row_values(rownum)[2])))
    # print(points)





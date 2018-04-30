from constants import *

# Здесь должен быть реализован класс bullet (кружочки со своими соординатами, радиусом, скоростями по осям и цветом)
# + со своим методом draw (класс можно написать в main)
# роцедура при вызове которой:
# в массиве bullets создается новый объект типа bullet (в случайном месте за экраном,
# летящая по направлению к самолётику)

#Первый залив функции про пересечение многоугольника и снаряда, свисите Руслаше Г. если что поправить

def distance(x_p, y_p, x_l, y_l, c_l):
    '''Return the distance between the point (x_p, y_p) and the line x_l * x + y_l * y + c_l = 0'''
    return (abs(x_l * x_p + y_l * y_p + c_l) / (x_l ** 2 + y_l ** 2) ** 0.5)


def straight(a, b):
    '''Return A, B, С from straight line Ax + Bx + С = 0 equation, which includes points a and b'''
    if a[0] == b[0]:
        return [1, 0, -a[0]]
    elif a[1] == b[1]:
        return [0, 1, -a[1]]
    else:
        return [b[1] - a[1], a[0] - b[0], a[1] * (b[0] - a[0]) - a[0] * (b[1] - a[1])]


def projection(x_p, y_p, alfa):
    '''Return coordinates of point M (x_p, y_p) projection onto line alfa'''
    if alfa[0] == 0:
        return [x_p, - alfa[2] / alfa[1]]
    elif alfa[1] == 0:
        return [- alfa[2] / alfa[0], y_p]
    else:
        x0 = (alfa[1] * x_p / alfa[0] - alfa[2] / alfa[1] - y_p) / (alfa[1] / alfa[0] + alfa[0] / alfa[1])
        return [x0, - alfa[0] * x0 / alfa[1] - alfa[2] / alfa[1]]


def one_crossing(a, b, x_p, y_p, r): #a, b - arrays of 2 elements, which are coordinates of segment's ends
    '''Return True if segment ab crosses the circle with the center in (x_p, y_p) and radius r, False if not'''
    t = 0
    if ((x_p - a[0]) ** 2 + (y_p - a[1]) ** 2) ** 0.5 <= r:
        t += 1
    if ((x_p - b[0]) ** 2 + (y_p - b[1]) ** 2) ** 0.5 <= r:
        t += 1
    p = projection(x_p, y_p, straight(a, b))
    if p[0] <= max(a[0], b[0]) and p[0] >= min(a[0], b[0]) and p[1] <= max(a[1], b[1]) and p[1] >= min(a[1], b[1]):
        t += 1
    if t == 0:
        return False
    else:
        return True


def crossing(a, x_p, y_p, r): # a - array of arrays, including both coordinates of every polygon vertex
    '''Return true if there are any crossings, no if not'''
    t = 0
    for i in range(len(a)):
        if one_crossing(a[i - 1], a[i], x_p, y_p, r):
            t += 1
    if t == 0:
        return False
    else:
        return True

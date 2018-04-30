# Здесь должен быть реализован класс bullet (кружочки со своими соординатами, радиусом, скоростями по осям и цветом)
# + со своим методом draw (класс можно написать в main)
# роцедура при вызове которой:
# в массиве bullets создается новый объект типа bullet (в случайном месте за экраном,
# летящая по направлению к самолётику)

#Первый залив функции про пересечение многоугольника и снаряда, свисите Руслаше Г. если что поправить

def distance(x_p, y_p, x_l, y_l, c_l):
    '''Return the distance between the point (x_p, y_p) and the line x_l * x + y_l * y + c_l = 0'''
    return (abs(x_l * x_p + y_l * y_p + c_l) / (x_l ** 2 + y_l ** 2) ** 0.5)


def straight(first_point, second_point):
    '''Return A, B, С from straight line Ax + Bx + С = 0 equation, which includes
    points first_point and second_point'''
    if first_point[0] == second_point[0]:
        return [1, 0, -first_point[0]]
    elif first_point[1] == second_point[1]:
        return [0, 1, -first_point[1]]
    else:
        return [second_point[1] - first_point[1], first_point[0] - second_point[0], first_point[1] *
                (second_point[0] - first_point[0]) - first_point[0] * (second_point[1] - first_point[1])]


def projection(x_p, y_p, alfa):
    '''Return coordinates of point M (x_p, y_p) projection onto line alfa'''
    if alfa[0] == 0:
        return [x_p, - alfa[2] / alfa[1]]
    elif alfa[1] == 0:
        return [- alfa[2] / alfa[0], y_p]
    else:
        x0 = (alfa[1] * x_p / alfa[0] - alfa[2] / alfa[1] - y_p) / (alfa[1] / alfa[0] + alfa[0] / alfa[1])
        return [x0, - alfa[0] * x0 / alfa[1] - alfa[2] / alfa[1]]


def one_crossing(first_point, second_point, x_p, y_p, r): #first_point, second_point - arrays of 2 elements, which are coordinates of segment's ends
    '''Return True if segment first_point, second_point crosses the circle with the center in (x_p, y_p)
    and radius r, False if not'''
    st = straight(first_point, second_point)
    if ((x_p - first_point[0]) ** 2 + (y_p - first_point[1]) ** 2) ** 0.5 <= r:
        return True
    if ((x_p - second_point[0]) ** 2 + (y_p - second_point[1]) ** 2) ** 0.5 <= r:
        return True
    p = projection(x_p, y_p, straight(first_point, second_point))
    if p[0] <= max(first_point[0], second_point[0]) and p[0] >= min(first_point[0], second_point[0]) \
            and p[1] <= max(first_point[1], second_point[1]) and p[1] >= min(first_point[1], second_point[1]) \
            and distance(x_p, y_p, st[0], st[1], st[2]) <= r:
        return True
    return False


def crossing(polygon_vertexes, x_p, y_p, r): # polygon_vertexes - array of arrays, including both coordinates of every polygon vertex
    '''Return true if there are any crossings, no if not'''
    for i in range(len(polygon_vertexes)):
        if one_crossing(polygon_vertexes[i - 1], polygon_vertexes[i], x_p, y_p, r):
            return True
    return False
#def check_hitting(bullet):  # Проверка на попадание снаряда в самолётик, возвращает True или False
   # pass

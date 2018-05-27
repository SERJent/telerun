from constants import *
import random

bullet_array = []
speed_counter = 0  # Constant for changing the bullet speed


class bullet():
    '''An object, which has several parameters and can bw drawn'''
    def __init__(self, x, y, v_x, v_y, rad, picture):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.rad = rad
        self.picture = picture

    def draw(self, win):
        win.blit(self.picture, (self.x - bull_w / 2, self.y - bull_w / 2))


def bullet_generator(win, x, y, bullet_picture):
    '''Draws bullets in there current position and draws new ones in necessary'''
    global bullet_array
    global speed_counter
    edge = bull_w / 2

    for shot in bullet_array:
        if (shot.x < -edge) or (shot.x > win_w + edge) or (shot.y < -edge):
            del bullet_array[bullet_array.index(shot)]
        else:
            shot.x = shot.x + shot.v_x
            shot.y = shot.y + shot.v_y

    if speed_counter < 3000:
        bullet_speed = bullet_speed_init + bullet_speed_init * (speed_counter // 500)
    else:
        bullet_speed = bullet_speed_init * 7

    if len(bullet_array) == 0:
        new_born_x = random.randrange(0, win_w, 5)
        new_born_y = win_h + bull_w / 2
        new_born_v_x = bullet_speed * (x - new_born_x) / ((x - new_born_x) ** 2 + (y - new_born_y) ** 2) ** 0.5
        new_born_v_y = bullet_speed * (y - new_born_y) / ((x - new_born_x) ** 2 + (y - new_born_y) ** 2) ** 0.5
        bullet_array.append(bullet(new_born_x, new_born_y, new_born_v_x, new_born_v_y, bull_w / 2, bullet_picture))
    else:
        if bullet_array[-1].y <= win_h - 3 * bull_w:
            new_born_x = random.randrange(0, win_w, 5)
            new_born_y = win_h + bull_w / 2
            new_born_v_x = bullet_speed * (x - new_born_x) / ((x - new_born_x) ** 2 + (y - new_born_y) ** 2) ** 0.5
            new_born_v_y = bullet_speed * (y - new_born_y) / ((x - new_born_x) ** 2 + (y - new_born_y) ** 2) ** 0.5
            bullet_array.append(bullet(new_born_x, new_born_y, new_born_v_x, new_born_v_y, bull_w / 2, bullet_picture))

    for shot in bullet_array:
        shot.draw(win)


def distance(x_p, y_p, x_l, y_l, c_l):
    '''Return the distance between the point (x_p, y_p) and the line x_l * x + y_l * y + c_l = 0'''
    return abs(x_l * x_p + y_l * y_p + c_l) / (x_l ** 2 + y_l ** 2) ** 0.5


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


def one_crossing(first_point, second_point, x_p, y_p, r):
    # first_point, second_point - arrays of 2 elements, which are coordinates of segment's ends
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


def crossing(polygon_vertexes, x_p, y_p, r):
    # polygon_vertexes - array of arrays, including both coordinates of every polygon vertex
    '''Return true if there are any crossings, no if not'''
    for i in range(len(polygon_vertexes)):
        if one_crossing(polygon_vertexes[i - 1], polygon_vertexes[i], x_p, y_p, r):
            return True
    return False



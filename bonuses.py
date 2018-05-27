from constants import *
import random

list_of_bonuses = []
coordinates = []


class bonuses():
    def __init__(self, x, y, v_x, rad, picture):
        self.x = x
        self.y = y
        self.rad = rad
        self.v_x = v_x
        self.picture = picture

    def draw(self, win):
        win.blit(self.picture, (self.x - bonus_w/2, self.y - bonus_w/2))


def bonus_generation(win, game_time, picture):
    global list_of_bonuses, n_ext

    def generation():
        global list_of_bonuses
        x1 = win_w
        y1 = random.randrange(0, win_h - bonus_w)
        v_x = -bonus_speed
        return x1, y1, v_x

    for bonus in list_of_bonuses:
        if bonus.x < -bonus_w:
            del list_of_bonuses[list_of_bonuses.index(bonus)]
        else:
            bonus.x = bonus.x + bonus.v_x

    if (len(list_of_bonuses) == 0) and (game_time > t_ext * n_ext):
        n_ext = n_ext + 1
        gen_x, gen_y, gen_v_x = generation()
        list_of_bonuses.append(bonuses(gen_x, gen_y, gen_v_x, bonus_w, picture))

    for bonus in list_of_bonuses:
        bonus.draw(win)

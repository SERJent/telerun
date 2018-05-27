from constants import *
import random
#import bullets as bul
list_of_bonuses = []
coordinates = []


class bonuses():
    def __init__(self, x, y, v_x, v_y, rad, picture):
        self.x = x
        self.y = y
        self.rad = rad
        self.v_x = v_x
        self.v_y = v_y
        self.picture = picture

    def draw(self, win):
        win.blit(self.picture, (self.x - bonus_w/2, self.y - bonus_w/2))


def bonus_generation(win, x, y, picture):
    global list_of_bonuses, t_cont

    def generation():
        global list_of_bonuses
        x1 = random.randrange(0, win_w, 1)
        y1 = win_h - bonus_w/2
        v_x = bonus_speed * (x - x1) / ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
        v_y = 1.5 * bonus_speed * (y - y1) / ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
        return x1, y1, v_x, v_y

    for bonus in list_of_bonuses:
        if (bonus.x < -bonus_w) or (bonus.x > win_w + bonus_w) or (bonus.y < -bonus_w) or (bonus.y > win_h + bonus_w):
            del list_of_bonuses[list_of_bonuses.index(bonus)]
        else:
            bonus.x = bonus.x + bonus.v_x
            bonus.y = bonus.y + bonus.v_y
    t_cont += 2
    if t_cont >= t_ext:
        t_cont = 0
        if len(list_of_bonuses) == 0 :
            gen_x, gen_y, gen_v_x, gen_v_y = generation()
            list_of_bonuses.append(bonuses(gen_x, gen_y, gen_v_x, gen_v_y, bonus_w, picture))
        else:
            if len(list_of_bonuses) < n_bon:  # можем менять количество бонусов на экране
                gen_x, gen_y, gen_v_x, gen_v_y = generation()
                list_of_bonuses.append(bonuses(gen_x, gen_y, gen_v_x, gen_v_y, bonus_w, picture))
            #for bonus in list_of_bonuses:
            #    coordinates.append([bonus.x, bonus.y])
            #    if bul.crossing(coordinates, (bonus.x + 1), (bonus.y + 1), bonus_w):
            #        bonus.x = (bonus_speed + 3) * (x - bonus.x) / ((x - bonus.x) ** 2 + (y - bonus.y) ** 2) ** 0.5
            #        bonus.y = (bonus_speed + 3) * (y - bonus.x) / ((x - bonus.x) ** 2 + (y - bonus.y) ** 2) ** 0.5
    for bonus in list_of_bonuses:
        bonus.draw(win)
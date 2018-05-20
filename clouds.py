import random
from constants import *

class cloud:
    def __init__(self, x , y, v, png):
        self.x = x
        self.y = y
        self.speed = v
        self.png = png

    def shift(self):#сдвигает облако влево
        self.x -= self.speed

    def draw(self, win):#отрисовывает облако на экране
        win.blit(self.png, (self.x, self.y))

def clouds_init(clouds, clouds_img):#создаёт начальный массив из облаков
    for i in range(cld_n):
        clouds.append(cloud(random.randrange(0, win_w, win_w/10), random.randrange(0, win_h, win_h/10), random.randrange(cld_v-1, cld_v+1), clouds_img[random.randint(0, 3)]))

def clouds_run(win, clouds, clouds_img):#создает новые облака со случайной координатой и удаляет старые, отрисовываея всё на экране
    for cl in clouds:
        if (cl.x + cld_w) > 0:
            cl.shift()
        else:
            del clouds[clouds.index(cl)]
            clouds.append(cloud(win_w, random.randrange(0, win_h, win_h/10), random.randrange(cld_v-1, cld_v+1), clouds_img[random.randint(0, 3)]))
    for cld in clouds:
        cld.draw(win)




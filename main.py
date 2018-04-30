import pygame as pg
from constants import *
import painting as pnt
import clouds as cl
import lives as liv

pg.init()
win = pg.display.set_mode((win_w, win_h))  # Создание самого экрана для отрисовки
pg.display.set_caption("TELERUN")  # Название, которое будет в шапке окна
clock = pg.time.Clock()  # Штуковина для отсчета всяких времён

# Подгружаем всякие картинки для отрисовки -----------------------------------------------------------------------------
font_huge = pg.font.Font('cornerstone.ttf', int(72 * scaling))
font_normal = pg.font.Font('cornerstone.ttf', int(48 * scaling))
font_small = pg.font.Font('cornerstone.ttf', int(36 * scaling))

logo = pg.image.load("logo_tr.png").convert_alpha()  # Подгружаем картинки и изменяем их размер для отрисовки
logo = pg.transform.smoothscale(logo, (int(258 * scaling), int(192 * scaling)))
plane = pg.image.load("plane.png").convert_alpha()
plane = pg.transform.smoothscale(plane, (int(pl_w * scaling), int(pl_h * scaling)))
plane_dmg = pg.image.load("plane_dmg.png").convert_alpha()
plane_dmg = pg.transform.smoothscale(plane_dmg, (int(pl_w * scaling), int(pl_h * scaling)))

rkn = pg.image.load("PKH.png").convert_alpha()  # Снаряды
rkn = pg.transform.smoothscale(rkn, (int(bull_w * scaling), int(bull_w * scaling)))
vpn = pg.image.load("VPN.png").convert_alpha()  # Бонус VPN
vpn = pg.transform.smoothscale(vpn, (int(bonus_w * scaling), int(bonus_w * scaling)))
extr_l = pg.image.load("life.png").convert_alpha()  # Дополнительная жизнь
extr_l = pg.transform.smoothscale(extr_l, (int(bonus_w * scaling), int(bonus_w * scaling)))

cloud_0 = pg.image.load("cloud0.png").convert_alpha()  # Подгружаем картинки облаков и изменяем их размер для отрисовки
cloud_1 = pg.image.load("cloud1.png").convert_alpha()
cloud_2 = pg.image.load("cloud2.png").convert_alpha()
cloud_3 = pg.image.load("cloud3.png").convert_alpha()
cloud0 = pg.transform.smoothscale(cloud_0, (cld_w, cld_h))
cloud1 = pg.transform.smoothscale(cloud_1, (cld_w, cld_h))
cloud2 = pg.transform.smoothscale(cloud_2, (cld_w, cld_h))
cloud3 = pg.transform.smoothscale(cloud_3, (cld_w, cld_h))
# ----------------------------------------------------------------------------------------------------------------------

clouds_img = [cloud0, cloud1, cloud2, cloud3]  # Массив всех возможных форм облачков
clouds = []  # Массив облачков, которые на экране уже бегут

pl_spdx = spd  # Текущие скорости самолётика по осям
pl_spdy = 0

pl_x = midle_x  # Текущие координаты самолётика
pl_y = midle_y

vulnerable = True  # Флаг, показывающий является ли цель уязвимой в данный момент

game_time = 0  # Счётчик текущего времени игры
best_time = 0  # Тут храниться лучшее время за сессию

# Всякие флаги ---------------------------------------------------------------------------------------------------------
crashed = False  # Флаг для проверки закрывания программы
menu = True  # Флаг, показывающий, что игрк находится (не находится) в меню
game_over = False  # Флаг, показывающий, что игрк играет (не играет)
game = False  # Флаг, показывающий, что игрк видит (не видит) окно GAME OVER
# ----------------------------------------------------------------------------------------------------------------------


while not crashed:
    """Основной цикл, внутри которого должна быть написана обработка клавиш и порядок отрисовки для каждого из окон:
    'MENU'
    'GAME'
    'GAME OVER' 
    Также именно тут должен быть реализован счетчик времени и сохранение лучшего результата!"""
    win.fill((255, 255, 255))

    pg.time.delay(delay)
    for event in pg.event.get():  # Проверка на выход из игры
        if event.type == pg.QUIT:
            crashed = True

    pg.display.flip()  # Перерисовка всего экрана

pg.quit()  # Завершение программы
quit()

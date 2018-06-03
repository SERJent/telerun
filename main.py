import pygame as pg
from constants import *
import painting as pnt
import clouds as cl
import lives as liv
import bullets as bul
import bonuses as bon

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

pl_spdx0 = spd
pl_spdy0 = 0
pl_spdx = pl_spdx0  # Текущие скорости самолётика по осям
pl_spdy = pl_spdy0

pl_lives0 = 3
pl_lives = pl_lives0

pl_x = midle_x  # Текущие координаты самолётика
pl_y = midle_y

vulnerable = True  # Флаг, показывающий является ли цель уязвимой в данный момент

game_time = 0  # Счётчик текущего времени игры
best_time = 0  # Тут храниться лучшее время за сессию

counter_cloud = cld_border_shift

# Всякие флаги ---------------------------------------------------------------------------------------------------------
crashed = False  # Флаг для проверки закрывания программы
menu = True  # Флаг, показывающий, что игрк находится (не находится) в меню
game_over = False  # Флаг, показывающий, что игрк играет (не играет)
game = False  # Флаг, показывающий, что игрк видит (не видит) окно GAME OVER
# ----------------------------------------------------------------------------------------------------------------------

def fall(dt, y, spdy, ay):  # Процедура, просчитывающая свободное падение
    y += spdy * dt + ay * dt ** 2 / 2
    spdy += ay * dt
    return y, spdy


while not crashed:
    win.fill((255, 255, 255))
    if cl.clouds_run(win, clouds, clouds_img, counter_cloud):
        counter_cloud = 0
    else:
        counter_cloud += 1
        
    bul.speed_counter += 1

    if menu:
        pg.time.delay(delay)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crashed = True

        pnt.draw_menu(win, font_small, font_normal, font_huge, logo, best_time)  # Рисуем меню
        pg.display.update()
        keys = pg.key.get_pressed()  # Все нажатые кнопки

        if keys[pg.K_RETURN]:  # Новая игра
            pl_x, pl_y, = pl_x0, pl_y0
            pl_spdx, pl_spdy = pl_spdx0, pl_spdy0
            pl_lives = pl_lives0
            menu = False
            game = True
            game_time = 0
            clock.tick()

    if game:
        if pl_lives:
            clock.tick()

            pg.time.delay(delay)
            for event in pg.event.get():  # Проверка на выход из игры
                if event.type == pg.QUIT:
                    crashed = True

            keys = pg.key.get_pressed()  # Все нажатые кнопки

            if keys[pg.K_RIGHT] and (win_w - pl_x >= pl_w + brd):  # Движение вправо
                pl_x += pl_spdx*t

            if keys[pg.K_LEFT] and (pl_x >= brd):  # Движение влево
                pl_x -= pl_spdx*t

            if (not keys[pg.K_DOWN] and not keys[pg.K_UP]) or (keys[pg.K_DOWN] and keys[pg.K_UP]): # Падение
                pl_y, pl_spdy = fall(t, pl_y, pl_spdy, pl_g)

            else:
                if keys[pg.K_UP] and (pl_y > brd):  # Движение вверх
                    pl_y, pl_spdy = fall(t, pl_y, spd_up, pl_g)

                if pl_y < pl_h/2 + brd:   # Выход за границы по высоте
                    pl_spdy = 0

                if keys[pg.K_DOWN]:  # Движение вниз
                    pl_y, pl_spdy = fall(t, pl_y, pl_spdy, a_down)
            if pl_y <= brd:  # Ограничение сверху
                pl_y = brd

            polygon = [[pl_x + 0.21 * pl_w, pl_y + 0.32 * pl_h], [pl_x + 0.19 * pl_w, pl_y],
                             [pl_x + pl_w, pl_y + 0.32 * pl_h], [pl_x + 0.21 * pl_w, pl_y + pl_h],
                             [pl_x + 0.21 * pl_w, pl_y + 0.75 * pl_h], [pl_x, pl_y + 0.85 * pl_h]]
            bul.bullet_generator(win, pl_x + pl_w / 2, pl_y + pl_h / 2, rkn)

            game_time += clock.get_time() / 1000  # Обновление игрового времени
            pnt.print_time(win, font_small, game_time)  # Вывод времени на экран

            pl_lives, vulnerable = liv.check_bonuses(pl_lives, vulnerable, polygon)
            pl_spdy, pl_lives, vulnerable = liv.check_lives(pl_y, pl_spdy, pl_lives, vulnerable, polygon)
            bon.bonus_generation(win, game_time, extr_l)
            pnt.lives_counter(win, font_normal, pl_lives)  # Прорисовка счетчика жизней

            pnt.draw_plane(win, pl_x, pl_y, plane, plane_dmg, vulnerable)
            pg.display.update()  # Перерисовка всего экрана

        else:
            game = False
            game_over = True
            if game_time > best_time:  # Сохранение лучшего времени
                best_time = game_time

    if game_over:
        bul.speed_counter = 0
        bul.bullet_array = []
        bon.list_of_bonuses = []
        pg.time.delay(delay)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crashed = True
        pnt.draw_go(win, font_small, font_normal, font_huge, game_time, best_time)  # Отрисовка game_over
        pg.display.update()

        keys = pg.key.get_pressed()

        if keys[pg.K_RETURN]:  # Новая игра
            pl_x, pl_y, = pl_x0, pl_y0
            pl_spdx, pl_spdy = pl_spdx0, pl_spdy0
            pl_lives = pl_lives0
            game_over = False
            game = True
            game_time = 0
            clock.tick()

        if keys[pg.K_BACKSPACE]:  # Выход в меню
            game_over = False
            menu = True


pg.quit()  # Завершение программы
quit()



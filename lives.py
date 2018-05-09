

# Внутри этой процедуры можно использовать процедуру (даже если она ещё не написана) из bullets.py,
# которая принимает в качестве аргумента объект типа bullet и возвращает True или False в зав-ти
# от того попала пуля в самолётик или же нет.
# P.S. если пуля попала в самолётик, её заодно необходимо удалить из списка bullets
"""Процедура, которая проверяет события, влекущие за собой потерю жизней
    Аргументы:
    y - координата самолётика по оси Y
    pl_spdy - скорость самолётика по оси Y
    lives - переменная, отвечающая за количество жизней
    vulnerable - флаг, показывающий является ли цель уязвимой в данный момент
    bullets - массив объектов  типа bullets (пули, которые в данный момент отрисовываются на экране)"""
from const import *
import bullets


def check_lives(bullets_fb,bullets_or,polygon,y,lives):
    if y > (win_h - brd):
        pl_spdy = -rescue_spd
        lives = lives - 1
    for bull in bullets_fb:
        if bullets.crossing(polygon, bull.x, bull.y, bull.rad):
            lives = lives - 1
            del bullets_fb[bullets_fb.index(bull)]
    for bull in bullets_or:
        if bullets.crossing(polygon, bull.x, bull.y, bull.rad):
            lives = lives - 1
            del bullets_or[bullets_or.index(bull)]
    return pl_spdy, lives

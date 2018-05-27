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
from constants import *
import bullets as bul
import bonuses as bon
def check_lives(y ,pl_spdy ,lives,vulnerable,bullets, polygon):
    global t_vul
    if y > (win_h - brd) and vulnerable:
        pl_spdy = -rescue_spd
        lives = lives - 1
        vulnerable = False
    for bull in bul.bullet_array:
        if bul.crossing(polygon, bull.x, bull.y, bull.rad) and vulnerable:
            lives = lives - 1
            del bul.bullet_array[bul.bullet_array.index(bull)]
            vulnerable = False
    if not vulnerable:
        if y >= win_h:
            pl_spdy = -rescue_spd
        t_vul += t_add
        if t_vul >= invulnerability_t:
            vulnerable = True
            t_vul = 0

    return pl_spdy, lives , vulnerable


def check_bonuses(lives, bonuses, vulnerable, polygon):
    ''''''
    for bonus in bon.list_of_bonuses:
        if bul.crossing(polygon, bonus.x, bonus.y, bonus.rad) and vulnerable:
            lives = lives + 1
            del bon.list_of_bonuses[bon.list_of_bonuses.index(bonus)]
            vulnerable = True
    return lives, vulnerable


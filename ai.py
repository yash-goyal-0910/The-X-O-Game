from cs50 import SQL
import random

db = SQL("sqlite:////workspaces/154236903/x-o_game/game.db")


def t_ai(n):
    pm_n = min_position(point_map(n))
    min_n = min(point_map(n))
    n = 1 - n
    pm_m = min_position(point_map(n))
    min_m = min(point_map(n))

    if min_n < min_m:
        return random.choice(pm_n)

    if min_m < min_n:
        posi_p = list(set(pm_n) & set(pm_m))
        possible = max_posi_p(n)
        posi_p = list(set(posi_p) & set(possible))
        if posi_p == []:
            return random.choice(pm_m)
        if len(posi_p) >= 1:
            return random.choice(posi_p)

    if min_m == min_n:
        possible = max_posi_p(n)
        posi = list(set(possible) & set(pm_n))
        if posi == []:
            return random.choice(possible)
        else:
            return random.choice(posi)


def max_posi_p(n):
    n = 1 - n
    y = 1 - n
    rms_n = rm(n)
    p_max_n = p_max(rms_n)
    m_n = max(p_max_n)
    while True:
        t = 0
        possible = []
        for m in p_max_n:
            t = t + 1
            if m_n == m:
                possible.append(t)
        possible = list((set(possible) - set(filled(n)) - set(filled(y))))
        if len(possible) >= 1:
            break
        m_n = m_n - 1

    return possible


def point_map(a):
    P = []
    F_x = filled(a)
    rms = rm(a)
    a = 1 - a
    F_o = filled(a)
    a = 1 - a
    for n in range(10):
        if n == 0:
            continue
        P.append(p_(n, rms, F_x, F_o))
    return P


def p_(n, rms, F_x, F_o):
    min_i = 100
    if (n in F_x) or (n in F_o):
        return 100
    for p_win in rms:
        if n in p_win:
            i = len(set(p_win) - set(F_x))
            if i < min_i:
                min_i = i
    return min_i


def min_position(M):
    return position(M, min(M))


def min(M):
    P = []
    min = 100
    for a in M:
        if a < min:
            min = a
    return min


def position(M, min):
    p = 0
    P = []
    for a in M:
        p = p + 1
        if a == min:
            P.append(p)
    return P


def filled(n):
    if n == None:
        F = []
        filled = db.execute("SELECT position FROM crnt_game")
        for b in filled:
            F.append(b['position'])
        return F
    if n == 0:
        F = []
        filled = db.execute("SELECT position FROM crnt_game WHERE x_o = 0")
        for b in filled:
            F.append(b['position'])
        return F
    if n == 1:
        F = []
        filled = db.execute("SELECT position FROM crnt_game WHERE x_o = 1")
        for b in filled:
            F.append(b['position'])
        return F


def rm(a):
    a = 1 - a
    F_o = filled(a)
    wins = [[1, 2, 3], [1, 5, 9], [3, 5, 7], [1, 4, 7], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9]]
    rms = []
    for win in wins:
        rm = set(win) - set(F_o)
        if len(rm) == 3:
            rms.append(rm)
    return rms


def p_max(M):
    P = []
    for n in range(10):
        if n == 0:
            continue
        c = 0
        for a in M:
            if n in a:
                c = c + 1
        P.append(c)
    return P

print(t_ai(0))

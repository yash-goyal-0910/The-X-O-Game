from cs50 import SQL
import random
from ai import t_ai
import sys


db = SQL("sqlite:////workspaces/154236903/x-o_game/game.db")


def main():
    start()


def start():
    print("New Game - 1")
    print("Saved game - 2")
    ans(0)


def new_game():
    print("2 player - 1")
    print("With computer - 2")
    print("return to previous menu - 3")
    ans(1)


def ans(n):
    try:
        a = int(input("Choose from above option - "))
    except ValueError:
        print("Select a valid response")
        ans(n)
    if n == 0:
        if a > 2 or a < 1:
            print("try again")
            return ans(n)
        chosen(a)
    if n == 1:
        if a > 3 or a < 1:
            print("try again")
            return a(n)
        a = a + 2
        chosen(a)


def chosen(m):
    print("")
    if m == 1:
        new_game()
    if m == 2:
        saved_game()
    if m == 3:
        n_game()
    if m == 4:
        n2_game()
    if m == 5:
        start()


def map():
    print(p(1), " | ", p(2), " | ", p(3))
    print("---|-----|---")
    print(p(4), " | ", p(5), " | ", p(6))
    print("---|-----|---")
    print(p(7), " | ", p(8), " | ", p(9))


def plan():
    print(1, " | ", 2, " | ", 3)
    print("---|-----|---")
    print(4, " | ", 5, " | ", 6)
    print("---|-----|---")
    print(7, " | ", 8, " | ", 9)


def p(n):
    t = db.execute("SELECT x_o FROM crnt_game WHERE position = ?", n)
    if not t:
        n = ' '
    else:
        value = t[0]['x_o']
        if value == 1:
            n = 'x'
        elif value == 0:
            n = 'o'
    return n


def n_game():
    db.execute("DELETE FROM crnt_game")
    print("This will be position in the game")
    plan()
    print("To Save Game Enter 54")
    n = 1
    for a in range(9):
        t(n)
        n = 1 - n
        if check_win():
            return 0
    print("Game Tied")


def n2_game():
    y = input("choose x or o = ")
    if y == 'x':
        p = 1
    if y == 'o':
        p = 0
    if y == None:
        random.choose(0, 1)
    db.execute("DELETE FROM crnt_game")
    print("This will be position in the game")
    plan()
    n = 1
    for a in range(9):
        if n == p:
            t(n)
        else:
            b = t_ai(n)
            db.execute("INSERT INTO crnt_game (position,x_o) VALUES (?,?)", b, n)
            map()
        n = 1 - n
        if check_win():
            return 0
    print("Game Tied")


def t(n):
    if n == 1:
        x_o = "X"
    if n == 0:
        x_o = "O"
    y = input(f"{x_o} Turn : ")
    if y not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "54"):
        print("Retry")
        t(n)
        return 0
    a = int(y)
    if a == 54:
        save()
        main()
        sys.exit()
    # 1 means x and 0 means o
    F = []
    filled = db.execute("SELECT position FROM crnt_game")
    for b in filled:
        F.append(b['position'])
    if a in F:
        print("ALREADY TAKEN")
        t(n)
        return 0
    db.execute("INSERT INTO crnt_game (position,x_o) VALUES (?,?)", a, n)
    map()


def check_win():
    X = []
    P_x_o = db.execute("SELECT position FROM crnt_game WHERE x_o = 1")
    for a in P_x_o:
        X.append(a['position'])

    Y = []
    P_x_o = db.execute("SELECT position FROM crnt_game WHERE x_o = 0")
    for a in P_x_o:
        Y.append(a['position'])

    win = [[1, 2, 3], [1, 5, 9], [3, 5, 7], [1, 4, 7], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9]]
    for win_condi in win:
        if set(win_condi) <= set(X):
            print("X Won")
            return True
        if set(win_condi) <= set(Y):
            print("O Won")
            return True
    return False


def save():
    game_id = db.execute("SELECT game_id FROM saved_game ORDER BY game_id DESC LIMIT 1")[
        0]['game_id']
    game_id = game_id + 1
    db.execute("INSERT INTO saved_game (game_id) VALUES (?)", game_id)
    X = []
    P_x_o = db.execute("SELECT position FROM crnt_game WHERE x_o = 1")
    for a in P_x_o:
        X.append(a['position'])
    for a in X:
        query = f"UPDATE saved_game SET p{a} = 1 WHERE game_id = ?"
        db.execute(query, game_id)
    Y = []
    P_x_o = db.execute("SELECT position FROM crnt_game WHERE x_o = 0")
    for a in P_x_o:
        Y.append(a['position'])
    for a in Y:
        query = f"UPDATE saved_game SET p{a} = 0 WHERE game_id = ?"
        db.execute(query, game_id)
    print("Game Saved")


def saved_game():
    games = db.execute("SELECT * FROM saved_game ORDER BY game_id DESC")
    for game in games:
        id = game['game_id']
        time = game['time_stamp']
        P = []
        for n in range(10):
            if n == 0:
                continue
            p = game[f'p{n}']
            if p == None:
                p = 3
            P.append(p)
        print(f"id = {id}")
        print(f"time = {time}")
        map_s(P)
    selected = input("Select ID -> ")
    s_game = db.execute("SELECT * FROM saved_game WHERE game_id = ?", selected)
    db.execute("DELETE FROM crnt_game")
    for n in range(10):
        if n == 0:
            continue
        p = s_game[0][f'p{n}']
        if p == 1:
            db.execute("INSERT INTO crnt_game (position,x_o) VALUES (?,1)", n)
        if p == 0:
            db.execute("INSERT INTO crnt_game (position,x_o) VALUES (?,0)", n)
    P = []
    for n in range(10):
        if n == 0:
            continue
        p = s_game[0][f'p{n}']
        if p == None:
            p = 3
        P.append(p)
    n = turn(P)
    map()
    for a in range(9):
        t(n)
        n = 1 - n
        if check_win():
            return 0
    print("Game Tied")


def map_s(P):
    print(p_s(1, P), " | ", p_s(2, P), " | ", p_s(3, P))
    print("---|-----|---")
    print(p_s(4, P), " | ", p_s(5, P), " | ", p_s(6, P))
    print("---|-----|---")
    print(p_s(7, P), " | ", p_s(8, P), " | ", p_s(9, P))


def p_s(n, P):
    t = 0
    for p in P:
        t = t + 1
        if t == n:
            value = p
            if value == 1:
                n = 'x'
            if value == 0:
                n = 'o'
            if value == 3:
                n = ' '
            return n


def turn(P):
    n_x = 0
    n_o = 0
    for p in P:
        if 1 == p:
            n_x = n_x + 1
        if 0 == p:
            n_o = n_o + 1
    if n_x > n_o:
        return 0
    else:
        return 1


main()

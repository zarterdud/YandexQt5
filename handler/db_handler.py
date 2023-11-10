import sqlite3


def login(login, passw, signal):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        signal.emit("Успешная авторизация!")
        cur.close()
        con.close()
        return True
    else:
        signal.emit("Проверьте правильность ввода данных!")
        cur.close()
        con.close()
        return False

    # cur.close()
    # con.close()


def register(login, passw, signal):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    # Регистрируем пользователя
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    # Проверяем на наличие пользователя в базе данных
    if value != []:
        signal.emit("Такой ник уже используется!")
        cur.close()
        con.close()
        return False
    elif value == []:
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{passw}')")
        signal.emit("Вы успешно зарегистрированы!")
        con.commit()
        cur.close()
        con.close()
        return True


def products(name):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    cur.execute(f'SELECT name FROM products WHERE name="{name}";')
    value = cur.fetchall()
    if value != []:
        return value
    else:
        return "Введите корректное\nзначение"


def analogue(name):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    cur.execute(f'SELECT analogue FROM products WHERE name="{name}";')
    value = cur.fetchall()
    if value != []:
        return value
    else:
        return "Не найдено"

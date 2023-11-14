import sqlite3
import difflib
import hashlib
import os


def login(login, passw, signal):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    salt = cur.execute(f'SELECT salt FROM users WHERE name="{login}";').fetchall()
    if salt != []:
        password = cur.execute(
            f'SELECT password FROM users WHERE name="{login}";'
        ).fetchall()
        new_key = hashlib.pbkdf2_hmac(
            "sha1", passw.encode("utf-8"), bytes(salt[0][0], "utf-8"), 100000
        ).hex()

        if new_key != [] and new_key == password[0][0]:
            signal.emit("Успешная авторизация!")
            cur.close()
            con.close()
            return True
        else:
            signal.emit("Проверьте правильность ввода данных!")
            cur.close()
            con.close()
            return False
    else:
        signal.emit("Проверьте правильность ввода данных!")
        return False


def register(login, passw, signal):
    salt = os.urandom(32)
    salt = salt.hex()
    key = hashlib.pbkdf2_hmac(
        "sha1", passw.encode("utf-8"), bytes(salt, "utf-8"), 100000
    ).hex()

    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    # Регистрируем пользователя
    cur.execute(f'SELECT name FROM users WHERE name="{login}";')
    value = cur.fetchall()

    # Проверяем на наличие пользователя в базе данных
    if value != []:
        signal.emit("Такой ник уже используется!")
        cur.close()
        con.close()
        return False
    elif value == []:
        cur.execute(
            f"INSERT INTO users (name, password, salt) VALUES ('{login}', '{key}', '{salt}')"
        )
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
        return "Введите корректно"


def analogue(name):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    cur.execute(f'SELECT analogue FROM products WHERE name="{name}";')
    value = cur.fetchall()
    if value != []:
        return value
    else:
        return "Не найдено"


def check(name):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    cur.execute(f"SELECT name FROM products")
    value = cur.fetchall()
    for i in value:
        y = (
            difflib.SequenceMatcher(None, name.lower(), "".join(*i).lower()).ratio()
            * 100
        )
        if y >= 75:
            return "".join(*i)
    return None


def price(name):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    cur.execute(f"SELECT price_name FROM products WHERE name='{name}'")
    price_name = cur.fetchall()

    cur.execute(f"SELECT price_analogue FROM products WHERE name='{name}'")
    price_analogue = cur.fetchall()

    cur.execute(f"SELECT name FROM products WHERE name='{name}'")
    name_name = cur.fetchall()

    cur.execute(f"SELECT analogue FROM products WHERE name='{name}'")
    name_analogue = cur.fetchall()
    if name != [] and name:
        ans = "".join(*name_name) + ": " + "".join(*price_name) + "руб"
        for i in name_analogue:
            ans += "\n"
            ans += "".join(i) + ": "
            for j in price_analogue:
                ans += "".join(j) + "руб"
        return ans
    else:
        return "Введите коректное значение"


def struck(name):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    cur.execute(f"SELECT structure_name FROM products WHERE name='{name}'")
    struck_name = cur.fetchall()

    cur.execute(f"SELECT structure_analogue FROM products WHERE name='{name}'")
    struck_analogue = cur.fetchall()

    cur.execute(f"SELECT name FROM products WHERE name='{name}'")
    name_name = cur.fetchall()

    cur.execute(f"SELECT analogue FROM products WHERE name='{name}'")
    name_analogue = cur.fetchall()

    ans = "".join(*name_name) + ": " + "".join(*struck_name)
    for i in name_analogue:
        ans += "\n" * 2
        ans += "".join(i) + ": "
        for j in struck_analogue:
            ans += "".join(j)
    return ans


def popular():
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    cur.execute(f"SELECT name, analogue FROM products;")
    value = cur.fetchall()
    ans = ""
    rangee = 1
    for i in value:
        rangee += 1
        ans += i[0] + ": "
        for j in i:
            if j != i[0]:
                ans += j + ", "
        ans += "\n"
        if rangee == 5:
            break

    return ans[:-3]


def add_sth(
    name,
    analogue,
    price_name="",
    price_analogue="",
    structure_name="",
    structure_analogue="",
    picture="",
):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    if name == "" and analogue == "":
        return "Введите название и аналог"
    elif name == "":
        return "Введите название"
    elif analogue == "":
        return "Введите аналог"
    else:
        cur.execute(
            f"INSERT INTO products (name, analogue, price_name, price_analogue, structure_name, structure_analogue, photo) VALUES ('{name}', '{analogue}', '{price_name}', '{price_analogue}', '{structure_name}', '{structure_analogue}', '{picture}');"
        )
        con.commit()


def picture(name):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()
    ans = cur.execute(f"SELECT photo FROM products WHERE name = '{name}';").fetchall()
    if ans != []:
        if ans[0][0] != None:
            return "".join(*ans)
        else:
            return "photos/error.png"
    else:
        return "photos/error.png"

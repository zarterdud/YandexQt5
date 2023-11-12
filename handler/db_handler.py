import sqlite3
import difflib
import hashlib
import os
import hashlib


def login(login, passw, signal):
    con = sqlite3.connect("handler/users.sqlite")
    cur = con.cursor()

    salt = cur.execute(f'SELECT salt FROM users WHERE name="{login}";').fetchall()
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
        if y > 75:
            return "".join(*i)
    return None


def struck(name):
    pass


def price(name):
    pass

import sqlite3
#
# connection = sqlite3.connect('categories.db')
# cursor = connection.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS categories(code VARCHAR(2) PRIMARY KEY,
# title VARCHAR(150))'''
# )
#
# cursor.execute("INSERT INTO categories(code,title)VALUES('FD','Food products')")
# connection.commit()

connection = sqlite3.connect('products.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY,
title VARCHAR(250),
category_code VARCHAR(2),
unit_price FLOAT,
stock_id INTEGER)''')

connection.commit()

connection = sqlite3.connect('store.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS store(store_id INTEGER PRIMARY KEY, title VARCHAR(100))''')

connection.commit()

def display_stores():
    cursor.execute("SELECT * FROM store")
    stores = cursor.fetchall()
    print("Список магазинов из базы данных:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")

def display_products_by_store(store_id):
    cursor.execute("SELECT * FROM products WHERE store_id = ?", (store_id,))
    products = cursor.fetchall()
    for product in products:
        print(f"Название продукта: {product[1]}")
        print(f"Категория: {product[2]}")
        print(f"Цена: {product[3]}")
        print(f"Количество на складе: {product[4]}")
        print()

print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
display_stores()

while True:
    selected_store_id = input("Введите id магазина (или 0 для выхода): ")
    if selected_store_id == '0':
        break

    try:
        selected_store_id = int(selected_store_id)
        if selected_store_id < 0:
            raise ValueError
    except ValueError:
        print("Пожалуйста, введите положительное целое число или 0 для выхода.")
        continue

    cursor.execute("SELECT * FROM store WHERE store_id = ?", (selected_store_id,))
    selected_store = cursor.fetchone()

    if selected_store:
        print(f"Вы выбрали магазин: {selected_store[1]}")
        display_products_by_store(selected_store[0])
    else:
        print("Магазин с таким id не найден. Пожалуйста, выберите существующий id магазина.")

connection.close()
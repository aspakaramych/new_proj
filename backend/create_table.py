#------------Файл для создания sqlite бд---------------------

import sqlite3

db = sqlite3.connect('db/data')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS data_services(
    id INT,
    service TEXT,
    otvets TEXT,
    city TEXT
)""")

db.commit()
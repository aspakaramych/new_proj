#-----------------Файл с функциями для работы с бд----------------
#Импорт библиотек
import sqlite3

#Создание класса бд и курсора
db = sqlite3.connect('./db/data', check_same_thread=False)
sql = db.cursor()

#Функция для записи из excel в бд
def set_xlsx(id, service, otvets, city):
    sql.execute("INSERT INTO data_services VALUES (?, ?, ?, ?)", (id, service, otvets, city))
    db.commit()

#Функция для нахождения всех услуг по таким ключам как введенный запрос пользователя и город
def get_service_by_word_and_city(words, city):
    responses = []
    for id in range(2727):
        sql.execute("SELECT * FROM data_services WHERE id = ?", (id,))
        line = sql.fetchone()
        string = line[1].lower()
        words = words.lower()
        spisok_word = list(words.split())
        flag = True
        for word in spisok_word:
            if word[0:4] not in string:
                flag = False
                break
        if flag and line[3] == city:
            response = {
                "services": line[1],
                "otvets": line[2],
            }
            if response not in responses:
                responses.append(response)
    return responses

#Функция для нахождения всех услуг по такому ключу как город
def get_service_by_only_city(city):
    responses = []
    for id in range(2727):
        sql.execute("SELECT * FROM data_services WHERE id = ?", (id,))
        line = sql.fetchone()
        if line[3] == city:
            response = {
                "services": line[1],
                "otvets": line[2],
            }
            if response not in responses:
                responses.append(response)

    return responses

#Функция для нахождения всех услуг по такому ключу как введенный запрос пользователя
def get_service_by_only_words(words):
    responses = []
    for id in range(2727):
        sql.execute("SELECT * FROM data_services WHERE id = ?", (id,))
        line = sql.fetchone()
        string = line[1].lower()
        words = words.lower()
        spisok_word = list(words.split())
        flag = True
        for word in spisok_word:
            if word[0:4] not in string:
                flag = False
                break
        if flag:
            response = {
                "services": line[1],
                "otvets": line[2],
            }
            if response not in responses:
                responses.append(response)
    return responses


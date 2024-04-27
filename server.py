#--------------Основной файл с api сервером---------------------------

#Импорты библиотек
from flask import Flask, request, Response
from func_db import get_service_by_word_and_city, get_service_by_only_city, get_service_by_only_words
from flask_cors import CORS

app = Flask(__name__) #создание основного класса
CORS(app) #разрешения

@app.route('/', methods=['GET', 'POST'])#основной рут, принимает GET и POST
def main():
    if request.method == 'POST':
        #чтение JSON с клиента
        words = request.json.get("key")
        city = request.json.get("city")

        #условия
        #Если пользователь не введет запрос
        if words == '':
            data = get_service_by_only_city(city)
            data = data[0:6]
            for Id in range(len(data)):
                data[Id]["id"] = Id
            resp = {
                "title": data,
            }
            return resp
        #Если пользователь не введет город
        if city == '':
            data = get_service_by_only_words(city)
            data = data[0:6]
            for Id in range(len(data)):
                data[Id]["id"] = Id
            resp = {
                "title": data,
            }
            return resp
        #Если  все введет
        else:
            data = get_service_by_word_and_city(words, city)
            data = data[0:6]
            for Id in range(len(data)):
                data[Id]["id"] = Id
            resp = {
                "title": data,
            }
            return resp
    #GET запрос при подключении клиента к серверу
    elif request.method == 'GET':
        response = Response(status=200)
        return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)

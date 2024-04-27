#-----------------Файл для обработки данных с excel на sqlite3 --------------------
#Импорты нужных библиотек и функций
import pandas as pd
from func_db import set_xlsx
from Cities import cities

#Путь до excel таблицы
STRING_TO_XLSX = './db/data.xlsx'

#Запись таблицы в переменную и разделение данных
db = pd.read_excel(STRING_TO_XLSX)
serv_str = db['Услуга/функция'].str.split()
adm_str = db['Адм. уровень'].str.split()
otvet_str = db['ответственный огв'].str.split()

#основной цикл обработки, где 2727 строк
for i in range(2727):
    #Создание строки с услугами
    str_a = serv_str[i]
    itog_service = ''
    for j in str_a:
        itog_service += j + ' '
    itog_service = itog_service[0:-1]

    #Создание строки с учреждением
    str_c = otvet_str[i]
    try:
        itog_otvet = ''
        for k in str_c:
            itog_otvet += k + ' '
    except Exception as e:
        itog_otvet = 'ничего'
    itog_otvet = itog_otvet[0:-1]

    #Небольшой алгоритм поиска, в каком городе предоставляется та или иная услуга
    p = ''
    temp_itog_otvet = itog_otvet.lower()
    for city in cities:
        if len(city) == 5:
            y = city[0:4].lower()
        else:
            y = city[0:5].lower()
        if y in temp_itog_otvet:
            p = city
            break
        if "яйск" in temp_itog_otvet:
            p = 'Яя'
            break
        if 'юрги' in temp_itog_otvet:
            p = 'Юрга'
            break
    city = p
    #Запись в бд
    set_xlsx(i, itog_service, itog_otvet, city)


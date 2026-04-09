import os  
import datetime 
import pandas as pd
import socket


id = socket.gethostname() #получаем имя компа
user=os.getlogin()        #получаем имя пользователя


def now_time():
    date = datetime.datetime.now().strftime('%d.%m.%Y')  #сегодняшняя дата
    return date


def sec():
    now_datetime = str(datetime.datetime.now()).split() #время в данный момент
    time = now_datetime[1]
    return time

def log(func):
    def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            data = {
                'id' : [id],    # имя компа
                'pc_username' : [user] ,    # имя пользователя
                'function_name' : [func.__name__],    # имя вызванной функции
                'date' : [now_time()],    # текущая дата
                'time' : [sec()]     # текущее время
            }
            df = pd.DataFrame(data)  # создаем датафрейм из словарика
            
            # сохраняем в цсвшчку
            if os.path.isfile('log.csv'): # если файлик существует
                df.to_csv('log.csv', mode = 'a', index = False, header = False)     #добавляем только строку
            else: 
                df.to_csv('log.csv', index = False) #создаем новый со всеми заголовками


            return res
    return wrapper

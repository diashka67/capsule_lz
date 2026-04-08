import os
import datetime 
import pandas as p
import socket


id = socket.gethostname()
user=os.getlogin()


def now_time():
    date = datetime.datetime.now().strftime('%d.%m.%Y')  #сегодняшняя дата
    return date


def sec():
    now_datetime = str(datetime.datetime.now()).split() #время в данный момент времени
    time = now_datetime[1]
    return time

def log(func):
    def wrapper(*args, **kwargs):
        if os.path.isfile('log.csv'):
            file_df = p.read_csv('logs.csv')
            data = {
                'id' : [id],
                'pc_username' : [user] ,
                'function_name' : [func.__name__],
                'date' : [now_time],
                'time' : [sec]
            }
            df = p.DataFrame(data)
            df.to_csv('log.csv', mode='a', index = False, header = False)

        else: 
            data = {
                'id' : [id],
                'pc_username' : [user] ,
                'function_name' : [func.__name__],
                'date' : [now_time],
                'time' : [sec]
            }
            df.to_csv('logs.csv')
            df = p.DataFrame(data)
            res = func(*args, **kwargs)
            return res
        return wrapper


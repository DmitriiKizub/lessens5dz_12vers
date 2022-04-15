# просмотр содержимого рабочей директории

import os
# вывод всех объектов в рабочей папке;
def show_dir_all():

    i = None
    print("________________________")
    for i in os.listdir():
        print(i)
    print("________________________")

# Вывод только папок каталога
def show_dir():
    dir = os.getcwd()
    print("________________________")
    for i in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, i)):
            print(i)
    print("________________________")
# Вывод только файлы каталога
def show_file():
    file = os.getcwd()
    print("________________________")
    for i in os.listdir():
        if os.path.isfile(os.path.join(file, i)):
            print(i)
    print("________________________")

def info_os():
    info = [os.name, os.getlogin()]
    for i in info:
        print(i)

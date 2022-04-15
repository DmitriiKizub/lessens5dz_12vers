import shutil
import os
def copy_direct():

    name_direct = input("Введите название папки\файла для копирования: ")
    new_name_direct = input('Введите новое название папки\файла: ')
    if os.path.isfile(name_direct):
        shutil.copy(name_direct, new_name_direct)
    elif os.path.isdir(name_direct):
        shutil.copytree(name_direct,new_name_direct)
    else:
        print('что то пошло не так')

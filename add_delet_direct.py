# Содание паки
import os
import shutil

print("Текущая деректория: ", os.getcwd())
def new_direct():
    name_direct = input("Введите название новой папки: ")
    if not os.path.isdir(name_direct):
        os.mkdir(name_direct)

    else:
        print("\nДанная папка уже создана\n")

def new_file():
    name_direct =input("Введите название файла: ")
    if not os.path.isfile(name_direct):
        file = open(name_direct, 'w')


def del_direct():
    name_direct = input("Введите название папки\файла для удаления: ")
    if os.path.isdir(name_direct):
        shutil.rmtree(name_direct)

    elif os.path.isfile(name_direct):
        os.remove(name_direct)
    else:
        print('\nПапки с таким именем нет\n')


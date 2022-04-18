# Смена рабочей директории
import os
def select_dir():
    direct = input("Введите путь к директории: ")
    os.chdir(direct)
    print(f'Вы перешли в каталог: {os.getcwd()}')
    i = None
    print("Файлы в каталоге:\n________________________")
    for i in os.listdir():
        print(i)
    print("________________________")

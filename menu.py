# Создание папки
menu_push = None
while menu_push != '12':
    menu = ['1.Создать папку', '2.Удалить (файл\папку)', '3.Копировать(файл\папку)',
            '4.просмотр содержимого рабочей директории', '5.посмотреть только папки', '6.посмотреть только файлы',
            '7.просмотр информации об операционной системе', '8.создатель программы', '9.играть в викторину',
            '10.мой банковский счет', '11.смена рабочей директории', '12.выход']
    for i in menu:
        print(i)
    menu_push = input('Выберете пункт меню: ')
    # Создание папки
    if menu_push == "1":
        from add_delet_direct import new_direct

        new_direct()
        question = input('Хотите создать файл? Да\Нет ')

        if question.upper() == "ДА":
            from add_delet_direct import new_file
            new_file()
    # Уделание файла или папку
    elif menu_push == '2':
        from add_delet_direct import del_direct

        del_direct()
    # Копирование файла или папку
    elif menu_push == '3':
        from copy_direct import copy_direct
        copy_direct()
    # Просмотр всего содержимого папки
    elif menu_push == '4':
        from show_work_direct import show_dir_all
        show_dir_all()
    # Просмотр только папок
    elif menu_push == '5':
        from show_work_direct import show_dir
        show_dir()
    # Просмотр только файлов
    elif menu_push == '6':
        from show_work_direct import show_file
        show_file()
    elif menu_push == '7':
        from show_work_direct import info_os
        info_os()
    elif menu_push == '8':
        print("Создаитель программы: Кизуб Дмитрий Анатольевич")

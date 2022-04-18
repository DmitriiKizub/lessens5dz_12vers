def vicro():
    import random
    import datetime
    # Билл Гейтс 28.10.1955.г
    year_billGeitc = '28.10.1955'
    # Джон Рокфеллер 08.07.1839 г
    year_DjonRok = '08.07.1839'
    # Эндрю Карнеги 28.11.1835 г
    year_Karnegi = '28.11.1835'
    # Генри Форд 30.07.1863 г
    year_Ford = '30.07.1863'
    # Марк Цууенберг 14.05.1984 г
    year_Cukenberg = '14.05.1984'
    spisok_list = {'Билл Гейтс ': 'Двадцать восьмое Октября 1955.г',
                   'Джон Рокфеллер': 'Восьмое Июля 1839.г',
                   'Эндрю Карнеги': 'Двадцать восьмое Ноября 1835.г',
                   'Генри Форд': 'Тридцатое Июля 1863.г',
                   'Марк Цууенберг': 'Четырнадцатое Мая 1984.г'}

    spisok_sprav = {'Билл Гейтс ': year_billGeitc,
                    'Джон Рокфеллер': year_DjonRok,
                    'Эндрю Карнеги': year_Karnegi,
                    'Генри Форд': year_Ford,
                    'Марк Цууенберг': year_Cukenberg}

    spisok = ['Билл Гейтс ', 'Джон Рокфеллер', 'Эндрю Карнеги', 'Генри Форд', 'Марк Цууенберг']
    newtest = "Да"

    while newtest.upper() == 'ДА':
        result = random.sample(spisok, 5)
        chetchik = 0
        for i in result:
            print(i)
        input_date = list()
        for i in range(len(spisok)):
            date = input(f'Введите дату рождения {result[i]}: ')
            input_date.append(date)
            for key, val in spisok_sprav.items():
                if val == input_date[i] and key == result[i]:
                    for key, val in spisok_list.items():
                        if key == result[i]:
                            print(val)

                else:
                    if key == result[i]:
                        print(f'Верная дата:  {result[i]} {val} ')
                        chetchik += 1
        print(f'Кол-во верных ответов: {len(spisok) - chetchik}')
        print(f'Кол-во не правильных ответов: {chetchik}')

        newtest = input("Хотите пройти тест заново? Да\Нет")

    print("End")

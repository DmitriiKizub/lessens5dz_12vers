# Основное меню
def my_chek():
    # Сумма средств хранящаяся на счете
    account_sum = []

    def account(x):

        # Если покупка, то выполняем действие
        if x < 0:
            result = sum(account_sum) + x
            account_sum.clear()
            return account_sum.append(result)
        # Если пополнение, то выполняем действие
        else:
            account_sum.append(x)
            print(sum(account_sum))
            return sum(account_sum)

    # Список "словарь" с покупками
    purchase_spr = {}

    # Основное меню
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            x = int(input("Введите сумму пополнения: "))
            account(x)
            pass
        elif choice == '2':

            purchase_sum = int(input('Введите сумму покупки:'))

            if account(0) < purchase_sum:
                print('На Вашем счете недостаточно средств')
            else:
                purchase_name = str(input('Введите название продукта: '))
                purchase_spr[purchase_name] = purchase_sum
                account(purchase_sum * -1)
            pass
        elif choice == '3':
            i = 0
            for k, v in purchase_spr.items():
                print(f'Продукт покупки: {k} --Стоимость: {v}')

            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
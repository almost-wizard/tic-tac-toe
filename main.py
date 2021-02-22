table_size = 3                                           # Устанавливаем размер таблицы
table = [[""] * table_size for _ in range(table_size)]  # Генерируем пустую таблицу с установленным размером
user_assistance_table = [                                # Создаем таблицу используемую в функции user_assistance()
    [""] * 3,
    [""] * 3,
    ["", "X", ""]
]
count = 0                                                # Заводим счетчик ходов

print('''
ИГРА Крестики-нолики

Для вывода инструкций напишите "help"
Для выхода из игры напишите "exit"

Поехали!
''')


def print_table(array, size=3):     # Функция, рисующая таблицу с использованием символов Unicode
    print("\u250F" + ("\u2501" * 3 + "\u2533") * size + "\u2501" * 3 + "\u2513")
    print("\u2503   ", end="")
    [print(f"\u2503 {i} ", end="") for i in range(size)]
    print("\u2503")
    print("\u2523" + ("\u2501" * 3 + "\u254B") * size + "\u2501" * 3 + "\u252B")
    for row in range(size):
        print(f"\u2503 {row} \u2503", end="")
        for column in range(size):
            print(f" {array[row][column] or ' '} \u2503", end="")
        print()
        [
            print("\u2517" + ("\u2501" * 3 + "\u253B") * size + "\u2501" * 3 + "\u251B")
        ] if row == size - 1 else print("\u2523" + ("\u2501" * 3 + "\u254B") * size + "\u2501" * 3 + "\u252B")


def user_assistance(array):      # Инструкция к игре, вызываемая пользователем произвольно
    print("Помощь к игре\n")
    print("Крестики-нолики - логическая игра между двумя противниками на квадратном поле размнром 3х3 или больше")
    print("Один из игроков играет «крестиками», второй — «ноликами»\n")
    print("Правила\n")
    print("Игроки по очереди ставят на свободные клетки поля знаки (один всегда крестики, другой всегда нолики)")
    print("Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.")
    print("Первый ход делает игрок, ставящий крестики.\n")
    print("Как 'ходить'?\n")
    print("Перед игроком предстает поле, каждая колонка и столбец которого имеют свой порядковый номер (0, 1, 2...)")
    print("Игрок, которому нужно 'походить', вводит 2 координаты конечной клетки. Первая координата означает строку,")
    print("на которую мы идем, вторая - столбец.\n")
    print("Пример ввода:\n")
    print("Ходит крестик")
    print("1 2\n")
    print("Пример вывода:\n")
    print_table(array)
    print("\nИтак, попробуем еще раз!\n")


def check_input_data(xy_cords, array, size=3):      # Функция, проверяющая входные данные пользователя
    if len(xy_cords) != 2:
        print("Введите 2 координаты!")
        return False
    x_c, y_c = xy_cords
    if not (x_c.isdigit() and y_c.isdigit()):
        print("Введите 2 целых числа!")
        return False
    elif not (0 <= int(x_c) <= size - 1 and 0 <= int(y_c) <= size - 1):
        print("Введите 2 правильных координаты!")
        return False
    elif array[int(y_c)][int(x_c)] != "":
        print("Клетка занята!")
        return False
    return True


def is_win(array, size=3):      # Функция, определяющая, нет ли победителей
    win_t, win_t1, win_t2, win_t3 = [], [], [], [[], []]
    for row in range(size):
        win_t1.append([])
        win_t2.append([])
        for column in range(size):
            win_t1[row].append(tuple([column, row]))
            win_t2[row].append(tuple([row, column]))
            if row == column:
                win_t3[0].append(tuple([row, column]))
            if row + column == size - 1:
                win_t3[1].append(tuple([row, column]))
    win_t.extend(win_t1)
    win_t.extend(win_t2)
    win_t.extend(win_t3)
    for win_cords in win_t:
        check = []
        for cord in win_cords:
            check.append(array[cord[0]][cord[1]])
            if check == ["X"] * size:
                return "Победил крестик! Поздравляем! :D"
            elif check == ["O"] * size:
                return "Победил нолик! Поздравляем! :D"
    return False


def main(array, size, num):       # Главный игровой цикл
    while True:
        print_table(array, size)

        if is_win(array, size):
            print(is_win(array, size))
            break
        elif num == size ** 2:
            print("Ничья. Силы оказались равны :O")
            break

        if num % 2 == 0:
            print("Ходит крестик")
        else:
            print("Ходит нолик")

        string = None
        while not string:
            string = input()

        if string == "help":
            user_assistance(user_assistance_table)
            continue
        elif string == "exit":
            print("Игра окончена")
            break

        cords = string.split()

        if check_input_data(cords, array, size):
            x, y = cords
            if num % 2 == 0:
                array[int(y)][int(x)] = "X"
            else:
                array[int(y)][int(x)] = "O"
            num += 1


main(table, table_size, count)      # Запускаем игру

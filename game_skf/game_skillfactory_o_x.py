map = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
def output_map(map):
# Функция релизации карты через цикл
    print(' ', 0, 1, 2, sep=' ')
    for i in range(len(map)):
        for j in range(len(map[i])):
            if j == 0:
                print(i, end=' ')
            print(map[i][j], end=' ')
        print()

def check_wins(board, step):
    # Функция проверки на победу, где будут проверяться равенства по диагонали, строке и столбцу
    return any([
        [step] * 3 == [row[i] for i, row in enumerate(map)],
        [step] * 3 in map,
        (step,) * 3 in list(zip(*map)),
        [step] * 3 == [row[i] for i, row in enumerate(map[::-1])]
    ]) or False

def check_data(map, step, number_player):
    # проверка на корректность ввода данных

    while True:
        print('\033[36m' + f"\nИгрок {number_player} ваш ход")
        print('\033[39m')  # сброс к цвету по умолчанию

        col_number = input("Введите номер столбца: ")
        if col_number not in ('0', '1', '2'):
            print('\033[31m' + "Проверьте корректность ввода. Нумерация столбцов 0-2")
            print('\033[39m')  # сброс к цвету по умолчанию
            output_map(map)
            continue
        row_number = input("Введите номер строчки: ")
        if row_number not in ('0', '1', '2'):
            print('\033[31m' + "Проверьте корректность ввода. Нумерация строчек 0-2")
            print('\033[39m')  # сброс к цвету по умолчанию
            output_map(map)
            continue
        row_number = int(row_number)
        col_number = int(col_number)
        if map[row_number][col_number] not in ('X', '0'):
            map[row_number][col_number] = step
            output_map(map)
            return check_wins(map, step)
        else:
            print("Ячейка занята!")
            output_map(map)

def core_game():
# Ядро игры, где подключены все функции для стабильной работы игры
    print('\033[36m' + 'Добро пожаловать в игру крестики-нолики')
    print('\033[36m' + 'в игре может участвовать только 2 игрока!')
    print('\033[39m')  # сброс к цвету по умолчанию
    output_map(map)
    max_items= 9
    for i in range(max_items):
        if i % 2 == 0:
            number_player = 1
            step = 'X'
        else:
            number_player = 2
            step = '0'
        if check_data(map, step, number_player):
            print('\033[32m' + f"Игрок {number_player} победил!")
            print('\033[39m')  # сброс к цвету по умолчанию
            break
        if i == max_items - 1:
            print('\033[32m' + "Ничья!")
            print('\033[39m')  # сброс к цвету по умолчанию
core_game()









# Tic-Tac-Toe game
def check_input(number):  # Проверка корректности ввода
    if number in range(1, 4):
        return True
    else:
        print("Введено некорректное число")
        return False


def matrix_output(list):  # Вывод матрицы
    print(' '.join([str(i) for i in list]))


def check_win_by_diagonal():  # Проверка победы по диагоналям
    check_line = data[2]
    if check_line[2] == player:
        # Проверка левой диагонали
        check_line = data[1]
        if check_line[1] == player:
            check_line = data[3]
            if check_line[3] == player:
                return True
        # Проверка правой дигонали
        check_line = data[1]
        if check_line[3] == player:
            check_line = data[3]
            if check_line[1] == player:
                return True


def check_win_by_lines(list_item):  # Проверка победы по линиям
    if player == list_item:
        return True


def turn(player, line=0, row=0):  # Выполнение хода
    t_line = data[line]
    t_line[row] = player
    check_line = list(filter(check_win_by_lines, t_line))
    transp_data = list(map(list, zip(*data)))
    t_row = transp_data[row]
    check_row = list(filter(check_win_by_lines, t_row))
    if len(check_line) == 3 or len(check_row) == 3:
        return True
    if check_win_by_diagonal():
        return True


# Начальные установки
end_game = False
player = 'O'
data = [[i + j for i in range(0, 4)] for j in range(0, 4)]
for line_number in range(0, 4):
    line = data[line_number]
    if line_number > 0:
        for row_number in range(1, 4):
            line[row_number] = '-'
    matrix_output(data[line_number])  # Вывод первоначальной матрицы
# Ход игры
while not end_game:
    if player == 'O':
        player = 'X'
    else:
        player = 'O'
    print("Сейчас ходят", player)
    line_number = int(input("Введите номер строки: "))
    row_number = int(input("Введите номер столбца: "))
    if turn(player, line_number, row_number):
        end_game = True
        print("Победили", player)

    for line_number in range(0, 4):  # Вывод матрицы с учётом ходов
        line = data[line_number]
        matrix_output(data[line_number])

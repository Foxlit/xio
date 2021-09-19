# Tic-Tac-Toe game
def check_input(number):
    if 1 > number > 4:
        print("Введено некорректное число")
        return False
    else:
        return True


data = [[i + j for i in range(0, 4)] for j in range(0, 4)]
print(data)
for line_number in range(0, 4):
    line = data[line_number]
    if line_number > 0:
        for row_number in range(1, 4):
            line[row_number] = '-'
    print(data[line_number])

line_number_X = int(input("Игрок X, введите номер строки: "))
print(check_input(line_number_X))
row_number_X = int(input("Игрок X, введите номер столбца: "))
print(check_input(row_number_X))
line_number_O = int(input("Игрок O, введите номер строки: "))
print(check_input(line_number_O))
row_number_O = int(input("Игрок O, введите номер столбца: "))
print(check_input(row_number_O))





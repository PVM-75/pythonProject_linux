def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    # print(operand_1, operation, operand_2)
    '''if operation == "+":
        print(f'Результат: {operand_1 + operand_2}')
    if operation == "-":
        print(f'Результат: {operand_1 - operand_2}')
    if operation == "*":
        print(f'Результат: {operand_1 * operand_2}')
    if operation == "/":
        print(f'Результат: {operand_1 / operand_2}')
    if operation == "//":
        print(f'Результат: {operand_1 // operand_2}')
    if operation == "%":
        print(f'Результат: {operand_1 % operand_2}')'''

if __name__ == '__main__':
    cnt = 0
    with open('data.txt', 'r') as file:
        for line in file:
            cnt += 1
            try:
                calc(line)
            except ValueError as exc:
                if 'unpack' in exc.args[0]:
                    print(f'Ошибка в строке: {cnt}, не хватает данных для операции')
                else:
                    print(f'Ошибка в строке: {cnt}, нельзя перевести в число')
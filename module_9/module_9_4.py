first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for item in data_set:
                if isinstance(item, list):
                    file.write(str(item) + '\n')  # Преобразование списка в строку
                else:
                    file.write(str(item) + '\n')  # Преобразование элемента в строку
    return write_everything

write_ = get_advanced_writer('example.txt')
write_('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice

class MysticBall:
    def __init__(self, *args):
        self.ball_list = []
        for item in args:
            self.ball_list.append(item)

    def __call__(self):
        return choice(self.ball_list)

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())
from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__(name=name)
        # self.name = name
        self.power = power

    def run(self):
        opponents = 100
        days_num = 0
        print(f'{self.name}, на нас напали!')
        while opponents > 0:
            opponents -= self.power
            days_num += 1
            sleep(1)
            print(f'{self.name} сражается {days_num} день(дня)..., осталось {opponents} воинов.')
        print(f'{self.name} одержал победу спустя {days_num} дней(дня)!')


if __name__ == '__main__':
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    # Запуск потоков и остановка текущего
    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()
    print(f'Все битвы закончились!')
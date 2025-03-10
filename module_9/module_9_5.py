class Iterator:
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError
        else:
            self.step = step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0:
            if self.pointer <= self.stop:
                self.output = self.pointer
                self.pointer += self.step
                return self.output
            else:
                raise StopIteration()
        if self.step < 0:
            if self.pointer >= self.stop:
                self.output = self.pointer
                self.pointer += self.step
                return self.output
            else:
                raise StopIteration()


class StepValueError(ValueError):
    pass

if __name__ == '__main__':
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('Шаг указан неверно')

    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1) # В консоль ничего не выводится

    for i in iter2:
        print(i, end=' ')
    print()
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()

    # Вывод на консоль:
    # Шаг указан неверно
    # -5 - 4 - 3 - 2 - 1 0 1
    # 6 8 10 12 14
    # 5 4 3 2 1
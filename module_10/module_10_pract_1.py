# практика из видео в телеграмме
# 8-924-353-01-94 сестра Валя
# 8-902-531-29-54 сестра Таня
import time
import requests
from multiprocessing import Process, Pool


def activity():
    result = 0
    for e in range(1000000):
        result += abs(round(e ** 2 / 122) + e * 3.14)
    print(result)
    # requests.get('https://ya.ru')
    # print('OK')

def run(parallel=False):
    start = time.time()
    if not parallel:
        for e in range(10):
            activity()
    else:
        processes = [Process(target=activity, daemon=True) for _ in range(10)]
        for e in processes:
            e.start()
        for e in processes:
            e.join()
    end = time.time()
    print(f'Time: {end - start} seconds')

def work():
    arr = list(range(1000000))
    step = len(arr) // 10
    position = 0
    processes = []
    for _ in range(10):
        split = arr[position:position + step]
        processes.append(Process(target=calc_sum_print, args=(split, ), daemon=True))
        position += step
    start = time.time()
    for e in processes:
        e.start()
    for e in processes:
        e.join()
    end = time.time()
    print(f'Time: {end - start} second.')

def work_pool():
    arr = list(range(1000000))
    step = len(arr) // 10
    start = time.time()
    with Pool(10) as pool:
        result = pool.map(calc_sum, [arr[position:position + step] for position in range(0, len(arr), step)])
        print(result)
    end = time.time()
    print(f'Time: {end - start} second.')

def calc_sum(a_list: list):
    return sum(a_list)

def calc_sum_print(a_list: list):
    print(sum(a_list))

if __name__ == '__main__':
    # run(parallel=True) # При выборе False - без многопроцеесора, при выборе True - с многопроцем
    # work()
    work_pool()
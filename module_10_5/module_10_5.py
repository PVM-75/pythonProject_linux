import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(file=name, mode='r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    # start_time = time.time()
    # for filename in filenames:
    #     data = read_info(filename)
    # end_time = time.time()
    # print(f"Линейное выполнение заняло: {end_time - start_time:.4f} секунд.")

    start_time = time.time()
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессное выполнение заняло: {end_time - start_time:.4f} секунд.")
import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
    result_item = count(x)
    print('item ' + str(x) + ' result ' + str(result_item))


def count(num):
    for i in range(0, 10000000):
        i = i + 1
    return i * num


if __name__ == '__main__':
    start_time = time.clock()
    for item in number_list:
        evaluate_item(item)
    print('线性执行 耗时' + str(time.clock() - start_time), ' seconds')

    start_time_1 = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print('线程池 耗时' + str(time.clock() - start_time_1), ' seconds')

    start_time_2 = time.clock()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print('进程池 耗时' + str(time.clock() - start_time_2), ' seconds')

import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print('Starting {}......'.format(name))
    time.sleep(3)
    print('Existing:{}'.format(name))


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='foo_process', target=foo)
    process_with_name.daemon = True

    process_with_default_name = multiprocessing.Process(target=foo)

    process_with_name.start()
    process_with_default_name.start()
    # process_jobs = []
    # for i in range(5):
    #     p = multiprocessing.Process(target=foo, name='foo_process')
    #     process_jobs.append(p)
    # [job.start() for job in process_jobs]
    # [job.join() for job in process_jobs]

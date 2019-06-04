import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait


def get_html(url):
    time.sleep(url)
    print("task pass {}s".format(url))
    return url


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3)
    # task1 = executor.submit(get_html, (3))
    # task2 = executor.submit(get_html, (2))
    # print(task1.result())
    # print(task2.result())
    # print(task1.done())
    urls = [3, 2, 4]
    start_time = time.time()
    all_task = [executor.submit(get_html, (url)) for url in urls]
    for future in as_completed(all_task):
        data = future.result()
        print("thread return {}".format(data))
    wait(all_task)
    end_time = time.time()
    print("passed time {}".format(end_time-start_time))


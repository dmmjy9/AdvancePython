import time
import multiprocessing


def get_html(n):
    time.sleep(n)
    print("sub process success")
    return n


if __name__ == '__main__':
    # process = multiprocessing.Process(target=get_html, args=(2,))
    # process.start()
    # process.join()
    # print("main process end")
    pool = multiprocessing.Pool(3)
    # result = pool.apply_async(get_html, args=(3,))
    # pool.close()
    # pool.join()
    # print(result.get())
    for result in pool.imap(get_html, [1, 5, 3]):
        print(result)
    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print(result)
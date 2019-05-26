import time
import threading
from queue import Queue


def get_detail_html(queue):
    while True:
        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("{}".format(url))
        print("get detail html end")


def get_detail_url(queue):
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_detail_url.start()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    start_time = time.time()

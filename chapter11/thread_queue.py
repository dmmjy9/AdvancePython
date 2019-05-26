import threading
import time

from chapter11 import variables


def get_detail_html():
    detail_url_list = variables.detail_url_list
    while True:
        if len(variables.detail_url_list):
            url = detail_url_list.pop()
            print("get detail html started, {}".format(url))
            time.sleep(2)
            print("get detail html end")


def get_detail_url(detail_url_list):
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url,
                                         args=(variables.detail_url_list,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()

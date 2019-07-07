import socket
import time
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


selector = DefaultSelector()
urls = []
stop = False


class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHOST:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf-8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == "":
            self.path = "/"
        self.data = b""

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass

        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == '__main__':
    start_time = time.time()
    for i in range(20):
        url = "https://www.baidu.com"
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print("running time: {}".format(time.time() - start_time))

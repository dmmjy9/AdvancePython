from multiprocessing import Pipe, Process


def producer(pipe):
    pipe.send("send test")


def consumer(pipe):
    print(pipe.recv())


if __name__ == '__main__':
    recv_pipe, send_pipe = Pipe()
    my_producer = Process(target=producer, args=(send_pipe,))
    my_consumer = Process(target=consumer, args=(recv_pipe,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

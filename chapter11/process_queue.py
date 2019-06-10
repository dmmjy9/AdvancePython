import time
from multiprocessing import Process, Pool, Manager

def producer(queue):
    queue.put("a")
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == '__main__':
    queue = Manager().Queue(10)
    pool = Pool(2)
    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))
    # my_producer = Process(target=producer, args=(a,))
    # my_consumer = Process(target=consumer, args=(a,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()
    pool.close()
    pool.join()
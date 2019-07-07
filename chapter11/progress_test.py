def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from concurrent.futures import ProcessPoolExecutor
    import time
    start_time = time.time()
    with ProcessPoolExecutor(8) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
        for future in as_completed(all_task):
            data = future.result()
            print(data)
    print("last time is: {}".format(time.time()-start_time))

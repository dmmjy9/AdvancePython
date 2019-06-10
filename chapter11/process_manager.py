from multiprocessing import Manager, Process


def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == '__main__':
    process_dict = Manager().dict()
    first_process = Process(target=add_data, args=(process_dict, "test1", 22))
    second_process = Process(target=add_data, args=(process_dict, "test2", 23))
    first_process.start()
    second_process.start()
    first_process.join()
    second_process.join()
    print(process_dict)

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    def __getitem__(self, item):
        return self.employee[item]


class MyIterator:
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    company = Company(["tom", "bob", "jane"])
    for item in company:
        print(item)

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __str__(self):
        return ",".join(self.employee)


company = Company(["tom", "bob", "jane"])
company1 = company[:2]

employee = company.employee
# for em in company:
#     print(em)
# print(len(company1))
# print(company)

class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_instance):
        re_vector = MyVector(self.x+other_instance.x, self.y+other_instance.y)
        return re_vector

    def __str__(self):
        return "x:{x}, y:{y}".format(x=self.x, y=self.y)


first_vec = MyVector(1, 2)
second_vec = MyVector(2, 3)
print(first_vec+second_vec)

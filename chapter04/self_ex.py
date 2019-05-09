from class_method import Date

class Person:
    """
    Person Doc
    """
    name = "user"

class Stu(Person):
    def __init__(self, school_name):
        self.school_name = ""

if __name__ == '__main__':
    user = Stu("imooc")
    print(user.__dict__)
    print(Person.__dict__)

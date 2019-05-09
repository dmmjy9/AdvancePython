from class_method import Date

class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2019 - self.__birthday.year

class Stu(User):
    def __init__(self, birthday):
        self.__birthday = birthday

if __name__ == '__main__':
    user = User(Date(1990, 2, 1))
    user1 = Stu(Date(1994, 8, 30))
    print(user.get_age())
    print(user._User__birthday)
    print(user1._Stu__birthday)

class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y
a = A(2, 3)
print(a.x, a.y, a.aa)
print(A.aa)

A.aa = 11
a.aa = 100
print(A.aa, a.aa)

class Matrix:
    def __init__(self, list1):
        self.listt = list1.copy()

    def __str__(self):
        return '\n'.join(str(self.listt))


m = Matrix([[1, 2, 3], [4, 5, 6]])
# print(m.__dict__)
print(m)

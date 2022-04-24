import re


def findName(a1):
    if re.fullmatch(r"(?:\w+\W+){2}.*", a1):
        line = re.findall(r"\w+", a1)
        return line[1]


a = 'Привет, Дима!'
b = 'Привет, Аня!!'
c = 'Привет, Mike.'
d = 'Привет, Олег. Как дела?'
print(findName(a))
print(findName(b))
print(findName(c))
print(findName(d))

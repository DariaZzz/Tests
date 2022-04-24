import re


class Site:
    urlstring = ''
    __mainDict = {}

    def __init__(self, d):
        self.urlstring = d
        self.__tupleURL = ()

    def __print1(self):
        for word in self.__mainDict[self.urlstring]:
            name = self.__mainDict[self.urlstring][word]
            print(f'lvl {abs(int(word))}: ', name)

    def __domain_helper(self):
        line = (re.findall(r'\w+', self.urlstring))[2::]
        tup = self.__tupleURL = tuple(enumerate(line, -len(line)))
        url = self.urlstring
        self.__mainDict[url] = {}
        for i in range(len(tup) - 1, -1, -1):
            number = abs(int(tup[i][0]))
            name = tup[i][1]
            self.__mainDict[url][number] = name

    def __check(self):
        if self.urlstring not in self.__mainDict:
            print('domain ')
            self.__domain_helper()

    @property
    def domain(self):
        self.__check()
        return self.__print1()

    def domain_lvl(self, number):
        self.__check()
        return f'lvl {number}: {self.__mainDict[self.urlstring][number]}\n'


im = Site('https://www.vk.messages.video.google.com/')
new = Site('https://www.vk.messages.com/')
print(im.domain)
print(im.domain)
print(new.domain_lvl(3))

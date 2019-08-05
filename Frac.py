class Frac():
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
    def getNum(self):
        return self.__num
    def setNum(self, num):
        self.__num = num
    def getDen(self):
        return self.__den
    def setDen(self, den):
        self.__den = den
    def show(self):
        print(self.__num, '/', self.__den)
    def mult (self, num, den):
        self.__num = self.__num * num
        self.__den = self.__den * den
    def div (self, num, den):
        self.__num = self.__num * den
        self.__den = self.__den * num

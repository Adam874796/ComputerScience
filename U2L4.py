class Fraction:
    # See slideshow for a full discussion of this code.
    #
    def __init__(self, num, den):
        self.__n = num
        self.__d = den

    def getNum(self):
        return self.__n

    def getDen(self):
        return self.__d
    
    def setNum(self, num):
        self.__n = num
    
    def setDen(self, den):
        self.__d = den
    
    def __str__(self):
        return "{0}/{1}".format(self.__n, self.__d)
        

class Fraction2(Fraction):
    # See slideshow for a full discussion of this code.
    def __init__(self, num, den):
        super().__init__(num, den)
    
    def check(self):
        if self.getDen() == 0:
            print("Error: the denominator can not be a 0")
            exit()
        
    def unreduce(self, unreduce):
        self.setNum(self.getNum() * unreduce)
        self.setDen(self.getDen() * unreduce)
        
    def reduce(self):
        num = self.getNum()
        den = self.getDen()
        for i in range (2, (num + 1)):
            if ((den) % i) == 0 and ((num) % i) == 0:
                while ((den) % i) == 0 and ((num) % i) == 0:
                    den = den // i
                    num = num // i
        self.setNum(num)
        self.setDen(den)
        
        
        
    #def multiply(self):

        
num = input("choose a numerator: ")
num = int(num)
den = input("choose a denominator: ")
den = int(den)
f = Fraction2(num, den)
print(f)   

unreduce = input("chose a value to unreduce the fraction by: ")
unreduce = int(unreduce)
f.unreduce(unreduce)
print(f)
f.reduce()
print("when reduced", f)

        
# driver code

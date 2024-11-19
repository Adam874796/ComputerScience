class Fraction:
    # See slideshow for a full discussion of this code.
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
        return self
        
    def add(self, num2, den2):
        num1 = self.getNum()
        den1 = self.getDen()
        if den2 != den1:
            DenT = (den1*den2)
            num1 = (num1*den2)
            num2 = (num2*den1)
            numT = (num1 + num2)
        else:
            DenT = den1
            numT = (num1 + num2)
        self.setNum(numT)
        self.setDen(DenT)
        return self
        
    def multiply(self, num2, den2):
        num1 = self.getNum()
        den1 = self.getDen()
        
        self.setNum(num1 * num2)
        self.setDen(den1 * den2)
        return self        
        

        
num = input("choose a numerator: ")
num = int(num)
den = input("choose a denominator: ")
den = int(den)

if den == 0:
    print("your denominator can not be 0")
else:    
    f = Fraction2(num, den)
    print("your first fraction is", f)   
    num2 = input("choose a second numerator: ")
    num2 = int(num2)
    den2 = input("choose a second denominator: ")
    den2 = int(den2)

    if den2 == 0:
        print("your denominator can not be 0")
    
    if den and den2 != 0:
        choice = input("would you like to 'add' or 'multiply'? ")
        choice = str(choice)
        
        if choice == "multiply":
            FMul = f.multiply(num2, den2)
            print(FMul)
            FReduce = f.reduce()
            print("when reduced...", FReduce)
        elif choice == "add":
            FAdd = f.add(num2, den2)
            print(FAdd)
            FReduce = f.reduce()
            print("when reduced...", FReduce)
        else:
            print("this is not an avalible option")

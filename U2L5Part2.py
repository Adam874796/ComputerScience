from Fraction import Fraction

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

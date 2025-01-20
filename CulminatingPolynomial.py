import math

class Polynomial:
    def __init__(self, func):
        self.__func = func
        self.__len = len(func)
        self.__eq = ""
   
    def craft(self):
        i = 0
        for c in self.__func:
           
            if i == 0 and c < 0:
                c = c *-1
                self.__eq = self.__eq + "-"
            elif 0 < i < self.__len and c > 0 and self.__eq != "":
                self.__eq = self.__eq + " + "
            elif 0 < i < self.__len and c < 0 and self.__eq != "":
                self.__eq = self.__eq + " - "
                c = c*-1
                 
            if c == 0:
                pass

            elif c == 1:
                if self.__len-1 == i:
                    self.__eq = self.__eq + str(c)
                elif (self.__len -2) == i:
                    self.__eq = self.__eq + 'x'
                else:
                    piece = "x^" + str(self.__len -i-1)
                    self.__eq = self.__eq + piece
                    
            else:
                if self.__len-1 == i:
                    self.__eq = self.__eq + str(c)
                elif (self.__len -2) == i:
                    piece = str(c) + 'x'
                    self.__eq = self.__eq + piece
                else:
                    piece = str(c) + "x^" + str(self.__len -i-1)
                    self.__eq = self.__eq + piece
           
            i += 1
        return self.__eq
   
    def get_order(self):
        i = 0  
        while i < self.__len:
            if self.__func[i] != 0:  
                return self.__len - i - 1
            i += 1
        return -1
   
    def f(self, x: float):
        i = 0
        y = 0.0
        for c in self.__func:
            if i == self.__len-1:
                y = y + c
            elif i == self.__len-2:
                y = x*c + y
            else:
                y = x**(self.__len-(i + 1))*c+y
            i += 1
        return y
           
    def __str__(self):
        return f"{self.__eq}"

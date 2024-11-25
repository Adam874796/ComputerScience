from Fraction2 import Fraction2
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
            
            



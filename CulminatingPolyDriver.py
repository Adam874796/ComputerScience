from Polynomial import *

"""
Author : Adam Saad
   Revison date : January 22nd 2025
   Program : ICS4U0-1
   Description : A code that solves a polynomial function given an x-value

 General Variable Dictionary:
 - function (list[str]) the coefficients of the function
 - arr (list[str]) the filtered out version of the coefficients of the function
 - temp (list[str]) a list of coefficients each as their own term
 - func (list[int/float]) the final version of our list of coefficients as a float/int
 - x (float) an inputed x-value which the function will be solved for
"""

#-2, 5, -3, 1 and 4, 2, -3, 33 are the functions im using

function = (4, 2, -3, 33)
function = str(function) # input a string for the coefficients of the function

func = []

arr = function.strip("+()[]{}") # get rid of uneccesary terms which may have been used
temp = arr.split(',') # split up input

for c in temp:
    try:
        func.append(float(c)) # try making the coefficients into floats
    except ValueError:
        print("Please input a set of numbers with commas in between") # if a value error occurs output the issue to let the user know and exit the code
        exit()
        
test = Polynomial(func)
test.craft()
print(test)
        
x = input("Please input an x value you would like to solve the function for: ") # take input for an x-value the user would like the function to be solved for.
try:
    x = float(x) # make it a float
except ValueError:
    print("please input a proper number") # if a value error occurs output the issue to let the user know and exit the code

    exit()
        
print(test.f(x)) # solve the y value at the inputted x

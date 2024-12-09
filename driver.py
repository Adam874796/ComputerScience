# driver for the polygon class
from poly import *

def getNumeric(data : str):
    # input: S is a point in the format "(x,y)" (type str)
    # output: a tuple or list indicating a point (x, y) where x, y are int or float
    arr = data.split(', ')
    PS = []
    for c in arr:
        p = c.strip("()")
        [x,y] = p.split(',')
        pt = point(x, y)
        pt.valid()
        PS.append([x,y])
    return PS

fh = open("a2.txt", "r") # this is the name of the data file to open
polydata = fh.readline().strip()
cord = getNumeric(polydata)
Poly = Polygon()
for z in range(len(cord)):
    x = cord[z][0]
    y = cord[z][1]
    Poly.add_point(x,y)
   
# declare a polygon
# loop through the points array and turn them into numbers for the polynomial object
    # generate an x, y pair (numerical not str) from getNumeric
    # add to the polynomial (call add_point())

print(Poly) # this should print the entire linked list of points as string

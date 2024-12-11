"""
Author : Adam Saad
   Revison date : December 9th 2024
   Program : ICS4U0-1
   Description : A code that takes input from a file of polygon vertex coordinates and returns information back
   
 General Variable Dictionary:
 - fh (file object): File handle for reading the input file.
 - polydata (str): Raw data line from the file.
 - cord (list): List of parsed points from the file.
 - Poly (Polygon): The Polygon object created and populated.

    
"""

# import code from poly
from poly import *
# Driver for the polygon class.

def get_numeric(data: str):
    # PreConditions and Purpose: Parse a string of points in the format "(x, y), (x, y), ...".
    # PostConditions: Returns a list of Point objects after validation.

    # Variable dictionary:
    # data (str): Input string of points.
    # arr (list): List of point substrings split by commas.
    # PS (list): List of validated Point objects.

    arr = data.split('), (')  # Split into individual points.
    PS = []
    for c in arr:
        p = c.strip("()")  # Remove parentheses.
        x, y = p.split(',')
        pt = point(x, y)
        pt.valid()  # Validate coordinates.
        PS.append([float(x), float(y)])
    return PS


# Main execution.

fh = open("a2.txt", "r")  # Open the data file.
polydata = fh.readline().strip()  # Read the first line and strip whitespace.
cord = get_numeric(polydata)  # Parse points from the file.

Poly = Polygon()  # Create a new Polygon object.
for z in range(len(cord)):
    x = cord[z][0]
    y = cord[z][1]
    Poly.add_point(x, y)  # Add each point to the Polygon.

print(Poly)  # Output the polygon as a string.

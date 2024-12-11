import math

class point:
    def __init__(self, x: float = None, y: float = None):
        # PreConditions and Purpose: Initialize a Point object with x and y coordinates.
        # x, y can be floats or None for the creation of a head node in a circular linked list.
        # PostConditions: Creates a Point object with default x, y as None and next as None.

        self.__x = x  # x-coordinate of the point (type: float or None)
        self.__y = y  # y-coordinate of the point (type: float or None)
        self.next = None  # Pointer to the next point in the circular linked list (type: Point or None)

    def valid(self):
        # PreConditions and Purpose: Validate the x and y coordinates to ensure they are numbers.
        # PostConditions: Converts x and y to int or float, or exits if invalid.

        try:
            self.__x = int(self.__x)
            self.__y = int(self.__y)
        except ValueError:
            try:
                self.__x = float(self.__x)
                self.__y = float(self.__y)
            except ValueError:
                print("x and y coordinates must be numbers")
                exit()

    def get_coordinates(self):
        # PreConditions and Purpose: Retrieve the x and y coordinates of the Point.
        # PostConditions: Returns a tuple (x, y) as floats.

        return float(self.__x), float(self.__y)

    def __str__(self):
        # PreConditions and Purpose: Represent the Point object as a string in the format "(x, y)".
        # PostConditions: Returns a string representation of the Point.

        return f"({self.__x}, {self.__y})"


class Polygon:
    def __init__(self):
        # PreConditions and Purpose: Initialize a Polygon object.
        # PostConditions: Creates a Polygon with default values and an empty circular linked list of points.

        self.__sides = 0  # Number of sides in the polygon (type: int, default: 0)
        self.__vertices = 0  # Number of vertices in the polygon (type: int, default: 0)
        self.__head = None  # Head node of the circular linked list (type: Point or None)

    def add_point(self, x: float, y: float):
        # PreConditions and Purpose: Add a new point (x, y) to the polygon as part of a circular linked list.
        # PostConditions: Adds a new Point to the circular linked list and updates vertex count.

        # Variable dictionary:
        # h (Point): The new point to be added.
        # V (Point): Traversal pointer to find the last point in the circular linked list.

        h = point(x, y)
        if self.__head is None:
            # First point: Initialize head and make it circular.
            self.__head = h
            h.next = h
        else:
            # Add the new point to the circular linked list.
            V = self.__head
            while V.next != self.__head:
                V = V.next
            V.next = h
            h.next = self.__head
        self.__vertices += 1

    def __str__(self):
        # PreConditions and Purpose: Generate a string representation of the polygon as a series of points.
        # PostConditions: Returns the circular linked list of points in the format "(x, y) -> (x, y) -> ...".

        if self.__vertices < 3:
            return "A line or point is not a Polygon"

        # Variable dictionary:
        # nodes (list): List of point strings.
        # V (Point): Traversal pointer to traverse the circular linked list.

        nodes = []
        V = self.__head
        nodes.append(str(V))  # Add the head point.
        V = V.next
        while V != self.__head:
            nodes.append(str(V))
            V = V.next
        return " -> ".join(nodes)


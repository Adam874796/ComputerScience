import math
import turtle

class Point:
    def __init__(self, x: float = None, y: float = None):
        # PreConditions: Initialize a Point object with x and y coordinates.
        # x and y can be floats or None for creating a head node in a circular linked list.
        # PostConditions: Creates a Point object with x, y coordinates (default None) and a next pointer (default None).
        # Variable dictionary:
        # - self.__x (float): The x-coordinate of the point.
        # - self.__y (float): The y-coordinate of the point.
        # - self.next (Point): Pointer to the next point in the circular linked list.

        self.__x = x  # x-coordinate of the point (type: float or None)
        self.__y = y  # y-coordinate of the point (type: float or None)
        self.next = None  # Pointer to the next point in the circular linked list (type: Point or None)
        self.valid()

    def valid(self):
        # PreConditions: Validate x and y coordinates to ensure they are numbers (int or float).
        # PostConditions: Converts x and y to int or float if valid; exits the program if invalid.

        try: # try converting values to an int
            self.__x = int(self.__x)
            self.__y = int(self.__y)
        except ValueError: # if there is an error try again with a float.
            try:
                self.__x = float(self.__x)
                self.__y = float(self.__y)
            except ValueError: # if there is another error then output that the values are not numbers and exit the code.
                print("x and y coordinates must be numbers")
                exit()

    def distance(self, p2):
        # PreConditions: Requires another Point object (p2) to compute the distance.
        # PostConditions: Returns the Euclidean distance between this point and p2.
        # Variable dictionary:
        # - p2 (Point): The other Point object.
        # - x2, y2 (float): Coordinates of p2.

        x2, y2 = p2.get_cord()
        return math.sqrt((self.__x - x2) ** 2 + (self.__y - y2) ** 2)

    def get_cord(self):
        # PreConditions: None.
        # PostConditions: Returns a tuple (x, y) of the Point's coordinates as floats.

        return float(self.__x), float(self.__y)

    def __str__(self):
        # PreConditions: None.
        # PostConditions: Returns a string representation of the Point in the format "(x, y)".

        return f"({self.__x}, {self.__y})"

class Polygon:
    def __init__(self):
        # PreConditions: None.
        # PostConditions: Creates a Polygon object with an empty circular linked list of points.
        # Variable dictionary:
        # - self.__sides (int): Number of sides in the polygon.
        # - self.__vertices (int): Number of vertices in the polygon.
        # - self.__head (Point): Head node of the circular linked list of points.

        self.__sides = 0
        self.__vertices = 0
        self.__head = None

    def add_point(self, x: float, y: float):
        # PreConditions: Adds a new point (x, y) to the polygon.
        # PostConditions: Adds a new Point to the circular linked list and updates the vertex count.
        # Variable dictionary:
        # - V (Point): The new point to be added.
        # - h (Point): Traversal pointer to find the last point in the circular linked list.

        V = Point(x, y)
        if self.__head is None:
            # First point: Initialize head and make it circular.
            self.__head = V
            V.next = V
        else:
            # Add the new point to the circular linked list.
            h = self.__head 
            while h.next != self.__head: # stop the code when you have circled back to the head.
                h = h.next
            h.next = V
            V.next = self.__head # set the value of V.next to your head.
        self.__vertices += 1 # add up the vertices as you go.
        if self.__vertices > 1:
            self.__sides = self.__vertices # equate the # of sides to the # of vertices.
            
    def nodes(self):
        # PreConditions: Requires a circular linked list of points.
        # PostConditions: Returns all points in variable 'nodes'.
        # Variable dictionary:
        # - V: The new point to be added.
        # - nodes: list of all points.
        V = self.__head # make a variable, V, with the value of your head.
        nodes = []
        nodes.append(V) # add the head to your nodes array.
        V = V.next # move onto the next point.
        while V != self.__head: # make a loop which goes until you circle back to your head.
            nodes.append(V) # add each point to your nodes list.
            V = V.next
        return nodes # return nodes which contains all points.        

    def side_len(self):
        # PreConditions: Requires a circular linked list of points.
        # PostConditions: Returns a list of side lengths of the polygon.
        # Variable dictionary:
        # - side_len (list): List of side lengths.
        # - side (Point): Traversal pointer for the circular linked list.

        side_len = []
        side = self.__head 
        dist = side.distance(side.next) # 'set dist' to the distance between the head and the first point.
        side_len.append(dist)
        side = side.next 
        while side != self.__head: # make a loop which repeats the last step for all other points until you circle back to the head.
            dist = side.distance(side.next)
            side_len.append(dist) # add all lengths to the list 'side_len'.
            side = side.next
        return side_len

    def is_poly(self):
        # PreConditions: None.
        # PostConditions: Validates if the linked list represents a valid polygon.
        # Checks for duplicate points and ensures at least three vertices exist.

        check = self.nodes()
        if len(check) < 3: # if there are less than 3 points output that the polygon is not proper.
            print("Not enough points found...")
            exit()
        for p1 in check: # setup a nested loop to compare every point
            tally = 0 
            for p2 in check:
                if p1 == p2:
                    tally += 1
                    if tally == 2: # if there is a duplicate point found exit code after informing the user.
                        print("Duplicate point found...")
                        exit()

    def internal_angle(self):
        # PreConditions: Requires a valid polygon.
        # PostConditions: Returns a list of internal angles of the polygon.
        # Variable dictionary:
        # - vert (Point): Traversal pointer for the linked list.
        # - angles (list): List of calculated internal angles.
        # - dotV (float): Dot product of vectors.
        # - mag_sum (float): Magnitude of vector product.

        self.is_poly() # confirm that the polygon is valid.
        vert = self.__head
        angles = []
        x1, y1 = vert.get_cord() # get coordinates.
        x2, y2 = vert.next.get_cord()
        x3, y3 = vert.next.next.get_cord()
        dotV = float((x1 - x2) * (x3 - x2)) + ((y1 - y2) * (y3 - y2))  # calculate dot product.

        mag_sum = abs(math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))) * (math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))
        if mag_sum != 0: # calculate the magnitude of the dot product and confirm that it is valid.
            theta2 = (math.acos((dotV / mag_sum))) * (180 / math.pi)
            vert = vert.next 
        else:
            print("Duplicate points...")
            exit()
        while vert != self.__head: # continue process for all other points until you circle back to the head.
            if vert.next == self.__head:
                x2, y2 = vert.next.get_cord()
                x3, y3 = vert.next.next.get_cord()
                dotV = float(((x2 - 1) - x2) * (x3 - x2)) + ((y2 - y2) * (y3 - y2))

                mag_sum = abs(math.sqrt(((x2 - 1) - x2) ** 2 + ((y2 - y2) ** 2))) * (
                    math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))
                if mag_sum != 0:
                    self.__head_angle = (math.acos((dotV / mag_sum))) * (180 / math.pi)
                    if self.__head_angle > 90: 
                        self.__head_angle = self.__head_angle - 90 # make sure the angle is valid
                else:
                    self.__head_angle = 0

            if vert == self.__head.next.next:
                angles.append(theta2) # add angles to list.

            x1, y1 = vert.get_cord()
            x2, y2 = vert.next.get_cord()
            x3, y3 = vert.next.next.get_cord()
            dotV = float((x1 - x2) * (x3 - x2)) + ((y1 - y2) * (y3 - y2))
            mag_sum = abs(math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))) * (math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))

            if mag_sum != 0:
                theta = (math.acos((dotV / mag_sum))) * (180 / math.pi)
                angles.append(theta) # add calculated angles to list
                vert = vert.next
            else:
                print("Duplicate points...")
                exit()
        return angles # after all angles have been added to the list and you have circled back to the head, return the angles as a list.

    def poly_check(self):
        # PreConditions: Requires a valid polygon.
        # PostConditions: Checks if the polygon is regular.

        self.is_poly()
        angles = self.internal_angle() 
        side_len = self.side_len()
        for i in range((len(angles)) - 1): # confirm if the polygon is regular or irregular based off the side lengths and angles.
            if round(side_len[i]) != round(side_len[i + 1]) or round(angles[i]) != round(angles[i + 1]):
                return False
        return True # if it is a regular polygon return true, vice versa.

    def perimeter(self):
        # PreConditions: Requires a valid polygon.
        # PostConditions: Returns the perimeter of the polygon.

        self.is_poly() # check if polygon is valid or not.
        side_len = self.side_len()
        if self.poly_check(): # if it is a regular polygon calculate the perimeter in the way below.
            return round(side_len[0] * self.__sides, 3)
        else: # if it is an irregular polygon calculate it the other way.
            return round(sum(side_len), 3)

    def area(self):
        # PreConditions: Requires a valid polygon.
        # PostConditions: Returns the area of the polygon.

        self.is_poly() # check if polygon is valid or not.
        angles = self.internal_angle()
        side_len = self.side_len()
        if self.poly_check(): # calculate area in the way below if input is a regular polygon.
            n = self.__sides
            s = side_len[0]
            return round((n * (s ** 2)) / (4 * math.tan(math.pi / n)), 3)
        else: # if polygon is irregular calculate area in the way below.
            x_points, y_points = [], []
            nodes = self.nodes()
            for n in range(len(nodes)):
                A, B = nodes[n].get_cord()
                x_points.append(A)
                y_points.append(B)
                if n == len(nodes) - 1:
                    A, B = nodes[0].get_cord()
                    x_points.append(A)
                    y_points.append(B)

            sum1 = sum(x_points[i] * y_points[i + 1] for i in range(len(nodes)))
            sum2 = sum(x_points[i + 1] * y_points[i] for i in range(len(nodes)))
            return round(abs((sum1 - sum2) / 2), 3)

    def draw(self):
        # PreConditions: Requires a valid polygon.
        # PostConditions: Draws the polygon using the turtle graphics library.

        self.is_poly()
        turtle.shape("circle") # change shape and size of cursor
        turtle.shapesize(0.3, 0.3)
        turtle.speed(1)
        turtle.penup()
        V = self.__head # start with head.
        x, y = V.get_cord()
        turtle.setpos(x, y) # go to the head.
        turtle.pendown()
        V = V.next
        while V != self.__head: # go to each point one by one until you circle back to the head.
            x0, y0 = V.get_cord()
            turtle.goto(x0, y0)
            V = V.next
        x0, y0 = V.get_cord()
        turtle.goto(x0, y0) 
        turtle.done()

    def __str__(self):
        # PreConditions: None.
        # PostConditions: Returns a string representation of the polygon as a series of points.
        # Variable dictionary:
        # nodes (list): List of point strings.
        # V (Point): Traversal pointer to traverse the circular linked list.

        self.is_poly()
        V = self.__head
        nodes = str(V) # Add the head point.
        V = V.next
        while V != self.__head: # continue until you circle back to the head
            nodes += " -> " + str(V) # format the string appropriately 
            V = V.next
        return nodes # return all points formatted appropiately

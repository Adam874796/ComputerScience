import math

# General Variable Dictionary:
# - func (list[int/float]): Coefficients of the polynomial in descending order of degree.
# - __func (list[int/float]): Encapsulated version of `func` for internal use.
# - __len (int): Length of the `__func` list, representing the number of terms.
# - __eq (str): String representation of the polynomial equation.
# - i (int): Loop counter used for iterating through coefficients.
# - c (int/float): Current coefficient during iteration.
# - piece (str): Substring representing a part of the polynomial term.
# - x (float): Input value for calculating the polynomial at a given point.
# - y (float): Resultant value of the polynomial after evaluation.

class Polynomial:
    def __init__(self, func):
        """
        Pre-conditions: `func` is a list of coefficients, ordered from highest to lowest degree.
        Post-conditions: Initializes the polynomial object with its coefficients and prepares
                         an empty equation string.
        """
        self.__func = func
        self.__len = len(func)  # Store the number of terms.
        self.__eq = ""          # Initialize the polynomial equation as an empty string.
   
    def craft(self):
        """
        Pre-conditions: `self.__func` contains the coefficients of the polynomial.
        Post-conditions: Constructs a human-readable string representation of the polynomial equation.
                         Returns this string representation.
        """
        i = 0  # Initialize the term index.
        for c in self.__func:
            # Handle sign for positive and negative coefficients.
            if i == 0 and c < 0:
                c = -c
                self.__eq += "-"
            elif 0 < i < self.__len and c > 0 and self.__eq != "":
                self.__eq += " + "
            elif 0 < i < self.__len and c < 0 and self.__eq != "":
                self.__eq += " - "
                c = -c
            
            # Skip terms with a coefficient of 0.
            if c == 0:
                pass
            elif c == 1:
                # Handle coefficients of 1 for different positions.
                if self.__len - 1 == i:
                    self.__eq += str(c)
                elif self.__len - 2 == i:
                    self.__eq += 'x'
                else:
                    piece = "x^" + str(self.__len - i - 1)
                    self.__eq += piece
            else:
                # Handle coefficients other than 1.
                if self.__len - 1 == i:
                    self.__eq += str(c)
                elif self.__len - 2 == i:
                    piece = str(c) + 'x'
                    self.__eq += piece
                else:
                    piece = str(c) + "x^" + str(self.__len - i - 1)
                    self.__eq += piece

            i += 1  # Increment the term index.
        return self.__eq  # Return the constructed polynomial equation.
   
    def get_order(self):
        """
        Pre-conditions: `self.__func` contains the coefficients of the polynomial.
        Post-conditions: Returns the highest degree of the polynomial. If all coefficients
                         are zero, returns -1.
        """
        i = 0  # Initialize the term index.
        while i < self.__len:
            if self.__func[i] != 0:  # Identify the first non-zero coefficient.
                return self.__len - i - 1
            i += 1  # Increment the index.
        return -1  # Return -1 if all coefficients are zero.
   
    def f(self, x: float):
        """
        Pre-conditions: `x` is a float or int value. `self.__func` contains the coefficients.
        Post-conditions: Returns the value of the polynomial evaluated at `x`.
        """
        i = 0  # Initialize the term index.
        y = 0.0  # Initialize the result of the polynomial evaluation.
        for c in self.__func:
            # Add each term's contribution to the total value.
            if i == self.__len - 1:
                y += c
            elif i == self.__len - 2:
                y += x * c
            else:
                y += x ** (self.__len - (i + 1)) * c
            i += 1  # Increment the term index.
        return y  # Return the computed value.
           
    def __str__(self):
        """
        Pre-conditions: The polynomial equation string (`self.__eq`) is already constructed.
        Post-conditions: Returns the string representation of the polynomial.
        """
        return f"{self.__eq}"

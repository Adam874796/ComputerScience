import math
from Polynomial import *

class IVT:
    def __init__(self, func):
        """
        Pre-conditions:
        - `func` is a list of coefficients representing a polynomial, ordered from the highest to lowest degree.

        Post-conditions:
        - Initializes the IVT object with the polynomial function, its length, and a Polynomial object.

        Variable Dictionary:
        - func (list[float]): Coefficients of the polynomial.
        - self.__func (list[float]): Encapsulated version of `func`.
        - self.__len (int): Length of the function (number of coefficients).
        - self.__Poly (Polynomial): Polynomial object to leverage existing methods.
        """
        self.__func = func
        self.__len = len(func)
        self.__Poly = Polynomial(func)
       
    def solve(self, x: float, y: float):
        """
        Pre-conditions:
        - `x` is a float representing the input to the polynomial.
        - `y` is a float to compare the polynomial evaluation against.

        Post-conditions:
        - Returns the difference between the polynomial evaluated at `x` and `y`.

        Variable Dictionary:
        - i (int): Index for iterating over coefficients.
        - exp (int): Exponent of the current term.
        - val (float): Accumulated value of the polynomial evaluation.
        """
        i = 0
        val = 0.0
        while i < self.__len:
            exp = self.__len - i - 1
            val += self.__func[i] * (x ** exp)
            i += 1
        return val - y
   
    def derivative(self):
        """
        Pre-conditions:
        - None (uses `self.__func`).

        Post-conditions:
        - Returns a list of coefficients representing the derivative of the polynomial.

        Variable Dictionary:
        - derive (list[float]): Coefficients of the derivative.
        - i (int): Index for iterating over coefficients.
        - exp (int): Exponent of the current term.
        """
        derive = []
        i = 0
        while i < self.__len:
            exp = self.__len - i - 1
            if exp > 0 and self.__func[i] != 0:
                derive.append(self.__func[i] * exp)
            i += 1
        return derive
   
    def derive(self, der, x: float):
        """
        Pre-conditions:
        - `der` is a list of derivative coefficients.
        - `x` is the point at which the derivative is evaluated.

        Post-conditions:
        - Returns the derivative evaluated at `x`.

        Variable Dictionary:
        - val (float): Accumulated value of the derivative evaluation.
        - i (int): Index for iterating over `der`.
        - exp (int): Exponent of the current term.
        """
        val = 0.0
        for i in range(len(der)):
            exp = len(der) - i - 1
            val += der[i] * (x ** exp)
        return val
   
    def newton(self, x1: float):
        """
        Pre-conditions:
        - `x1` is the initial guess for the root.

        Post-conditions:
        - Returns the root found using Newton's method, or None if it fails.

        Variable Dictionary:
        - valid (float): Threshold for convergence.
        - max (int): Maximum iterations.
        - test (int): Counter for iterations (unused).
        - der (list[float]): Coefficients of the derivative.
        - fx (float): Value of the polynomial at `x1`.
        - fx_pr (float): Value of the derivative at `x1`.
        - new_x (float): Updated value of the root estimate.
        """
        valid = 1e-10
        max = 100
        test = 0
        der = self.derivative()

        for __ in range(max):
            fx = self.solve(x1, 0)
            fx_pr = self.derive(der, x1)

            if fx_pr == 0:  # Failsafe for division by zero.
                return None
           
            if __ == max - 1:  # Did not converge.
                return None
           
            new_x = x1 - fx / fx_pr
            if abs(new_x - x1) < valid:  # Convergence check.
                return new_x
            x1 = new_x
        return None

    def brute(self, x1: float, x2: float):
        """
        Pre-conditions:
        - `x1` and `x2` define the interval within which a root is sought.

        Post-conditions:
        - Returns the root found using the bisection method, or None if no root exists.

        Variable Dictionary:
        - valid (float): Threshold for convergence.
        - f_x1 (float): Value of the polynomial at `x1`.
        - f_x2 (float): Value of the polynomial at `x2`.
        - avg (float): Midpoint of the current interval.
        - f_z (float): Value of the polynomial at `avg`.
        """
        valid = 1e-5  
        f_x1 = self.__Poly.f(x1)
        f_x2 = self.__Poly.f(x2)
       
        if f_x1 * f_x2 > 0:
            return None  # No root if f(x1) and f(x2) have the same sign.

        while abs(x2 - x1) > valid:
            avg = (x1 + x2) / 2
            f_z = self.__Poly.f(avg)

            if abs(f_z) < valid:
                return avg
            elif f_x1 * f_z < 0:  
                x2 = avg
                f_x2 = f_z
            else:  
                x1 = avg
                f_x1 = f_z

        return None

    def find1Zero(self, _x1: float, _x2: float):
        """
        Pre-conditions:
        - `_x1` and `_x2` define the interval for searching one root.

        Post-conditions:
        - Returns a root of the polynomial, or a message if no root is found.

        Variable Dictionary:
        - x1, x2 (float): Corrected interval endpoints.
        - deg (int): Degree of the polynomial.
        - r (float): Root for linear or constant polynomials.
        - z1, z2, z3 (float): Roots found using different methods.
        """
        # Function logic continues as provided...

    def findZero(self, _x1: float, _x2: float):
        """
        Pre-conditions:
        - `_x1` and `_x2` define the interval for searching all roots.

        Post-conditions:
        - Returns a list of all roots, or a message if none are found.

        Variable Dictionary:
        - x1, x2 (float): Corrected interval endpoints.
        - deg (int): Degree of the polynomial.
        - z1, z2, z3 (float): Roots found using different methods.
        - roots (list[float]): List of all roots.
        """
        # Function logic continues as provided...

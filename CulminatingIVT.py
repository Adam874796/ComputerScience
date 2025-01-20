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
        - _x1 and _x2 must be floating-point numbers.
        - _x1 and _x2 must not be equal.
        - Polynomial coefficients must be initialized in self.__func.
    
        Post-conditions:
        - Returns one root of the polynomial within the range [_x1, _x2] if found.
        - Handles polynomials of degree 0 (constant), 1 (linear), and 2 (quadratic) explicitly.
        - For degree > 2, attempts to find a root using brute force and Newton's method.
        - Returns a message if no roots are found.
        """
    
        # Variable Dictionary:
        # _x1, _x2: float - Input bounds for searching roots.
        # x1, x2: float - Adjusted bounds to ensure x1 < x2.
        # deg: int - Degree of the polynomial.
        # r: float or str - The root of the polynomial or a message indicating no roots.
        # Qf: float - Discriminant of the quadratic equation.
        # z1, z2, z3: float or None - Potential roots found using brute force or Newton's method.
    
        # Get the degree of the polynomial
        deg = self.__Poly.get_order()
    
        # Ensure the input bounds are valid
        if _x1 == _x2:
            return "The x values must be different"
        elif _x1 > _x2:
            x1 = _x2
            x2 = _x1
        else:
            x1 = _x1
            x2 = _x2
    
        # Handle cases based on the degree of the polynomial
        if deg == -1:  # No function exists
            return "No function found"
    
        elif deg == 0:  # Constant polynomial
            r = self.__func[self.__len - 1]
            return r
    
        elif deg == 1:  # Linear polynomial
            der = self.derivative()  # Calculate derivative
            r = (0 - self.__func[self.__len - 1]) / der[0]  # Root from ax + b = 0
            return r
    
        elif deg == 2:  # Quadratic polynomial
            a = self.__func[self.__len - 3]
            b = self.__func[self.__len - 2]
            c = self.__func[self.__len - 1]
    
            # Compute discriminant
            Qf = (b**2 - 4 * a * c)
    
            if Qf > 0:  # Two distinct roots
                r1 = (-b + math.sqrt(Qf)) / (2 * a)
                r2 = (-b - math.sqrt(Qf)) / (2 * a)
                return r1, r2
    
            elif Qf == 0:  # One root (double root)
                r = -b / (2 * a)
                return abs(r) if r == 0 else r
    
            else:  # No real roots
                return "No root found..."
    
        elif deg > 2:  # Higher degree polynomial
            # Try brute force to find a root in the range
            z1 = self.brute(x1, x2)
    
            if z1 is None or abs(self.__Poly.f(z1)) > 1e-5 or not (x1 - 1 <= z1 <= x2 + 1):
                # Try Newton's method starting at x1
                z2 = self.newton(x1)
                if z2 is None or abs(self.__Poly.f(z2)) > 1e-5 or not (x1 <= z2 <= x2 + 1):
                    # Try Newton's method starting at x2
                    z3 = self.newton(x2)
                    if z3 is None or abs(self.__Poly.f(z3)) > 1e-5 or not (x1 - 1 <= z3 <= x2 + 1):
                        return "No roots between given values"
                    elif z3 != -0:
                        return z3
                    else:
                        return 0.0
    
                elif z2 != -0:
                    return z2
                else:
                    return 0.0
    
            elif z1 != -0:
                return z1
            else:
                return 0.0

    def findZero(self, _x1: float, _x2: float):
    """
    Pre-conditions:
    - _x1 and _x2 must be floating-point numbers.
    - _x1 and _x2 must not be equal.
    
    Post-conditions:
    - Returns the roots of the polynomial within the range [_x1, _x2], if any exist.
    - Returns a sorted list of unique roots if multiple roots exist.
    - Returns a message if no roots exist in the given range.
    """

    # Variable Dictionary:
    # _x1, _x2: float - The bounds within which to search for roots.
    # x1, x2: float - Adjusted bounds ensuring x1 < x2.
    # z1: float or None - Root found using the brute-force method.
    # z2, z3: float or None - Roots found using Newton's method at bounds x1 and x2.
    # deg: int - Degree of the polynomial.
    # roots: list - List of unique roots found within the range.

    # Ensure _x1 < _x2 for consistency
    if _x1 == _x2:
        return "The x values must be different"
    elif _x1 > _x2:
        x1 = _x2
        x2 = _x1
    else:
        x1 = _x1
        x2 = _x2

    # Attempt to find roots using different methods
    z1 = self.brute(x1, x2)  # Brute-force search for a root
    z2 = self.newton(x1)     # Newton's method starting from x1
    z3 = self.newton(x2)     # Newton's method starting from x2
    deg = self.__Poly.get_order()  # Degree of the polynomial
    roots = []  # List to store found roots

    # If no roots are found using any method, return a message
    if z1 is None and z2 is None and z3 is None:
        return "No roots between given values"

    # For polynomials of degree less than 3, return z2 and z3 directly
    elif deg < 3:
        return z2, z3

    # If Newton's method converges to the same root for both bounds, return that root
    elif round(z2, 7) == round(z3, 7):
        return z2

    # For higher-degree polynomials, find and return all unique roots
    else:
        roots.append(z2)  # Root closest to negative infinity
        roots.append(z3)  # Root closest to positive infinity
        i = 0
        while i < deg - 2:  # Continue finding additional roots
            # Divide the interval dynamically for new guesses
            low = 1 / (deg - 1)
            high = 1 - low
            z = self.newton((z2 * high + z3 * low))  # Test a point closer to z2

            # Check if the found root z is already in roots
            f = 0
            for r in roots:
                if z is None or r is None:
                    pass
                elif round(r, 5) == round(z, 5):
                    f = 1

            # Add z if it is a new root
            if f != 1 and z is not None:
                roots.append(z)
                z2 = z

            else:
                # Try different combinations to find a new root
                z = self.newton((z2 * 0.7 + z3 * 0.3))  # Test midpoint closer to z2
                f = 0
                for r in roots:
                    if z is None or r is None:
                        pass
                    elif round(r, 5) == round(z, 5):
                        f = 1

                if f != 1 and z is not None:
                    roots.append(z)
                    z2 = z
                else:
                    z = self.newton((z2 + z3) / 2)  # Midpoint of z2 and z3
                    f = 0
                    for r in roots:
                        if z is None or r is None:
                            pass
                        elif round(r, 5) == round(z, 5):
                            f = 1

                    if f != 1 and z is not None:
                        roots.append(z)
                        z2 = z
                    else:
                        # As a last resort, use brute-force to find a root in a small interval
                        z = self.brute((z2 + 1e-4), (z3 - 1e-4))
                        if z is not None:
                            roots.append(z)
                            z2 = z
            i += 1

        roots.sort()  # Sort the roots for consistency
        return roots

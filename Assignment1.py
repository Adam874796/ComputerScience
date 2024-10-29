"""
Author : Adam Saad
   Revison date : October 16th 2024
   Program : ICS4U0-1
   Description : A code that makes a magic square array of n x n size with random digits
   
Variable Dictionary:
Value : int : The number the user inputs for the size of the matrix
    
"""

import random  # Used to shuffle arrays randomly
import math  # Used to calculate square roots for prime-checking


# PreConditions and Purpose: Function to check if inputted number 'n' is prime
def is_prime(n):
    """
    Variable Dictionary:
    n : int : The number we're checking if it's prime for
    
    """
    if n < 2:  # Numbers less than 2 are not prime
        return False
    # Check if n is prime by seeing if it has divisors up to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If n is divisible by i, it's not prime where i is every number upto the square root of n
            return False 
    return True  # If no divisors are found, n is prime
    # PostConditions: Returns: True if n is prime, False otherwise.

# PreConditions and Purpose: Function to generate two arrays, A and B, based on the input value
def generate_arrays(Value):
    """
    Variable Dictionary:
    Value : int : The upper limit for generating arrays
    
    """
    # Create array A with numbers from 1 to Value, then shuffle them randomly
    A = list(range(1, Value + 1))
    random.shuffle(A)  # Shuffles A to create a random order

    # Create array B with multiples of Value (0*Value, 1*Value, 2*Value, 3*Value, ..., Value * (Value - 1))
    B = [Value * i for i in range(0, Value)]
    random.shuffle(B)  # Shuffle B randomly as well

    return A, B  # Return both arrays
    # PostConditions: Returns: Two lists, A (1 to Value in random order) and B (multiples of Value in random order).

# PreConditions and Purpose: Function to create a shifted square matrix (size x size) based on an input list M, an inputted shift amount for each line of the code, and a size to make the resulting square matrix
def Make_Square(M, shift, size):
    """
    Variable Dictionary:
    M : list : A list of numbers used to fill the square matrix
    shift : int : The number of shifts to apply for each row
    size : int : The size of the square matrix (size x size)
    
    """
    result = []  # This will hold the final square matrix
    for i in range(size):  # Loop to create 'size' number of rows
        shifted_row = []  # Start a new row for each iteration
        for n in range(len(M)):  # Loop through each element in M
            # Calculate the shifted index for this element
            y = (n - (shift * i)) % size
            shifted_row.append(M[y])  # Append the shifted element to the row
        result.append(shifted_row)  # Add the shifted row to the final matrix
    return result  # Return the full square matrix
    # PostConditions: Returns: A list of lists representing a shifted square matrix.

# PreConditions and Purpose: Function to add two square matrices element-wise the square matrices are known as M1 and M2
def addM(M1, M2):
    """
    Variable Dictionary:
    M1 : list : The first square matrix to add
    M2 : list : The second square matrix to add
    
    """
    w = len(M1)  # Assume both matrices are of the same size
    # Initialize a new matrix (AT) with zeros, same size as M1 and M2
    AT = [[0] * w for _ in range(w)]  
    # Loop through each element in both matrices and add them
    for i in range(len(M1)):
        for j in range(len(M1)):
            AT[i][j] = M1[i][j] + M2[i][j]  # Add corresponding elements
    print("The Magic Square is:")
    for row in range(len(AT)):
        print(AT[row])  # Print the resulting matrix
    return AT  # Return the resulting matrix
    # PostConditions: Returns: A new matrix that is the sum of M1 and M2 called AT

# PreConditions and Purpose: Function to check if a matrix 'M' is a magic square
def isMagic(M):
    """
    Variable Dictionary:
    M : list : A square matrix to check if it's a magic square.
    size : int : total size of the matrix's lentgh
    magic_sum : int : the targetted magic sum amount
    
    """
    size = len(M)  # Get the size of the matrix
    magic_sum = sum(M[0])  # Sum of the first row, the target magic sum

    # Check if all rows sum to the magic sum
    for row in M:
        if sum(row) != magic_sum:  # If any row doesn't sum to magic_sum, return False
            return False

    # Check if all columns sum to the magic sum
    for col in range(size):
        if sum(M[row][col] for row in range(size)) != magic_sum:
            return False

    # Check if the main diagonal sums to the magic sum
    if sum(M[i][i] for i in range(size)) != magic_sum:
        return False

    # Check if the anti-diagonal sums to the magic sum
    if sum(M[i][size - 1 - i] for i in range(size)) != magic_sum:
        return False
    
    print("The magic sum is:", magic_sum)  # If everything passes, print the magic sum
    return True  # The matrix is a magic square
    # PostConditions: Returns True if the matrix is a magic square, if not then False.

# Main program logic
try: 
    Value = (input("Please input a positive prime number integer between 5 and 19: "))
    Value = int(Value)
    if Value >= 5 and Value <= 19 and is_prime(Value):  # Check if the input meets the criteria
        result = generate_arrays(Value)  # Generate two arrays, A and B
        A, B = result
        print("Array A:", A)  # Print the randomly shuffled array A
        print("Array B:", B)  # Print the randomly shuffled array B
        
        # Check if adding the shifted square matrices of A and B forms a magic square
        if isMagic(addM(Make_Square(A, 2, Value), Make_Square(B, 3, Value))):
            print("The arrays create a magic square!!")
        else:
            print("The arrays do not create a magic square")
    else:
        print("This number did not meet the criteria...")  # Invalid input
except ValueError:
    print("Please enter an integer...")

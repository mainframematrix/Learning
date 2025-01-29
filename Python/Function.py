def hello():
    """
    Prints "Hello, World!
    """

    print("Hello, World!")


def hello_with_parameters(name: str):
    """
    Function that requires a parameter and prints a "Hello" message.
    """

    print("Hello, "+name+"!")

def return_hello(name: str):
    """
    Function that returns the string concatenated with the name parameter.
    """
    return "Hello, "+name+"!"

def recursive_factorial(num: int):
    """
    Function that uses recursion to find factorial of a number.
    """
    if(num<=1):
        return 1
    else:
        return num*recursive_factorial(num-1)
    
def functionA(numA: int):
    """
    Function that multiplies a number with 2.
    """
    print("FunctionA:\n")
    print("Number A*2: "+str(numA*2))
    return functionB(numA)

def functionB(numA: int):
    """
    Function that prints square of a number.
    """
    print("FunctionB:\n")
    print("Number A^2: "+str(numA**2))

if __name__ == "__main__":
    # Calling hello() function
    print("Calling hello() function...")
    hello()
    print("\n\n")
    # Calling hello_with_parameters(name: str) function
    print("Calling hello_with_parameters(name: str) function...")
    hello_with_parameters(name="Github")
    print("\n\n")
    # Calling return_hello(name: str) function
    print("Calling return_hello(name: str) function...")
    print(return_hello("Github"))
    print("\n\n")
    # Calling recursive_factorial(num: int) function
    print("Calling recursive_factorial(num: int) function...")
    print("Factorial of 5: " + str(recursive_factorial(5)))
    print("\n\n")
    # calling functionA that calls functionB
    print("Calling functionA that calls functionB...")
    functionA(numA=5)
    print("\n\n")
    
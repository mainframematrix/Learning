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


if __name__ == "__main__":
    hello()
    hello_with_parameters(name="Github")

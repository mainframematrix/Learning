class Dog:
    """
    A class that barks and remembers the number of times it barked.
    """

    def __init__(self):
        """
        Initializes the Dog Class.
        """
        self.count = 0

    def bark(self):
        """
        Prints "Woof!!"
        """
        self.count += 1
        print("Woof!!")

    def remember(self):
        """
        Remembers the number of times it barked!
        """
        print("I have barked "+str(self.count)+" times")


if __name__ == "__main__":
    dog = Dog()
    dog.bark()
    dog.bark()
    dog.remember()

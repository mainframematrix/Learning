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


class Animal_Hierarchical:
    def __init__(self):
        self.count = 0

    def remember(self):
        """
        Remembers the number of times it this its task!
        """
        print("I have "+self.task+"ed "+str(self.count)+" times")


class Dog_Hierarchical(Animal_Hierarchical):
    """
    A class that barks!
    """

    def __init__(self):
        """
        Initializes with parent class (i.e. Animal) and has a task to bark.
        """
        super().__init__()
        self.task = "bark"

    def bark(self):
        """
        Prints "Woof!!"
        """
        self.count += 1
        print("Woof!!")


class Cat_Hierarchical(Animal_Hierarchical):
    """
    A class that meows!
    """

    def __init__(self):
        """
        Initializes with parent class (i.e. Animal) and has a task to meow.
        """
        super().__init__()
        self.task = "meow"

    def meow(self):
        """
        Prints "Meow!!"
        """
        self.count += 1
        print("Meow!!")


if __name__ == "__main__":

    # Demonstate normal class call
    print("Demonstate normal class call")
    dog = Dog()
    dog.bark()
    dog.bark()
    dog.remember()
    print("\n\n")
    # Demonstrate class call with Hierarchical Inheritance.
    print("Demonstrate class call with Hierarchical Inheritance.")
    dog = Dog_Hierarchical()
    dog.bark()
    dog.bark()
    dog.remember()
    cat = Cat_Hierarchical()
    cat.meow()
    cat.remember()
    print("\n\n")

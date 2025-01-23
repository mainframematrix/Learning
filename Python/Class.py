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

class Animal_Simple():
    def __init__(self):
        self.count = 0

    def remember(self):
        """
        Remembers the number of times it this its task!
        """
        print("I have "+self.task+"ed "+str(self.count)+" times")

class Dog_Simple(Animal_Simple):
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

class Person:
    """
    A class about a person that stores name and age and introduces itself
    """
    def __init__(self, name: str, age: int):
        """
        Initializes class with name and age
        """
        self.name = name
        self.age = age
    def introduction(self):
        """
        Introduces itself
        """
        print("Hi! My name is "+self.name+" and I am "+str(self.age)+" years old!")

class Job:
    """
    A class about job
    """
    def __init__(self,company: str):
        """
        Initializes the class with a company name
        """
        self.company = company
    def jobdescription(self):
        """
        Describes where it works
        """
        print("I work in "+self.company+".")
        
class Employee(Person,Job):
    """
    A class that inherits properties of Person and Job.
    """
    def __init__(self,name: str, age: int, company: str):
        """
        Initializes a class with name, age and company name
        """
        Person.__init__(self,name=name,age=age)
        Job.__init__(self,company=company)
    def employeeintro(self):
        """
        Introduces itself and where it works
        """
        Person.introduction(self)
        Job.jobdescription(self)
    
class Plant:
    """
    A class for a plant
    """
    def __init__(self):
        """
        Initializes its origin from seed
        """
        self.origin="seed"
    def tellorigin(self):
        """
        Tells its origin
        """
        print("I originate from a seed")

class Tree(Plant):
    """
    A class for a tree
    """
    def __init__(self):
        """
        Initializes its origin from a plant and seed.
        """
        super().__init__()
        self.origin="plant"
    def tellorigin(self):
        """
        Tells its origin
        """
        print("I originated from a plant")
        return super().tellorigin()
    
class Fruit(Tree):
    """
    A class for a fruit
    """
    def __init__(self):
        """
        Initializes its origin from a tree, plant and seed.
        """
        super().__init__()
        self.origin = "Plant"
    def tellorigin(self):
        """
        Tells its origin
        """
        print("I originate from a Tree")
        return super().tellorigin()
    
if __name__ == "__main__":

    # Demonstate normal class call
    print("Demonstate normal class call")
    dog = Dog()
    dog.bark()
    dog.bark()
    dog.remember()
    print("\n\n")
    # Demonstate class call with simple inheritance
    print("Demonstate class call with simple inheritance")
    dog_simple = Dog_Simple()
    dog_simple.bark()
    dog_simple.bark()
    dog_simple.remember()
    print("\n\n")
    # Demonstrate class call with Hierarchical Inheritance.
    print("Demonstrate class call with Hierarchical Inheritance.")
    dog_hierarchical = Dog_Hierarchical()
    dog_hierarchical.bark()
    dog_hierarchical.bark()
    dog_hierarchical.remember()
    cat_hierarchical = Cat_Hierarchical()
    cat_hierarchical.meow()
    cat_hierarchical.remember()
    print("\n\n")
    # Demonstrate class call with Multiple Inheritance.
    print("Demonstrate class call with Multiple Inheritance.")
    employee = Employee(name="John",age=21,company="GitHub")
    employee.employeeintro()
    print("\n\n")
    # Demonstate class call with Multilevel Inheritance.
    print("Demonstate class call with Multilevel Inheritance.")
    fruit = Fruit()
    fruit.tellorigin()
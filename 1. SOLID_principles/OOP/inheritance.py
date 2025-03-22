# Inheritance Example
# BAD PRACTICE:
# - Deep inheritance hierarchies
# - Tight coupling between classes
# - Breaking "is-a" relationship
# - Inheritance for code reuse only


class BadVehicle:
    def start_engine(self):
        pass


class BadBoat(BadVehicle):  # Problematic: Not all boats have engines
    pass


# GOOD PRACTICE:
# - Clear "is-a" relationships
# - Proper method overriding
# - Using composition when appropriate
# - Shallow inheritance hierarchies
# Benefits:
# 1. Code reuse
# 2. Extensibility
# 3. Maintainability


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

    def get_info(self):
        return f"{self.name} is {self.age} years old"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def get_info(self):
        return f"{super().get_info()} and has {self.fur_color} fur"


class Dog(Mammal):
    def __init__(self, name, age, fur_color, breed):
        super().__init__(name, age, fur_color)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{super().get_info()}. It's a {self.breed}"


class Cat(Mammal):
    def __init__(self, name, age, fur_color, indoor=True):
        super().__init__(name, age, fur_color)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says Meow!"

    def get_info(self):
        habitat = "indoor" if self.indoor else "outdoor"
        return f"{super().get_info()}. It's an {habitat} cat"


class Horse(Mammal):
    def __init__(self, name, age, fur_color, breed):
        super().__init__(name, age, fur_color)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Neigh!"

    def get_info(self):
        return f"{super().get_info()}. It's a {self.breed} horse"


if __name__ == "__main__":
    dog = Dog("Buddy", 5, "brown", "Labrador")
    cat = Cat("Whiskers", 3, "gray", True)
    horse = Horse("Thunder", 7, "black", "Arabian")

    animals = [dog, cat, horse]
    for animal in animals:
        print(animal.get_info())
        print(animal.speak())
        print()

# Explanation of method extension and super() in this code:

# 1. Method Extension and Overriding:
#    - The 'speak()' method is declared in Animal class as an abstract method that subclasses must implement
#    - Dog class extends this functionality by providing its own implementation of 'speak()'
#    - When dog.speak() is called, it returns "Buddy says Woof!" - this is method overriding

# 2. Method Extension with super():
#    - The 'get_info()' method is defined in Animal class and returns basic information
#    - Mammal class extends this method by calling super().get_info() to get the base implementation and then adds fur color information
#    - Dog class further extends by calling super().get_info() to get Mammal's implementation and then adds breed information
#    - This creates a chain: Dog -> Mammal -> Animal

# 2-1. How super() works:
#    - super() returns a temporary object of the superclass, allowing access to its methods
#    - It automatically follows the Method Resolution Order (MRO)
#    - In Dog.get_info(), super() refers to Mammal
#    - In Mammal.get_info(), super() refers to Animal
#    - This allows for clean extension of parent methods without code duplication

# 3. Method Resolution Order:
#    - When dog.get_info() is called, Python first looks for the method in Dog class
#    - Inside Dog.get_info(), super().get_info() calls Mammal.get_info()
#    - Inside Mammal.get_info(), super().get_info() calls Animal.get_info()
#    - The result builds up as each method adds its own information to the string

# 4. Output:
#    - Buddy is 5 years old and has brown fur. It's a Labrador
#    - Buddy says Woof!

#    - Whiskers is 3 years old and has gray fur. It's an indoor cat
#    - Whiskers says Meow!

#    - Thunder is 7 years old and has black fur. It's a Arabian horse
#    - Thunder says Neigh!

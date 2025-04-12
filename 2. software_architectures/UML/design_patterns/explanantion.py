def greet(*args):
    for name in args:
        print(f"Hello, {name}!")


greet("Alice", "Bob", "Charlie")
# output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!


def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_profile(name="Alice", age=30, country="UK")
# output:
# name: Alice
# age: 30
# country: UK


def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


demo(1, 2, 3, a=10, b=20)
# output:
# args: (1, 2, 3)
# kwargs: {'a': 10, 'b': 20}


def add(a, b, c):
    return a + b + c


values = (1, 2, 3)
print(add(*values))  # → 6

options = {"a": 1, "b": 2, "c": 3}
print(add(**options))  # → 6


##########################################################


class MyClass:
    @classmethod
    def say_hello(cls):
        print(f"Hello from {cls.__name__}")


MyClass.say_hello()
# output:
# Hello from MyClass
# Using @classmethod, you can call something like MyClass.say_hello() without creating an instance.


class Greeter:
    def __call__(self, name):
        print(f"Hi, {name}!")


g = Greeter()
g("Bob")
# output:
# Hi, Bob!
# Using __call__, you can call an instance like a function.
# With g("Bob"), __call__ is executed.


##########################################################


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Woof!")


dog = Dog()
dog.speak()  # → "Woof!"


# @abstractmethod imposes the rule “subclasses(Dog) must implement speak()”.
# If Dog does not define speak(), an error will occur.
# Cannot use Animal() directly (cannot be instantiated)


##########################################################


class Printer:
    def nomalPrint(self, message):
        print(f"[Printer] {message}")


class Report:
    def set_printer(self, printer):
        self.printer = printer

    def display(self):
        self.printer.nomalPrint("Report content")


printer = Printer()
report = Report()
report.set_printer(printer)  # ← Here is the injection!
report.display()  # → [Printer] Report content


##########################################################


observers = ["Alice", "Bob"]


# Check if the same item is already on the list
def add_observer(observer):
    if observer not in observers:
        observers.append(observer)


add_observer("Charlie")
print(observers)  # → ['Alice', 'Bob', 'Charlie']
add_observer("Alice")
print(observers.count("Alice"))  # → 1


# ternary operator
x = 7
result = "OK" if x > 5 else "NG"
print(result)  # → OK


# Check if the variable is None
x = None
if x is None:
    print("x is None")  # → OK

y = []
if y is not None:
    print("y is not None")  # → OK


##########################################################

# list
fruits = ["apple", "banana"]

fruits.append("orange")
fruits.remove("banana")
print("apple" in fruits)

# set
colors = {"red", "blue"}

colors.add("green")
colors.remove("red")

# dictionary
user = {"name": "Alice", "age": 30}

user["email"] = "alice@example.com"
del user["age"]

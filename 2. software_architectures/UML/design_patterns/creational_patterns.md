# Creational Patterns in Python

Creational patterns deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

## 1. Factory Method Pattern

Factory Method defines an interface for creating objects but lets subclasses decide which class to instantiate.

```python
from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

# Concrete products
class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

# Creator interface
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

# Concrete creators
class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()

# Usage
def get_pet_sound(factory: AnimalFactory) -> str:
    animal = factory.create_animal()
    return animal.speak()

dog_factory = DogFactory()
cat_factory = CatFactory()

print(get_pet_sound(dog_factory))  # Output: Woof!
print(get_pet_sound(cat_factory))  # Output: Meow!
```

## 2. Abstract Factory Pattern

Abstract Factory provides an interface for creating families of related or dependent objects without specifying their concrete classes.

```python
from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass

# Concrete Products
class WindowsButton(Button):
    def paint(self) -> str:
        return "Rendering a Windows button"

class WindowsCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering a Windows checkbox"

class MacButton(Button):
    def paint(self) -> str:
        return "Rendering a macOS button"

class MacCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering a macOS checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Usage
def create_ui(factory: GUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())

windows_factory = WindowsFactory()
mac_factory = MacFactory()

print("Windows UI:")
create_ui(windows_factory)
print("\nmacOS UI:")
create_ui(mac_factory)
```

## 3. Builder Pattern

Builder lets you construct complex objects step by step. It's especially useful when you need to create an object with lots of possible configuration options.

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Pizza:
    size: str
    cheese: bool = False
    pepperoni: bool = False
    mushrooms: bool = False
    bacon: bool = False

class PizzaBuilder:
    def __init__(self, size: str):
        self.pizza = Pizza(size)

    def add_cheese(self) -> 'PizzaBuilder':
        self.pizza.cheese = True
        return self

    def add_pepperoni(self) -> 'PizzaBuilder':
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self) -> 'PizzaBuilder':
        self.pizza.mushrooms = True
        return self

    def add_bacon(self) -> 'PizzaBuilder':
        self.pizza.bacon = True
        return self

    def build(self) -> Pizza:
        return self.pizza

# Usage
pizza = (PizzaBuilder("large")
         .add_cheese()
         .add_pepperoni()
         .add_bacon()
         .build())

print(f"Pizza size: {pizza.size}")
print(f"Toppings: cheese={pizza.cheese}, pepperoni={pizza.pepperoni}, "
      f"mushrooms={pizza.mushrooms}, bacon={pizza.bacon}")
```

## 4. Prototype Pattern

Prototype lets you copy existing objects without making your code dependent on their classes.

```python
from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Document(Prototype):
    def __init__(self, name: str, content: list):
        self.name = name
        self.content = content

    def clone(self) -> 'Document':
        # Create a deep copy of the object
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"Document(name={self.name}, content={self.content})"

# Usage
original_doc = Document("Original", ["line 1", "line 2"])
copied_doc = original_doc.clone()
copied_doc.name = "Copy"
copied_doc.content.append("line 3")

print(original_doc)  # Original content unchanged
print(copied_doc)    # Modified copy
```

## 5. Dependency Injection Pattern

Dependency Injection is a technique whereby one object supplies the dependencies of another object.

```python
from abc import ABC, abstractmethod
from typing import Protocol

# Dependencies
class Database(Protocol):
    def save(self, data: str) -> None:
        pass

class Logger(Protocol):
    def log(self, message: str) -> None:
        pass

# Concrete implementations
class MySQLDatabase:
    def save(self, data: str) -> None:
        print(f"Saving data to MySQL: {data}")

class FileLogger:
    def save(self, message: str) -> None:
        print(f"Logging to file: {message}")

# Service using dependencies
class UserService:
    def __init__(self, database: Database, logger: Logger):
        self.database = database
        self.logger = logger

    def create_user(self, username: str) -> None:
        self.database.save(username)
        self.logger.log(f"User created: {username}")

# Usage
database = MySQLDatabase()
logger = FileLogger()
user_service = UserService(database, logger)
user_service.create_user("john_doe")
```

## When to Use Each Pattern

1. **Factory Method**

   - When you don't know ahead of time what class you need
   - When you want to delegate object creation to subclasses
   - When you want to provide users of your library a way to extend its internal components

2. **Abstract Factory**

   - When your code needs to work with various families of related products
   - When you want to provide a library of products without exposing their implementations
   - When you want to enforce certain product combinations

3. **Builder**

   - When you need to create complex objects step by step
   - When you want to create different representations of the same product
   - When you want to prevent "telescoping constructors"

4. **Prototype**

   - When your code shouldn't depend on the concrete classes of objects that you need to copy
   - When you want to reduce the number of subclasses that only differ in their initialization process
   - When you need to create copies of objects at runtime

5. **Dependency Injection**
   - When you want to make your code more modular and testable
   - When you want to reduce coupling between classes
   - When you want to make your code more flexible and maintainable

## Advantages and Disadvantages

### Advantages:

- Provides flexibility in object creation
- Promotes loose coupling
- Makes code more maintainable and testable
- Follows SOLID principles
- Helps manage complexity in object creation

### Disadvantages:

- Can increase code complexity
- May introduce too many classes
- Can be overkill for simple applications
- Requires careful planning and design
- May impact performance (especially with Prototype pattern)

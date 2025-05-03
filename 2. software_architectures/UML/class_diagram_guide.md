# UML Class Diagram Guide

## 1. Basic Characteristics

### Class Structure

A class in UML is represented by a rectangle divided into three sections:

1. **Class Name** (top section)
2. **Attributes** (middle section)
3. **Methods** (bottom section)

### Example: Animal Class

```
+------------------------+
|        Animal         |
+------------------------+
| - name: String        |
| - id: Integer         |
| - age: Integer        |
+------------------------+
| - setName()           |
| - eat()               |
+------------------------+
```

### Visibility Modifiers

- `+` Public: Accessible by any other class
- `-` Private: Only accessible within the same class
- `#` Protected: Accessible by same class and subclasses
- `~` Package/Default: Accessible within same package (rarely used)

## 2. Relationships

### 2.1 Inheritance

- Represented by an open arrow (▷)
- Shows "is-a" relationship
- Child classes inherit attributes and methods from parent class
- Example: Tortoise, Otter, SlowLoris inherit from Animal

```
      Animal
        ▲
        |
   +----+----+
   |    |    |
Tortoise Otter SlowLoris
```

### 2.2 Association

- Represented by a simple line (─)
- Shows basic relationship between classes
- Example: "Otter eats SeaUrchin"

```
Otter ─────── SeaUrchin
```

### 2.3 Aggregation

- Represented by an open diamond (◇)
- Shows "has-a" relationship where parts can exist independently
- Example: Tortoise can be part of a Creep (group)

```
Creep ◇─────── Tortoise
```

### 2.4 Composition

- Represented by a filled diamond (◆)
- Shows "contains" relationship where parts cannot exist without the whole
- Example: VisitorCenter contains Lobby and Bathroom

```
VisitorCenter ◆─────── Lobby
             ◆─────── Bathroom
```

## 3. Multiplicity

Specifies the number of instances of one class that can relate to another:

- `1` Exactly one
- `0..1` Zero or one (optional)
- `0..*` or `*` Zero or many
- `1..*` One or many
- `n` Specific number
- `n..m` Number range

## 4. Online Shopping Cart Example Analysis

The online shopping system demonstrates several key concepts:

### Class Hierarchy

```
       User
        ▲
        |
   +----+----+
   |         |
Customer  Administrator
```

### Key Components:

1. **User Class**

   - Base class with common attributes:
     - userId
     - password
     - loginStatus
     - registerDate
   - Common methods:
     - verifyLogin()

2. **Customer Class (inherits from User)**

   - Has composition relationships with:
     - ShoppingCart (one-to-one)
     - Order (one-to-many)
   - Customer deletion cascades to related objects

3. **Order Relationships**
   - One customer can have many orders (0..\*)
   - Each order belongs to exactly one customer (1)
   - Each order has exactly one OrderDetails (1)
   - Composition relationship with ShippingInfo

### Design Patterns Demonstrated:

1. **Inheritance**: User as base class
2. **Composition**: Customer-Order relationship
3. **Encapsulation**: Private attributes with public methods
4. **Single Responsibility**: Each class has a specific purpose

This structure ensures:

- Clear separation of concerns
- Data integrity through proper relationships
- Scalability for adding new features
- Maintainable codebase through proper encapsulation

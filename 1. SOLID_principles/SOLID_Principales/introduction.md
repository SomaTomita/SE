# Introduction to SOLID Principles

## What are SOLID Principles?

SOLID principles are a set of five design guidelines that help developers create maintainable and scalable software. These principles ensure that code remains adaptable, readable, and easy to modify as requirements change over time.

## Why SOLID Principles Matter

Consider a Food Delivery App that constantly evolves with new features like real-time tracking, personalized promotions, and additional payment options. Without structured design principles, adding new functionality might break existing features, making maintenance difficult. SOLID principles help prevent these problems.

## The Five SOLID Principles

### 1. Single Responsibility Principle (SRP)

**Definition**: A class should have only one reason to change.

**Example**: Instead of having a single `DeliveryService` class that handles driver assignments, order status updates, and payment processing, separate these responsibilities into distinct classes:

- `OrderManager`
- `DeliveryScheduler`
- `PaymentProcessor`

**Benefit**: When payment processing needs to change, you can modify only the `PaymentProcessor` without risking effects on delivery assignments or order management.

### 2. Open/Closed Principle (OCP)

**Definition**: Software entities should be open for extension but closed for modification.

**Example**: For payment methods in our food delivery app:

- Create a `PaymentMethod` interface
- Implement separate classes for each payment type: `CreditCardPayment`, `WalletPayment`, `CryptoPayment`

**Benefit**: New payment methods can be added without modifying existing code, reducing the risk of introducing bugs.

### 3. Liskov Substitution Principle (LSP)

**Definition**: Subtypes must be substitutable for their base types without altering the correctness of the program.

**Example**: If all delivery drivers need to navigate to destinations:

- Create an abstract `Courier` class with appropriate navigation methods
- Implement `BicycleCourier` and `CarDriver` with navigation strategies suitable for their transportation modes

**Benefit**: Any courier type can be used interchangeably where the base type is expected, preventing unexpected failures.

### 4. Interface Segregation Principle (ISP)

**Definition**: No client should be forced to depend on methods it does not use.

**Example**: Instead of a single `UserInterface` with methods for all user types:

- Create separate interfaces: `CustomerInterface` and `RestaurantInterface`
- Each user type implements only relevant functionality

**Benefit**: Classes only implement methods they actually need, keeping the system modular and preventing unnecessary dependencies.

### 5. Dependency Inversion Principle (DIP)

**Definition**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Example**: For database access:

- Define a `DatabaseInterface`
- Implement concrete classes like `SQLDatabase` and `NoSQLDatabase`
- Have `OrderManager` depend on the interface, not concrete implementations

**Benefit**: The system becomes more flexible and adaptable to changes, such as switching database technologies.

## Practical Application

When applying SOLID principles to your projects:

1. Identify distinct responsibilities and separate them
2. Design for extension through interfaces and abstractions
3. Ensure subclasses maintain expected behaviors
4. Create focused interfaces that serve specific needs
5. Depend on abstractions rather than concrete implementations

These small improvements in design lead to significant long-term benefits in code maintainability, testability, and adaptability to changing requirements.

## Practice Questions

### Question 1

What is the primary objective of the Single Responsibility Principle (SRP)?

- [ ] To ensure that each class has multiple reasons to change
- [ ] To enforce strict dependencies between all classes in a system
- [ ] To allow a class to handle multiple functionalities to improve efficiency
- [x] To limit a class to only one reason to change, improving maintainability

**Explanation**: The Single Responsibility Principle states that a class should have only one reason to change. This means each class should have a single, well-defined responsibility, making the code more maintainable, easier to understand, and less prone to bugs when changes are needed.

### Question 2

Match each SOLID principle to its correct description:

Single Responsibility Principle:

- [x] A class should only have one reason to change

Open/Closed Principle:

- [x] Software entities should be open for extension but closed for modification

Liskov Substitution Principle:

- [x] A subclass should be replaceable for its parent class without affecting correctness

Interface Segregation Principle:

- [x] An interface should have only the methods relevant to the specific client that implements it

Dependency Inversion Principle:

- [x] High-level modules should not depend on low-level modules; both should depend on abstractions

**Explanation**: Each SOLID principle addresses a specific aspect of software design:

- SRP focuses on maintaining single responsibility
- OCP enables extension without modification
- LSP ensures proper inheritance behavior
- ISP prevents interface pollution
- DIP promotes loose coupling through abstractions

### Question 3

The Interface Segregation Principle states that large, general-purpose interfaces are preferable over smaller, more specific ones to ensure flexibility in software design.

- [ ] True
- [x] False

**Explanation**: This statement is false. The Interface Segregation Principle (ISP) actually advocates for the opposite: interfaces should be small, specific, and focused on the needs of the clients that use them. Large, general-purpose interfaces often force clients to implement methods they don't need, creating unnecessary dependencies.

### Question 4

A developer is designing an online food delivery application. The PaymentProcessor class handles all payment transactions, including card payments, digital wallets, and cash-on-delivery validation. As the application scales, new payment methods must be added frequently. Which SOLID principle should be applied to make this system more maintainable?

- [ ] Interface Segregation Principle – ensure that payment services implement only relevant methods
- [x] Open/Closed Principle – create an abstraction for different payment types
- [ ] Liskov Substitution Principle – ensure all payments inherit the same base behaviour
- [ ] Single Responsibility Principle – separate concerns within the class

**Explanation**: The Open/Closed Principle (OCP) is most applicable here because it allows for adding new payment methods without modifying existing code. By creating an abstract payment interface or base class, new payment methods can be added by creating new classes that implement this interface, rather than modifying the existing PaymentProcessor class.

## Summary

These practice questions help reinforce your understanding of SOLID principles and their practical applications in software design. Remember that while each principle has its specific focus, they work together to create more maintainable, flexible, and robust software systems.

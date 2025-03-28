# Software Architecture Summary Quiz

## Questions and Answers

### Question 1

The Open/Closed Principle states that software should be open for modification but closed for extension.

**Answer: False**

**Explanation:**
The Open/Closed Principle (OCP) actually states that software entities should be:

- Open for extension (can add new functionality)
- Closed for modification (existing code shouldn't need to be changed)

For example, when adding a new payment method to a food delivery app:

- Good OCP: Adding a new payment class that implements an existing payment interface
- Poor OCP: Modifying existing payment processing code to handle the new method

### Question 2

A food delivery app needs to notify customers when their order status changes. Which design pattern is best suited for this?

**Answer: Observer Pattern**

**Explanation:**
The Observer Pattern is ideal for this scenario because:

- It allows objects (customers) to be notified automatically when a state change occurs (order status)
- It maintains loose coupling between the order system and notification system
- It can handle multiple types of notifications (SMS, email, app notifications) without modifying the order system
- It's specifically designed for one-to-many dependencies where a change in one object needs to be reflected in multiple other objects

### Question 3

Which of the following techniques improve system performance? (Select all that apply)

**Correct Answers:**

- Caching
- Efficient database indexing
- Load balancing

**Explanation:**
These techniques improve performance in different ways:

- Caching: Reduces database load by storing frequently accessed data in memory
- Efficient database indexing: Speeds up data retrieval by optimizing query paths
- Load balancing: Distributes traffic across multiple servers to prevent bottlenecks

Using synchronous processing for all tasks would actually decrease performance by blocking operations that could run in parallel.

### Question 4

Which software architecture style is most suitable for applications that require loose coupling and scalability?

**Answer: Microservices Architecture**

**Explanation:**
Microservices Architecture is ideal for loose coupling and scalability because:

- Services can be developed, deployed, and scaled independently
- Each service has its own database and can use appropriate technology
- Services communicate through well-defined APIs
- Failures in one service don't directly affect others
- New features can be added by creating new services without modifying existing ones

### Question 5

The Factory Method Pattern is a creational design pattern used to organize relationships between classes.

**Answer: True**

**Explanation:**
The Factory Method Pattern:

- Creates objects without exposing the instantiation logic
- Refers to the newly created object through a common interface
- Allows subclasses to alter the type of objects that will be created
- Helps maintain loose coupling between object creation and object usage

For example, a food delivery app might use a factory method to create different types of payment processors without the ordering system needing to know the specific payment class being instantiated.

### Question 6

What is the primary purpose of software architecture in system development?

**Answer: To define the high-level structure of a software system and its interactions**

**Explanation:**
Software architecture:

- Provides a blueprint for system organization
- Defines how components interact with each other
- Establishes technical constraints and system characteristics
- Influences scalability, maintainability, and performance
- Guides development teams in implementing the system

### Question 7

Layered architecture always improves performance.

**Answer: False**

**Explanation:**
Layered architecture doesn't automatically improve performance because:

- Requests must traverse multiple layers, which can add latency
- Each layer transition involves some processing overhead
- Strict layer separation might prevent performance optimizations
- The benefits of layered architecture (maintainability, separation of concerns) often come at the cost of some performance overhead

### Question 8

A financial application must ensure all transactions are processed correctly even if a server crashes. What architecture pattern is best suited?

**Answer: Event-Driven Architecture**

**Explanation:**
Event-Driven Architecture is best suited because:

- It can persist events until they are successfully processed
- It supports event sourcing for transaction recovery
- It enables asynchronous processing with guaranteed delivery
- It can maintain transaction consistency across system failures
- Events can be replayed to rebuild system state after crashes

### Question 9

Which software architecture style is most suitable for applications that require high availability and fault tolerance?

**Answer: Microservices Architecture**

**Explanation:**
Microservices Architecture provides high availability and fault tolerance through:

- Independent deployment and scaling of services
- Isolation of failures to specific services
- Ability to run multiple instances of critical services
- Easy implementation of circuit breakers and fallbacks
- Support for rolling updates without system downtime

### Question 10

Which of the following are advantages of using a client-server architecture? (Select all that apply)

**Correct Answers:**

- Scalability
- Centralized Management
- Enhanced Security

**Explanation:**
Client-server architecture provides these advantages:

- Scalability: Server capacity can be increased independently of clients
- Centralized Management: Resources and security can be managed from a central location
- Enhanced Security: Sensitive data and business logic can be protected on the server

Reduced Network Traffic is not an advantage, as client-server communication often increases network traffic compared to local processing.

## Additional Study Tips

1. Focus on understanding the practical applications of each architecture style
2. Practice identifying scenarios where different patterns would be most appropriate
3. Consider the trade-offs between different architectural approaches
4. Study real-world examples of successful architecture implementations
5. Remember that there's rarely a "perfect" architecture - choices depend on specific requirements and constraints
6.

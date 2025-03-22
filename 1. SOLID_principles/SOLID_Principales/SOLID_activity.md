# SOLID Principles Activity: Food Delivery Application

## Scenario: Food Delivery Application

You are tasked with designing a Food Delivery App, where customers place orders, delivery drivers pick them up, and restaurants prepare meals. The system must handle:

- Customer order management
- Payment processing
- Delivery assignment
- Customer notifications

## Step 1: Identifying Non-SOLID Code Issues

### Original Code Problems

```python
class FoodDeliveryApp:
    def __init__(self):
        self.orders = []
        self.drivers = ['Alice', 'Bob', 'Charlie']

    def place_order(self, customer_name, food_item, payment_method):
        # Process order and payment
        print(f"Processing order for {customer_name}: {food_item}")
        if payment_method == 'card':
            print("Processing card payment...")
        elif payment_method == 'cash':
            print("Cash on delivery selected.")
        else:
            print("Invalid payment method!")
            return

        self.orders.append((customer_name, food_item))
        print(f"Order placed successfully for {customer_name}.")

        # Assign delivery driver
        assigned_driver = self.drivers[0]  # Always assigns the first driver
        print(f"{assigned_driver} will deliver the order.")

        # Send notification
        print(f"Notification sent to {customer_name}: Your order is on the way!")


app = FoodDeliveryApp()
app.place_order("John Doe", "Pizza", "card")
```

## Step 2: Identify SOLID Violations

Before refining the code, identify which SOLID principles are being violated and why:

1. **Single Responsibility Principle (SRP)**

   - Which responsibilities are mixed in a single class?
   - How are different concerns intermingled?

2. **Open/Closed Principle (OCP)**

   - What parts of the code will require modification for every new feature?
   - How is the code resistant to extension?

3. **Liskov Substitution Principle (LSP)**

   - Are all objects correctly substitutable?
   - Can derived classes be used in place of their base classes?

4. **Interface Segregation Principle (ISP)**

   - Does the class enforce unnecessary dependencies?
   - Are interfaces too broad or forcing unnecessary implementations?

5. **Dependency Inversion Principle (DIP)**
   - Are high-level modules dependent on low-level implementations?
   - How can we better use abstractions?

Write down your observations before moving to the next step.

## Step 3: Improve the Code to Follow SOLID Principles

Modify the code structure to align with SOLID principles by improving the design without changing its core functionality. Focus on breaking down responsibilities, and making the system more maintainable and scalable.

### Hints for Improvement:

1. **SRP**: Split the design into separate classes

   - Create distinct classes for order management, payment processing, and delivery coordination

2. **OCP**: Use abstraction for payment methods

   - Implement interfaces for payment processing
   - Allow new payment methods without modifying existing code

3. **LSP**: Ensure proper substitution

   - Make sure derived classes can replace base classes without issues
   - Maintain consistent behavior across inheritance hierarchies

4. **ISP**: Avoid unnecessary method enforcement

   - Create specific interfaces for different types of users
   - Split large interfaces into smaller, focused ones

5. **DIP**: Focus on abstractions
   - Depend on interfaces rather than concrete implementations
   - Use dependency injection where appropriate

## Step 4: Reflect on Your Changes

After improving the solution, reflect on the improvements:

1. **How has breaking down the code improved its maintainability?**

   - Each class has a well-defined role
   - Modifications can be made without unintended side effects
   - Code is more organized and easier to understand
   - Testing becomes more straightforward with isolated components

2. **What SOLID principles were most useful in improving the design?**

   - SRP ensured separation of concerns
   - OCP allowed future expansion without modification
   - DIP ensured flexibility and reduced coupling

3. **How does the new design allow for future enhancements?**
   - New payment methods can be added without modifying existing code
   - Additional delivery options can be introduced seamlessly
   - New notification types can be implemented independently
   - Reduced likelihood of introducing errors during updates

### Final Thoughts

Applying SOLID principles is not about rigidly following a formula but about making thoughtful design choices that improve software quality. The provided solution is one way to approach the problem, but alternative implementations may also be valid. Creativity and adaptability are key to writing effective software.

Key takeaways:

- SOLID principles are guidelines, not strict rules
- Different solutions can be equally valid
- Focus on improving maintainability and scalability
- Consider future requirements when designing
- Balance between perfect design and practical implementation

Take time to review your solution and reflect on how these principles can be applied to future projects.

## Model Answer

While there is no single prescriptive way to apply SOLID principles, improving the structure of the code requires thoughtful design choices. The goal is not just to fix issues but to develop a maintainable, scalable, and adaptable solution. Below is an improved version of the code, addressing the identified SOLID violations.

### Violations and Solutions

#### 1. Single Responsibility Principle (SRP) Violation

- The FoodDeliveryApp class handles order processing, payment processing, driver assignment, and notifications. This made the class difficult to maintain and extend.
- **Solution**: Create separate classes for each responsibility:
  - OrderProcessor
  - PaymentProcessor
  - DeliveryService
  - NotificationService

#### 2. Open/Closed Principle (OCP) Violation

- Payment method logic was hardcoded inside place_order(), requiring modifications whenever a new payment method was introduced.
- **Solution**: Use a PaymentProcessor interface with specific implementations for:
  - CardPayment
  - CashPayment
  - Future payment options

#### 3. Liskov Substitution Principle (LSP) Violation

- If different types of delivery (e.g., drone delivery) were added, the current structure would not support easy substitution without breaking functionality.
- **Solution**: Introduce an abstract DeliveryMethod class to allow new delivery types without modifying existing code.

#### 4. Dependency Inversion Principle (DIP) Violation

- The FoodDeliveryApp class was tightly coupled to concrete implementations, making future changes difficult.
- **Solution**: Introduce abstraction layers, where high-level modules depend on interfaces rather than specific implementations.

### Improved Code Following SOLID Principles

```python
# Applying SRP: Separate concerns into individual classes
class Order:
    def __init__(self, customer_name, food_item):
        self.customer_name = customer_name
        self.food_item = food_item

# Applying OCP & DIP: Using abstraction for payment methods
class PaymentProcessor:
    def process_payment(self, payment_method):
        raise NotImplementedError("Subclasses must implement process_payment method")

class CardPayment(PaymentProcessor):
    def process_payment(self):
        print("Processing card payment...")
        return True

class CashPayment(PaymentProcessor):
    def process_payment(self):
        print("Cash on delivery selected.")
        return True

# Applying LSP: Abstracting delivery types
class DeliveryMethod:
    def assign_driver(self):
        raise NotImplementedError("Subclasses must implement assign_driver method")

class DriverDelivery(DeliveryMethod):
    def __init__(self):
        self.drivers = ['Alice', 'Bob', 'Charlie']

    def assign_driver(self):
        assigned_driver = self.drivers[0]  # Placeholder assignment logic
        print(f"{assigned_driver} will deliver the order.")
        return assigned_driver

# Applying SRP: Separate Notification Service
class NotificationService:
    def send_notification(self, customer_name):
        print(f"Notification sent to {customer_name}: Your order is on the way!")

# The main application class follows DIP by depending on abstractions
class FoodDeliveryApp:
    def __init__(self):
        self.orders = []
        self.notification_service = NotificationService()

    def place_order(self, customer_name, food_item, payment_method):
        order = Order(customer_name, food_item)
        payment_processor = CardPayment() if payment_method == 'card' else CashPayment()

        if not payment_processor.process_payment():
            return

        self.orders.append(order)
        print(f"Order placed successfully for {customer_name}.")

        delivery = DriverDelivery()
        assigned_driver = delivery.assign_driver()
        self.notification_service.send_notification(customer_name)


app = FoodDeliveryApp()
app.place_order("John Doe", "Pizza", "card")
```

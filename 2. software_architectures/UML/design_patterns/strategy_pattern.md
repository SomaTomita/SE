# Strategy Pattern in Python

## What is Strategy Pattern?

The Strategy Pattern is a behavioral design pattern that enables you to define a family of algorithms, encapsulate each one, and make them interchangeable. It lets the algorithm vary independently from clients that use it.

Key characteristics:

- Defines a family of algorithms
- Encapsulates each algorithm
- Makes algorithms interchangeable
- Promotes loose coupling between the algorithm and the code that uses the algorithm

## Basic Implementation

Here's a basic implementation of the Strategy Pattern in Python:

```python
from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, expiry: str):
        self.card_number = card_number
        self.expiry = expiry

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using Credit Card ending with {self.card_number[-4:]}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using PayPal account: {self.email}")

# Context
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self, price: float):
        self.items.append(price)

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def checkout(self):
        total = sum(self.items)
        if not self.payment_strategy:
            raise Exception("Please set a payment strategy")
        self.payment_strategy.pay(total)

# Usage
cart = ShoppingCart()
cart.add_item(100)
cart.add_item(50)

# Pay with credit card (Strategy 1)
cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456", "12/25"))
cart.checkout()  # Output: Paid $150 using Credit Card ending with 3456

# Pay with PayPal (Strategy 2)
cart.set_payment_strategy(PayPalPayment("user@example.com"))
cart.checkout()  # Output: Paid $150 using PayPal account: user@example.com
```

## Real-World Example: Data Compression

Here's a more practical example showing different compression strategies:

```python
from abc import ABC, abstractmethod
import json
import pickle
import yaml

class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, data: dict) -> str:
        pass

    @abstractmethod
    def decompress(self, data: str) -> dict:
        pass

class JSONCompression(CompressionStrategy):
    def compress(self, data: dict) -> str:
        return json.dumps(data)

    def decompress(self, data: str) -> dict:
        return json.loads(data)

class PickleCompression(CompressionStrategy):
    def compress(self, data: dict) -> str:
        return pickle.dumps(data).hex()

    def decompress(self, data: str) -> dict:
        return pickle.loads(bytes.fromhex(data))

class YAMLCompression(CompressionStrategy):
    def compress(self, data: dict) -> str:
        return yaml.dump(data)

    def decompress(self, data: str) -> dict:
        return yaml.safe_load(data)

class DataManager:
    def __init__(self, compression_strategy: CompressionStrategy):
        self.compression_strategy = compression_strategy

    def save_data(self, data: dict) -> str:
        return self.compression_strategy.compress(data)

    def load_data(self, compressed_data: str) -> dict:
        return self.compression_strategy.decompress(compressed_data)
```

## When to Use Strategy Pattern

The Strategy pattern is useful in scenarios where:

1. You need to use different variants of an algorithm within an object
2. You have a lot of similar classes that only differ in their behavior
3. You need to isolate the algorithm logic from the code that uses the algorithm
4. You need to switch algorithms at runtime

Common use cases:

- Sorting algorithms
- Payment processing methods
- Data compression/serialization
- Authentication strategies
- File export formats

## Advantages and Disadvantages

### Advantages:

- Algorithms can be switched at runtime
- Isolates algorithm implementation details from code that uses the algorithm
- Promotes the Open/Closed Principle
- Makes code more maintainable and extensible
- Enables better unit testing of algorithms

### Disadvantages:

- Can increase complexity with many strategies
- Clients must be aware of different strategies
- Increased number of classes in the application
- Overkill for simple algorithm variations

## Best Practices

1. Use the Strategy pattern when you have a family of similar algorithms
2. Make sure the strategies are interchangeable
3. Consider using function objects or lambda expressions for simple strategies
4. Keep the strategy interface simple
5. Make strategies stateless when possible
6. Use dependency injection to provide strategies to clients

## Example Use Case: Sorting Strategies

Here's another practical example showing different sorting strategies:

```python
from typing import List

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass

class BubbleSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class QuickSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        arr = data.copy()
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort_data(self, data: List[int]) -> List[int]:
        return self.strategy.sort(data)

# Usage
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sorter = Sorter(BubbleSort())
quick_sorter = Sorter(QuickSort())

print(bubble_sorter.sort_data(data))  # Using bubble sort
print(quick_sorter.sort_data(data))   # Using quick sort
```

## Conclusion

The Strategy pattern is a powerful tool for managing algorithms in your application. It provides a clean way to encapsulate different implementations of an algorithm and make them interchangeable. While it may add some complexity to your code, the benefits of flexibility, maintainability, and testability often outweigh the costs. When implementing the Strategy pattern, focus on creating clear interfaces and ensuring that strategies are truly interchangeable from the client's perspective.

# Adapter Pattern in Python

## What is Adapter Pattern?

The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to collaborate. It acts as a wrapper between two objects, catching calls for one object and transforming them to format and interface recognizable by the second object.

Key characteristics:

- Converts the interface of a class into another interface clients expect
- Allows classes to work together that couldn't otherwise because of incompatible interfaces
- Wraps an existing class with a new interface
- Acts as a bridge between two incompatible interfaces

## Basic Implementation

Here's a basic implementation of the Adapter Pattern in Python:

```python
from abc import ABC, abstractmethod

# Target Interface (What the client expects)
class Target(ABC):
    @abstractmethod
    def request(self) -> str:
        pass

# Adaptee (The class that needs adapting)
class Adaptee:
    def specific_request(self) -> str:
        return "Adaptee's specific request"

# Adapter
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        # Translate the Target interface into Adaptee interface
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()}"

# Client code
def client_code(target: Target) -> None:
    print(target.request())

# Usage
adaptee = Adaptee()
adapter = Adapter(adaptee)
client_code(adapter)  # Output: Adapter: (TRANSLATED) Adaptee's specific request
```

## Real-World Example: Third-Party Payment Integration

Here's a practical example showing how to adapt different payment systems:

```python
from abc import ABC, abstractmethod
from typing import Dict

# Our application's payment interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

# Third-party payment services (Adaptees)
class StripePaymentService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def create_charge(self, amount: float, currency: str, token: str) -> Dict:
        # Simulate Stripe API call
        print(f"Stripe: Charging ${amount} to token {token}")
        return {"status": "success", "amount": amount, "currency": currency}

class PayPalPaymentService:
    def make_payment(self, amount: float, paypal_email: str) -> bool:
        # Simulate PayPal API call
        print(f"PayPal: Sending ${amount} to {paypal_email}")
        return True

# Adapters
class StripePaymentAdapter(PaymentProcessor):
    def __init__(self, stripe_service: StripePaymentService, token: str):
        self.stripe_service = stripe_service
        self.token = token

    def process_payment(self, amount: float) -> bool:
        response = self.stripe_service.create_charge(
            amount=amount,
            currency="USD",
            token=self.token
        )
        return response["status"] == "success"

class PayPalPaymentAdapter(PaymentProcessor):
    def __init__(self, paypal_service: PayPalPaymentService, email: str):
        self.paypal_service = paypal_service
        self.email = email

    def process_payment(self, amount: float) -> bool:
        return self.paypal_service.make_payment(amount, self.email)

# Client code
class OnlineStore:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount: float):
        if self.payment_processor.process_payment(amount):
            print("Payment successful!")
        else:
            print("Payment failed!")

# Usage
stripe_service = StripePaymentService(api_key="sk_test_123")
stripe_adapter = StripePaymentAdapter(stripe_service, token="tok_123")

paypal_service = PayPalPaymentService()
paypal_adapter = PayPalPaymentAdapter(paypal_service, email="user@example.com")

# Store can work with any payment processor through the adapter
store = OnlineStore(stripe_adapter)
store.checkout(100.0)
# output:
# Stripe: Charging $100.0 to token tok_123
# Payment successful!

store.payment_processor = paypal_adapter
store.checkout(50.0)
# output:
# PayPal: Sending $50.0 to user@example.com
# Payment successful!

```

## When to Use Adapter Pattern

The Adapter pattern is useful in scenarios where:

1. You want to use an existing class, but its interface isn't compatible with your code
2. You need to reuse several existing subclasses that lack common functionality
3. You need to integrate a third-party library without modifying its code
4. You want to create a reusable class that cooperates with classes that don't have compatible interfaces

Common use cases:

- Third-party library integration
- Legacy system integration
- Multiple API compatibility
- Data format conversion
- Cross-platform compatibility

## Advantages and Disadvantages

### Advantages:

- Separates interface or data conversion code from the core business logic
- Introduces new adapters without breaking existing code
- Improves reusability of existing code
- Provides a way to integrate incompatible systems
- Follows Single Responsibility Principle

### Disadvantages:

- Increases overall code complexity
- Sometimes it's better to change the service class to match the rest of your code
- Can be confusing to maintain if there are multiple adapters
- May introduce additional processing overhead

## Best Practices

1. Use the Adapter pattern when you want to reuse existing code with an incompatible interface
2. Keep adapters simple - they should only handle interface translation
3. Consider using the Adapter pattern when working with legacy code
4. Document clearly what the adapter is translating and why
5. Use composition over inheritance when possible
6. Consider creating a common interface for multiple adapters

## Example Use Case: Data Format Conversion

Here's another practical example showing format conversion:

```python
from abc import ABC, abstractmethod
from typing import Dict
import json
import xml.etree.ElementTree as ET

# Target Interface
class DataParser(ABC):
    @abstractmethod
    def parse(self, data: str) -> Dict:
        pass

# Concrete implementation for JSON
class JSONParser(DataParser):
    def parse(self, data: str) -> Dict:
        return json.loads(data)

# Adaptee - XML Parser with different interface
class XMLParserService:
    def parse_xml(self, xml_string: str) -> ET.Element:
        return ET.fromstring(xml_string)

    def get_values(self, element: ET.Element) -> Dict:
        result = {}
        for child in element:
            result[child.tag] = child.text
        return result

# Adapter
class XMLToJSONAdapter(DataParser):
    def __init__(self, xml_parser: XMLParserService):
        self.xml_parser = xml_parser

    def parse(self, data: str) -> Dict:
        xml_tree = self.xml_parser.parse_xml(data)
        return self.xml_parser.get_values(xml_tree)

# Client code
class DataProcessor:
    def __init__(self, parser: DataParser):
        self.parser = parser

    def process_data(self, data: str) -> Dict:
        return self.parser.parse(data)

# Usage
json_data = '{"name": "John", "age": "30"}'
xml_data = '''
<person>
    <name>John</name>
    <age>30</age>
</person>
'''

# Process JSON
json_parser = JSONParser()
processor = DataProcessor(json_parser)
print(processor.process_data(json_data))

# Process XML using adapter
xml_parser_service = XMLParserService()
xml_adapter = XMLToJSONAdapter(xml_parser_service)
processor = DataProcessor(xml_adapter)
print(processor.process_data(xml_data))
```

## Conclusion

The Adapter pattern is a crucial tool for integrating incompatible interfaces and making existing code work with new systems. While it adds a layer of complexity, it provides a clean way to make incompatible interfaces work together without modifying their source code. When implementing the Adapter pattern, focus on keeping the adaptation logic simple and clear, and document the purpose of each adapter thoroughly.

# Observer Pattern in Python

## What is Observer Pattern?

The Observer Pattern is a behavioral design pattern that defines a one-to-many dependency between objects. When one object (the subject/publisher) changes its state, all its dependents (observers/subscribers) are notified and updated automatically.

Key characteristics:

- Defines one-to-many relationship between objects
- Loose coupling between subject and observers
- Supports broadcast communication
- Observers can be added or removed dynamically
- Subject doesn't need to know observer details

## Basic Implementation

Here's a basic implementation of the Observer Pattern in Python:

```python
from abc import ABC, abstractmethod
from typing import List

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify() # Run _observers

# Concrete Observers
class CurrentConditionsDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Current conditions: {temperature}F degrees and {humidity}% humidity")

class StatisticsDisplay(Observer):
    def __init__(self):
        self._temperatures: List[float] = []

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperatures.append(temperature)
        avg_temp = sum(self._temperatures) / len(self._temperatures)
        print(f"Avg/Max/Min temperature = {avg_temp:.1f}/{max(self._temperatures)}/{min(self._temperatures)}")

# Usage
weather_station = WeatherStation()
current_display = CurrentConditionsDisplay()
statistics_display = StatisticsDisplay()
# Register two display panels for monitoring
weather_station.attach(current_display)
weather_station.attach(statistics_display)

weather_station.set_measurements(80, 65, 30.4)
weather_station.set_measurements(82, 70, 29.2)
# output
# Current conditions: 80F degrees and 65% humidity
# Avg/Max/Min temperature = 80.0/80/80

# Current conditions: 82F degrees and 70% humidity
# Avg/Max/Min temperature = 81.0/82/80

weather_station.detach(current_display)
weather_station.set_measurements(85, 75, 29.8)
# output
# Avg/Max/Min temperature = 82.3/85/80

```

## Real-World Example: News Agency

Here's a practical example showing a news agency notifying subscribers:

```python
from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime

# Observer interface
class NewsSubscriber(ABC):
    @abstractmethod
    def receive_news(self, news: Dict) -> None:
        pass

# Subject
class NewsAgency:
    def __init__(self):
        self._subscribers: List[NewsSubscriber] = []
        self._latest_news: Dict = {}

    def add_subscriber(self, subscriber: NewsSubscriber) -> None:
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: NewsSubscriber) -> None:
        self._subscribers.remove(subscriber)

    def publish_news(self, category: str, news: str) -> None:
        self._latest_news = {
            'category': category,
            'news': news,
            'timestamp': datetime.now()
        }
        self._notify_subscribers()

    def _notify_subscribers(self) -> None:
        for subscriber in self._subscribers:
            subscriber.receive_news(self._latest_news)

# Concrete Observers
class EmailSubscriber(NewsSubscriber):
    def __init__(self, email: str):
        self.email = email

    def receive_news(self, news: Dict) -> None:
        print(f"Sending news to {self.email}:")
        print(f"Category: {news['category']}")
        print(f"News: {news['news']}")
        print(f"Time: {news['timestamp']}\n")

class MobileAppSubscriber(NewsSubscriber):
    def __init__(self, user_id: str):
        self.user_id = user_id

    def receive_news(self, news: Dict) -> None:
        print(f"Pushing notification to user {self.user_id}:")
        print(f"{news['category']}: {news['news']}\n")

# Usage
news_agency = NewsAgency()

# Create subscribers
email_sub = EmailSubscriber("user@example.com")
app_sub = MobileAppSubscriber("USER_123")

# Add subscribers to news agency
news_agency.add_subscriber(email_sub)
news_agency.add_subscriber(app_sub)

# Publish news
news_agency.publish_news("Technology", "New AI breakthrough announced!")
news_agency.publish_news("Sports", "Local team wins championship!")
```

## When to Use Observer Pattern

The Observer pattern is useful in scenarios where:

1. When a change to one object requires changing others, and you don't know how many objects need to be changed
2. When an object should be able to notify other objects without making assumptions about who these objects are
3. When you need to maintain consistency between related objects without making them tightly coupled
4. When the dependency relationship between objects can change dynamically

Common use cases:

- Event handling systems
- News feed implementations
- Stock market monitoring
- User interface updates
- Real-time data monitoring
- Publish-subscribe systems

## Advantages and Disadvantages

### Advantages:

- Loose coupling between subject and observers
- Support for broadcast communication
- Dynamic relationships can be established at runtime
- Abstract coupling between subject and observer
- Observers can be added/removed at any time

### Disadvantages:

- Memory leaks if observers are not properly unregistered
- Random order of notification
- Potential performance issues with many observers
- Unexpected updates if observers are not properly managed
- Complex update logic can lead to cascading updates

## Best Practices

1. Use the Observer pattern when changes in one object require changes in others
2. Consider using weak references to prevent memory leaks
3. Implement a mechanism to handle observer removal properly
4. Keep the update interface simple
5. Consider using event channels for complex notification schemes
6. Be cautious with cascading updates

## Example Use Case: Stock Market Monitor

Here's another practical example showing stock market monitoring:

```python
from abc import ABC, abstractmethod
from typing import Dict, List
from datetime import datetime

class StockObserver(ABC):
    @abstractmethod
    def update(self, stock_data: Dict) -> None:
        pass

class StockMarket:
    def __init__(self):
        self._observers: List[StockObserver] = []
        self._stocks: Dict[str, float] = {}

    def add_observer(self, observer: StockObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: StockObserver) -> None:
        self._observers.remove(observer)

    def update_stock(self, symbol: str, price: float) -> None:
        old_price = self._stocks.get(symbol)
        self._stocks[symbol] = price

        stock_data = {
            'symbol': symbol,
            'price': price,
            'old_price': old_price,
            'timestamp': datetime.now()
        }
        self._notify_observers(stock_data)

    def _notify_observers(self, stock_data: Dict) -> None:
        for observer in self._observers:
            observer.update(stock_data)

class StockPriceDisplay(StockObserver):
    def update(self, stock_data: Dict) -> None:
        print(f"Stock Price Update: {stock_data['symbol']} = ${stock_data['price']:.2f}")

class PriceAlertSystem(StockObserver):
    def __init__(self, threshold: float):
        self.threshold = threshold

    def update(self, stock_data: Dict) -> None:
        if stock_data['old_price'] is not None:
            price_change = ((stock_data['price'] - stock_data['old_price']) / stock_data['old_price']) * 100
            if abs(price_change) > self.threshold:
                print(f"ALERT: {stock_data['symbol']} price changed by {price_change:.2f}%")

# Usage
stock_market = StockMarket()

# Create observers
price_display = StockPriceDisplay()
alert_system = PriceAlertSystem(threshold=5.0)  # Alert on 5% change

# Add observers
stock_market.add_observer(price_display)
stock_market.add_observer(alert_system)

# Update stock prices
stock_market.update_stock("AAPL", 150.0)
stock_market.update_stock("AAPL", 160.0)  # This will trigger alert
stock_market.update_stock("GOOGL", 2800.0)
```

## Conclusion

The Observer pattern is a powerful tool for implementing distributed event handling systems. It provides a way to establish loose coupling between objects while maintaining consistency when state changes occur. While it can introduce complexity in terms of managing observers and updates, the benefits of flexibility and maintainability often outweigh these challenges. When implementing the Observer pattern, focus on proper observer management and clear update interfaces to avoid common pitfalls.

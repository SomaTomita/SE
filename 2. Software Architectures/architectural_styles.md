# Software Architecture Styles

## Introduction

Software architecture defines how different components of a system interact, shaping its scalability, maintainability, and performance. Architectural styles refer to predefined structures that dictate how software components are organized and interact with each other. They provide standardized approaches to solving common architectural challenges.

Choosing the right architectural style is crucial in building robust, adaptable software. This document explores key architectural styles using a Food Delivery App scenario to illustrate their strengths, trade-offs, and best use cases.

## Why Understanding Architectural Styles Matters

Software systems are becoming increasingly complex, and the way they are structured has a direct impact on their performance, scalability, and maintainability. Choosing the right architectural style can mean the difference between a system that grows and adapts seamlessly and one that struggles under pressure.

Imagine a food delivery app that must process thousands of orders per minute, track real-time deliveries, and integrate with various payment and mapping services. Different architectural styles would handle these challenges in distinct ways, each with its own advantages and limitations.

## 1. Layered Architecture

[An example with meat and potatoes](https://qiita.com/c0ridrew/items/41f0566b676d8092a9fb)

```
food_delivery_app/
│
├── app/
│   ├── api/                      # Presentation Layer (REST API endpoints)
│   │   ├── v1/
│   │   │   ├── orders.py
│   │   │   ├── users.py
│   │   │   └── restaurants.py
│   │   └── __init__.py
│   │
│   ├── services/                # Application Layer (Business orchestration)
│   │   ├── order_service.py
│   │   ├── user_service.py
│   │   └── restaurant_service.py
│   │
│   ├── domain/                  # Domain Layer (Entities, domain logic)
│   │   ├── models/
│   │   │   ├── order.py
│   │   │   ├── user.py
│   │   │   └── restaurant.py
│   │   └── exceptions.py
│   │
│   ├── infrastructure/         # Infrastructure Layer (DB, APIs)
│   │   ├── db/
│   │   │   ├── repositories/
│   │   │   │   ├── order_repo.py
│   │   │   │   └── user_repo.py
│   │   │   └── database.py
│   │   └── external/
│   │       └── payment_gateway.py
│   │
│   └── main.py                 # Entry point
│
├── tests/                      # Test modules
│   ├── unit/
│   ├── integration/
│   └── conftest.py
│
├── requirements.txt
└── README.md
```

Layered architecture structures a system into separate, hierarchical layers, each responsible for a distinct aspect of the application. This separation enhances maintainability, reusability, and modularity, making it easier to modify or extend the system without disrupting other components.

### Implementation in the Food Delivery App

1. **Presentation Layer** - Handles user interactions through interfaces such as mobile apps, web applications, or APIs.

   - Example: When a customer opens the app and navigates through restaurant options, this layer manages the UI components, input validation, and initial request formatting.
   - Specific components might include the order screen, restaurant browsing interface, and checkout process.

2. **Business Logic Layer** - Contains the core functionality of the application.

   - Example: When a customer places an order for a pizza, this layer processes the order details, calculates delivery fees based on distance, applies relevant promotions (like "20% off on first order"), and handles restaurant assignment based on proximity and capacity.
   - This layer would include services like OrderProcessingService, PromotionService, and RestaurantAssignmentService.

3. **Data Layer** - Manages interactions with databases.
   - Example: After an order is processed, this layer stores the order details in the database, updates the restaurant's current order queue, and retrieves the customer's saved addresses for delivery options.
   - Components would include OrderRepository, CustomerRepository, and RestaurantRepository.

### Strengths and Trade-offs

**Strengths:**

- **Improved maintainability**: Changes to the database structure only affect the data layer, not the business logic.
- **Enhanced modularity**: Each layer can be developed, tested, and maintained independently.
- **Simplified debugging**: Issues can be isolated to specific layers.
- **Clear separation of concerns**: Developers can specialize in specific layers.

**Trade-offs:**

- **Performance overhead**: Requests must traverse multiple layers, potentially causing latency.
- **Rigid structure**: May be overly structured for simple applications.
- **Potential for tight coupling**: Lower layers might become dependent on upper layers if not carefully designed.

### Reflection

Would a layered approach work if the food delivery app needed instant real-time tracking of orders? While the layered architecture provides good organization, it might introduce latency due to the need for requests to pass through multiple layers. For real-time tracking, this architecture would need to be complemented with technologies like WebSockets or server-sent events to push updates directly to clients, potentially bypassing some layers for time-sensitive operations.

## 2. Client-Server Architecture

```
food_delivery_app_client_server/
│
├── server/                          # Server-side code (API backend)
│   ├── app/
│   │   ├── controllers/
│   │   │   └── order_controller.py
│   │   ├── services/
│   │   │   └── order_service.py
│   │   ├── models/
│   │   │   └── order.py
│   │   └── repositories/
│   │       └── order_repository.py
│   ├── database/
│   │   └── db.py
│   ├── requirements.txt
│   └── main.py
│
└── client/                          # Client-side code (command-line/web/mobile)
    ├── api_client.py
    ├── main.py
    └── requirements.txt

```

Client-server architecture is a widely used model in software development where clients (e.g., mobile apps, web browsers) request services from a central server, which processes the requests and returns responses. This architecture is foundational in modern distributed systems, ensuring efficient data management and structured communication between users and backend processes.

### Implementation in the Food Delivery App

1. A customer places an order for dinner via the client (mobile app or website).
2. The request is sent to the server, which:
   - Processes the order details
   - Verifies payment through a payment gateway
   - Identifies available restaurants based on location and cuisine
   - Assigns a delivery driver based on proximity
3. The server sends a response back to the client with:
   - Order confirmation number
   - Estimated preparation and delivery time
   - Real-time tracking information

This structured interaction ensures that all user requests are managed centrally, allowing for streamlined processes. For example, when multiple customers order from the same restaurant, the server can optimize delivery routes and restaurant workload.

### Strengths and Trade-offs

**Strengths:**

- **Centralized control**: All business logic and data management occur on the server, ensuring consistency.
- **Simpler client implementation**: Clients focus on presentation, reducing complexity in mobile apps.
- **Efficient data management**: Server can optimize database queries and cache common requests.
- **Easier security enforcement**: Authentication and authorization are managed centrally.

**Trade-offs:**

- **Scalability limitations**: As user numbers grow, the server can become a bottleneck.
- **Single point of failure**: If the server goes down, the entire system becomes unavailable.
- **Network dependency**: Requires stable internet connection for operation.
- **Latency issues**: Users in distant locations may experience delays.

### Reflection

If the central server experiences a high number of requests during peak hours (like dinner time), the system could be optimized through:

- **Load balancing**: Distributing requests across multiple server instances
- **Caching**: Storing frequently accessed data (like restaurant menus) to reduce database queries
- **Queue management**: Prioritizing critical operations (payment processing) over less time-sensitive ones
- **Regional servers**: Deploying servers in different geographical locations to reduce latency
- **Auto-scaling**: Automatically adding server capacity during peak hours

## 3. Event-Driven Architecture

```
food_delivery_app_event_driven/
│
├── producer/                      # Event producers (API or frontend triggers)
│   ├── order_api.py
│   └── requirements.txt
│
├── consumer/                      # Event consumers (workers handling events)
│   ├── order_processor.py
│   ├── notification_service.py
│   └── requirements.txt
│
├── events/                        # Shared event definitions
│   └── order_events.py
│
├── broker/                        # Message broker configuration
│   └── docker-compose.yml
│
└── README.md

```

Event-driven architecture responds to events (e.g., order placed, payment completed) in real-time, using an event broker to manage communication between components. This architecture excels in scenarios requiring real-time updates and loose coupling between services.

### Implementation in the Food Delivery App

1. **Order Placement Event Flow**:

   - When a customer places an order, the Order Service publishes an "OrderPlaced" event to the event broker.
   - The Payment Service, subscribed to "OrderPlaced" events, receives the notification and initiates payment processing.
   - Once payment is complete, the Payment Service publishes a "PaymentCompleted" event.
   - The Restaurant Service, listening for "PaymentCompleted" events, receives the notification and adds the order to the restaurant's queue.
   - The Notification Service sends a confirmation message to the customer.

2. **Delivery Event Flow**:
   - When the restaurant marks an order as ready, it publishes an "OrderReady" event.
   - The Delivery Service assigns a nearby driver and publishes a "DriverAssigned" event.
   - The Tracking Service begins monitoring the driver's location and publishes location updates.
   - The Notification Service keeps the customer informed about delivery progress.

This architecture enables real-time communication between different services without tight coupling. For example, if the app adds a new loyalty points system, it can simply subscribe to relevant events without modifying existing services.

### Strengths and Trade-offs

**Strengths:**

- **Highly responsive**: Events are processed as they occur, enabling real-time updates.
- **Loose coupling**: Services don't need direct knowledge of each other, only the events they care about.
- **Scalability**: Services can be scaled independently based on event volume.
- **Flexibility**: New features can be added by creating new services that subscribe to existing events.

**Trade-offs:**

- **Debugging complexity**: Tracing the flow of events across services can be challenging.
- **Event consistency**: Ensuring events are processed in the correct order requires careful design.
- **Eventual consistency**: The system may temporarily be in an inconsistent state as events propagate.
- **Monitoring challenges**: Requires sophisticated monitoring to ensure all events are properly processed.

### Reflection

Event-driven architecture would be highly beneficial for handling surge pricing during peak demand. When the system detects high order volume in a specific area, it could publish a "DemandSurge" event. Pricing services would respond by calculating new delivery fees, while notification services could alert available drivers to the high-demand area. This reactive approach allows the system to respond dynamically to changing conditions without requiring direct communication between components.

## 4. Service-Oriented Architecture (SOA)

```
food_delivery_app_soa/
│
├── services/
│   ├── order_service/
│   │   ├── app/
│   │   │   ├── api.py
│   │   │   ├── models.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   ├── requirements.txt
│   │   └── main.py
│   │
│   ├── user_service/
│   │   ├── app/
│   │   │   ├── api.py
│   │   │   ├── models.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   ├── requirements.txt
│   │   └── main.py
│   │
│   ├── restaurant_service/
│   │   └── ...
│   │
│   └── payment_service/
│       └── ...
│
├── shared/
│   ├── lib/
│   │   └── http_client.py         # Generic REST client for service-to-service calls
│   └── schemas/
│       └── common_models.py       # Shared DTOs / data contracts
│
├── gateway/
│   ├── api_gateway.py             # Optionally a central entry point (reverse proxy or BFF)
│   └── config.yaml
│
└── docker-compose.yml            # Orchestrates all services

```

SOA structures software as a collection of interoperable services that communicate via standardized protocols, ensuring reusability and integration across different platforms.

### Implementation in the Food Delivery App

1. **External Service Integration**:

   - **Google Maps API**: Provides route optimization, calculating the most efficient delivery paths based on traffic conditions and distance.

     - Example: When a new order comes in, the system queries Google Maps to estimate delivery time and suggest optimal routes to drivers.

   - **Payment Gateway Service**: Handles secure financial transactions through providers like Stripe or PayPal.

     - Example: When a customer selects "Pay with credit card," the request is routed to the payment service, which communicates with the external payment processor.

   - **SMS Gateway Service**: Sends text notifications to customers and drivers.
     - Example: When an order status changes, the notification service uses the SMS gateway to send updates.

2. **Internal Service Organization**:
   - **Order Management Service**: Coordinates the entire order lifecycle.
   - **Customer Management Service**: Handles user profiles, preferences, and history.
   - **Restaurant Management Service**: Manages restaurant information, menus, and availability.
   - **Delivery Management Service**: Coordinates driver assignments and tracking.

Unlike microservices, SOA often uses a centralized Enterprise Service Bus (ESB) for communication between services, making it a better fit for enterprise applications with complex integration needs.

### Strengths and Trade-offs

**Strengths:**

- **Service reusability**: Common functionalities can be exposed as services used across the organization.
- **Standardized integration**: Well-defined interfaces make it easier to connect with external systems.
- **Technology agnostic**: Services can be implemented in different technologies as long as they adhere to the interface contract.
- **Business alignment**: Services often map to business capabilities, making the architecture more intuitive for stakeholders.

**Trade-offs:**

- **Governance complexity**: Requires strong governance to manage service contracts and dependencies.
- **Performance overhead**: The ESB can become a bottleneck if not properly designed.
- **Integration challenges**: Ensuring consistent data models across services requires careful planning.
- **Development complexity**: Designing effective service boundaries requires deep domain knowledge.

### Reflection

SOA differs from microservices in several key ways:

- **Service granularity**: SOA services tend to be larger, often encompassing entire business domains, while microservices are more fine-grained.
- **Communication**: SOA typically uses an ESB for service communication, while microservices prefer direct service-to-service communication.
- **Deployment**: SOA services are often deployed together, while microservices are independently deployable.

In the food delivery app, both could be used together: SOA could handle enterprise-wide concerns and external integrations (payment processing, mapping), while microservices could manage specific business functions (order processing, restaurant management) that require frequent updates and independent scaling.

## 5. Microservices Architecture

```
food_delivery_app_microservices/
│
├── services/
│   ├── order_service/                 # Handles order placement & tracking
│   │   ├── app/
│   │   │   ├── api.py
│   │   │   ├── models.py
│   │   │   ├── service.py
│   │   │   └── db.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── user_service/                  # Handles registration, login, profile
│   ├── restaurant_service/           # Manages menu, restaurant data
│   ├── payment_service/              # Handles payments
│   ├── notification_service/         # Sends emails/SMS
│   └── delivery_service/             # Handles courier matching & tracking
│
├── gateway/                           # API Gateway / BFF
│   ├── main.py
│   ├── config.yaml
│   └── Dockerfile
│
├── shared_libs/                       # Shared protobufs, HTTP clients, auth logic
│   ├── auth/
│   ├── http/
│   └── schemas/
│
├── infrastructure/
│   ├── monitoring/                    # Prometheus/Grafana setup
│   ├── logging/                       # ELK stack config
│   └── service_mesh/                  # e.g., Istio or Linkerd
│
├── docker-compose.yml                 # Service orchestration for local dev
└── README.md

```

Microservices architecture breaks down a system into small, independently deployable services that communicate via APIs. Each service focuses on a specific business capability and can be developed, deployed, and scaled independently.

### Implementation in the Food Delivery App

1. **Order Service**:

   - Handles order creation, modification, and status tracking
   - Maintains its own database of orders
   - Exposes REST APIs for order operations
   - Example: When a customer places an order, this service validates the items, creates an order record, and initiates the order workflow

2. **Payment Service**:

   - Processes payments through various methods (credit cards, digital wallets)
   - Maintains payment records and transaction history
   - Communicates with external payment gateways
   - Example: When an order is confirmed, this service charges the customer's selected payment method and issues receipts

3. **Restaurant Service**:

   - Manages restaurant profiles, menus, and availability
   - Handles restaurant-side order acceptance and preparation status
   - Example: Notifies restaurants of new orders and allows them to update preparation status

4. **Delivery Service**:

   - Assigns drivers to orders based on location and availability
   - Tracks delivery progress in real-time
   - Optimizes delivery routes
   - Example: When an order is ready for pickup, this service identifies the nearest available driver and provides navigation instructions

5. **User Service**:

   - Manages customer profiles, addresses, and preferences
   - Handles authentication and authorization
   - Example: Stores customer delivery addresses and payment preferences for quick reuse

6. **Notification Service**:
   - Sends updates to customers, restaurants, and drivers
   - Supports multiple channels (push notifications, SMS, email)
   - Example: Alerts customers when their order is accepted, being prepared, and out for delivery

Each service operates independently with its own database, allowing teams to work in parallel and deploy updates without affecting other services.

### Strengths and Trade-offs

**Strengths:**

- **Independent deployment**: Services can be updated individually without system-wide downtime.
- **Technology diversity**: Different services can use different technologies based on specific requirements.
- **Scalability**: High-demand services can be scaled independently without scaling the entire system.
- **Team autonomy**: Small teams can own specific services, enabling faster development cycles.
- **Fault isolation**: Failures in one service don't necessarily affect others.

**Trade-offs:**

- **Distributed system complexity**: Managing service discovery, communication, and data consistency becomes challenging.
- **Operational overhead**: Monitoring and maintaining multiple services requires sophisticated DevOps practices.
- **Network latency**: Inter-service communication adds latency compared to monolithic applications.
- **Data consistency**: Maintaining consistency across service boundaries requires careful design.
- **Testing complexity**: End-to-end testing becomes more difficult with multiple independent services.

### Reflection

If the payment service fails in a microservices architecture, customers would be unable to complete new orders, but existing orders in progress would continue to be prepared and delivered. This partial system failure is actually an advantage over monolithic systems where a single component failure might bring down the entire application.

To improve fault tolerance:

1. **Circuit breakers**: Implement patterns that prevent cascading failures when a service is down
2. **Fallback mechanisms**: Provide alternative paths when a service is unavailable (e.g., queue payments for later processing)
3. **Redundancy**: Deploy multiple instances of critical services across different regions
4. **Asynchronous communication**: Use message queues to buffer requests during service outages
5. **Health monitoring**: Implement sophisticated monitoring to detect and respond to service failures quickly

## Reflection and Progression

### Hybrid Approaches

Most real-world systems don't strictly adhere to a single architectural style but combine elements from different approaches. For example, a food delivery app might use:

- **Microservices** for core business functions that need independent scaling (orders, payments)
- **Event-driven patterns** for real-time features (delivery tracking, notifications)
- **Layered architecture** within individual services for code organization
- **SOA principles** for integration with external systems (maps, payment gateways)

### Evolving Architecture

Systems often evolve their architecture as requirements change:

1. **Starting simple**: A new food delivery startup might begin with a monolithic application to quickly enter the market.
2. **Scaling challenges**: As the user base grows, the monolith becomes difficult to scale and maintain.
3. **Strategic decomposition**: The company gradually extracts high-value or problematic components into separate services.
4. **Continuous evolution**: Architecture continues to adapt as business requirements and technologies change.

### Decision Factors

When choosing an architectural style, consider:

1. **Business requirements**: Does the system need real-time updates? High availability? Rapid feature development?
2. **Team structure**: Do you have multiple teams that need to work independently?
3. **Scalability needs**: Which components need to scale independently?
4. **Development velocity**: How frequently do you need to deploy changes?
5. **Operational capabilities**: Does your team have experience managing distributed systems?

### International Expansion Considerations

If our food delivery app expanded internationally, architectural considerations would include:

1. **Data residency**: Some countries require customer data to be stored locally, potentially requiring region-specific databases.
2. **Regulatory compliance**: Different payment processing requirements might necessitate specialized payment services per region.
3. **Localization**: Services would need to support multiple languages, currencies, and regional preferences.
4. **Performance**: Regional deployment of services would reduce latency for users in different geographical areas.
5. **Offline capabilities**: In regions with less reliable internet, the app might need enhanced offline functionality.

A microservices architecture would be particularly advantageous for international expansion, as it would allow for:

- Region-specific service instances with local customizations
- Independent scaling based on regional demand patterns
- Gradual rollout to new markets without affecting existing operations
- Compliance with varying regulatory requirements through specialized service variants

## Conclusion

Architectural styles provide frameworks for organizing software systems, each with distinct advantages and limitations. Understanding these patterns helps software engineers make informed decisions that align with business goals and technical requirements.

The most successful systems often combine elements from multiple architectural styles, creating hybrid approaches tailored to specific needs. As systems grow and evolve, architecture must adapt accordingly, sometimes transitioning between styles to address changing requirements.

By considering factors such as scalability, maintainability, development velocity, and operational complexity, engineers can select architectural approaches that position their systems for long-term success.

```

```

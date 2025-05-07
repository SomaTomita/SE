# Canvas Learning Platform Architecture Analysis

## Question : (maximum of 300 words)

### Scenario

Canvas is designing a new collaborative learning platform to serve students and instructors worldwide.
The system must support:

- Rapid scaling during peak usage periods (e.g., exam seasons),
- Fast real-time communication between users across multiple regions,
- High system resilience and availability, even in the event of partial network failures.

The organisation is evaluating whether a Peer-to-Peer (P2P) architecture or a Microservices architecture would better meet these goals.

### Task

Critically compare P2P and microservices architectures in the context of Canvas's new platform goals.
For each system quality attribute:

- Scalability
- Latency
- Fault Tolerance

You should:

- Explain how each architecture supports or limits the quality in the context of Canvas goals.
- Critically compare and contrast the architectural approaches, highlighting trade-offs and operational impacts.
- Reflect on which architecture would be preferable for Canvas, based on its system goals and deployment environment.

### Marking Criteria

- Scalability: Clear comparison under Canvas's scaling needs, 4 marks
- Latency: Clear comparison under Canvas's real-time communication needs, 4 marks
- Fault Tolerance: Clear comparison under Canvas's high-availability requirement, 4 marks

## Answer

For Canvas’s global collaborative learning platform, microservices architecture offers a more reliable and scalable foundation than peer-to-peer (P2P), especially when considering the demands of real-time interaction, global access, and operational resilience.

Scalability is a core requirement. Microservices, deployed via orchestration platforms like Kubernetes, allow Canvas to scale individual components—such as exam or messaging services—based on real-time usage metrics. This enables the platform to dynamically accommodate exam-season surges without overloading auxiliary services, optimizing both performance and cost. In contrast, P2P systems scale through peer participation, but this model struggles with predictability and control during synchronized global usage spikes, where many users demand the same service simultaneously.

In terms of latency, microservices enable geographically distributed deployments supported by edge computing and CDNs. This helps maintain consistent sub-100ms response times for interactive tools like group chat or collaborative editing. Service meshes and intelligent load balancing further reduce communication overhead. Although P2P can offer low-latency direct connections in local contexts, it becomes unreliable in global deployments due to NAT traversal issues, peer churn, and inconsistent network quality.

When it comes to fault tolerance, microservices provide clear boundaries for failure isolation and recovery through mechanisms like circuit breakers, redundancy, and fallback routines. For example, if the assessment module fails, it can degrade gracefully without affecting authentication or messaging services. While P2P systems benefit from decentralization, their resilience depends heavily on peer availability, which is difficult to guarantee during critical synchronous events like live lectures or online exams.

Overall, microservices offer Canvas more deterministic control, global consistency, and operational transparency—qualities that align closely with its platform’s performance, resilience, and user experience goals.

(300 words)

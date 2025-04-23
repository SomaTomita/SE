# Distributed Systems and Cloud Computing Quiz

## Question 1: Primary Challenges in Distributed Systems

**Question:** Which of the following is a primary challenge in designing distributed systems?

**Options:**

- Ensuring data consistency across nodes
- Reducing energy consumption
- Limited processing power
- Eliminating network communication

**Correct Answer:** Ensuring data consistency across nodes

**Detailed Explanation:**

1. **Why Data Consistency is Critical:**

   ```python
   # Example of consistency challenge in distributed systems
   class DistributedCache:
       def update_value(self, key, value):
           # Challenge: Ensure all nodes see this update in the same order
           for node in self.nodes:
               try:
                   node.update(key, value, timestamp)
               except NetworkPartitionError:
                   # What happens to consistency when this fails?
                   self.handle_partition()
   ```

2. **Technical Challenges:**

   - Race conditions between concurrent updates
   - Network partitions affecting synchronization
   - Clock skew between different nodes
   - Eventual vs. Strong consistency trade-offs

3. **Real-world Impact:**

   - Banking systems: Account balances must be consistent
   - E-commerce: Inventory counts must be accurate
   - Social media: User feeds must reflect current state

4. **Why Other Options are Less Critical:**
   - Energy consumption: Important but not fundamental to distribution
   - Processing power: Can be scaled horizontally
   - Network communication: Essential, not to be eliminated

## Question 2: Cloud Service Provider Selection

**Question:** Which of the following factors influence the choice of a cloud service provider? (Select all that apply)

**Options:**

- Geographical location of users (without considering latency concerns)
- Service level agreements (SLAs)
- Cost structure
- Security and compliance requirements

**Correct Answers:**

- Service level agreements (SLAs)
- Cost structure
- Security and compliance requirements

**Detailed Explanation:**

1. **Service Level Agreements (SLAs):**

   ```yaml
   # Example SLA requirements
   service_requirements:
     availability: 99.99%
     response_time: <200ms
     data_durability: 99.999999999%
     recovery_time: <15 minutes
   ```

2. **Cost Structure Analysis:**

   ```python
   def calculate_cloud_costs(provider):
       return {
           'compute': usage_hours * provider.compute_rate,
           'storage': data_volume * provider.storage_rate,
           'network': data_transfer * provider.network_rate,
           'additional_services': sum(service.cost for service in provider.services)
       }
   ```

3. **Security & Compliance:**
   - Data sovereignty requirements
   - Industry-specific regulations (HIPAA, GDPR, etc.)
   - Encryption standards
   - Access control mechanisms

## Question 3: Distributed System Definition

**Question:** In a \***\*\_\*\*** system, multiple independent computers work together as a single unit to provide a unified service.

**Answer:** distributed

**Detailed Explanation:**

1. **Key Components:**

   ```python
   class DistributedSystem:
       def __init__(self):
           self.nodes = []
           self.service_registry = {}
           self.load_balancer = LoadBalancer()

       def add_node(self, node):
           self.nodes.append(node)
           self.rebalance_workload()

       def provide_unified_service(self, request):
           # Hide complexity from users
           node = self.load_balancer.get_next_node()
           return node.process_request(request)
   ```

2. **Essential Characteristics:**
   - Node Independence
   - Unified Interface
   - Coordinated Operation
   - Shared Resources

## Question 4: Microservices Architecture

**Question:** Microservices architecture reduces system complexity by centralising all functionality into a single service.

**Options:**

- True
- False

**Correct Answer:** False

**Detailed Explanation:**

1. **Actual Microservices Principle:**

   ```yaml
   # Example microservices architecture
   services:
     auth-service:
       build: ./auth
       scale: 3

     payment-service:
       build: ./payment
       scale: 2

     inventory-service:
       build: ./inventory
       scale: 4
   ```

2. **Benefits of Distribution:**

   - Independent scaling
   - Technology flexibility
   - Fault isolation
   - Team autonomy

3. **Complexity Management:**
   - Service boundaries based on business domains
   - Clear interfaces between services
   - Independent deployment cycles

## Question 5: Cloud Deployment Concerns

**Question:** Which of the following is NOT a typical concern when deploying applications in a cloud environment?

**Options:**

- Latency issues
- Vendor lock-in
- Data security risks
- Lack of scalability

**Correct Answer:** Lack of scalability

**Detailed Explanation:**

1. **Actual Cloud Concerns:**

   ```python
   class CloudDeployment:
       def assess_risks(self):
           return {
               'latency': self.measure_network_latency(),
               'vendor_lock_in': self.analyze_provider_dependencies(),
               'security': self.audit_security_measures(),
               'scalability': 'Actually a strength, not a concern'
           }
   ```

2. **Why Scalability is Not a Concern:**
   - Auto-scaling capabilities
   - Elastic resource allocation
   - Pay-as-you-go model
   - Global infrastructure availability

## Question 6: Blockchain Architecture

**Question:** Which distributed system model is best suited for decentralised applications like blockchain?

**Options:**

- Client-Server
- Peer-to-Peer
- Monolithic
- Multi-Tier

**Correct Answer:** Peer-to-Peer

**Detailed Explanation:**

1. **P2P Architecture Benefits:**

   ```python
   class BlockchainNode:
       def __init__(self):
           self.peers = set()
           self.blockchain = []

       def broadcast_transaction(self, transaction):
           # Each node is equal and can validate
           for peer in self.peers:
               peer.receive_transaction(transaction)

       def validate_block(self, block):
           # Decentralized consensus
           return self.consensus_algorithm.validate(block)
   ```

2. **Key Characteristics:**
   - No central authority
   - Equal peer relationships
   - Distributed consensus
   - Shared ledger

## Question 7: Cloud Migration Considerations

**Question:** Which of the following considerations impact cloud migration decisions? (Select all that apply.)

**Options:**

- Data transfer costs
- Application architecture compatibility
- Proximity to office locations
- Security and compliance

**Correct Answers:**

- Data transfer costs
- Application architecture compatibility
- Security and compliance

**Detailed Explanation:**

1. **Cost Analysis:**

   ```python
   def calculate_migration_costs(app):
       return {
           'data_transfer': app.data_size * transfer_rate,
           'refactoring': estimate_architecture_changes(app),
           'security': implement_security_measures(app),
           'training': staff_training_costs
       }
   ```

2. **Architecture Considerations:**
   - Monolithic vs. microservices
   - Database compatibility
   - API dependencies
   - Stateful vs. stateless design

## Question 8: Cloud Computing Advantages

**Question:** Match each cloud computing advantage with its correct description.

**Pairs:**

- Elasticity → Resources can be scaled up or down based on demand
- Cost Efficiency → Pay-as-you-go pricing reduces upfront investment
- Redundancy → Ensures system availability even in case of failures
- Global Reach → Cloud services are accessible from anywhere in the world

**Detailed Explanation:**

1. **Elasticity Implementation:**

   ```python
   class AutoScaler:
       def adjust_resources(self, metrics):
           if metrics.load > threshold:
               self.scale_up()
           elif metrics.load < threshold:
               self.scale_down()
   ```

2. **Cost Models:**
   - Pay per use
   - Reserved instances
   - Spot instances
   - Bulk discounts

## Question 9: E-commerce System Strategy

**Question:** A multinational e-commerce company experiences significant delays in processing orders during high-traffic events, such as seasonal sales. Which strategy would best help manage increased workload while maintaining performance and reliability?

**Options:**

- Implementing load balancing across multiple servers
- Reducing the number of users accessing the system simultaneously
- Using a single powerful server to handle all transactions
- Storing all transactions in a single centralised database

**Correct Answer:** Implementing load balancing across multiple servers

**Detailed Explanation:**

1. **Load Balancing Implementation:**

   ```python
   class LoadBalancer:
       def distribute_request(self, request):
           available_servers = self.get_healthy_servers()
           selected_server = self.algorithm.select(
               servers=available_servers,
               request=request,
               current_load=self.get_load_metrics()
           )
           return selected_server.process(request)
   ```

2. **Benefits:**
   - Even distribution of traffic
   - Automatic failover
   - Optimal resource utilization
   - Improved response times

## Question 10: Distributed System Challenges

**Question:** Match each challenge with its most appropriate solution:

**Pairs:**

- Network Latency → Use caching and content delivery networks (CDNs)
- Single Point of Failure → Implement redundancy and failover mechanisms
- Data Inconsistency → Use distributed consensus algorithms like Paxos or Raft
- Overloaded Nodes → Implement auto-scaling and load balancing

**Detailed Explanation:**

1. **Solution Implementations:**

   ```python
   class DistributedSystemSolutions:
       def handle_latency(self):
           return self.cdn.serve_from_edge_location()

       def prevent_failure(self):
           return self.failover.switch_to_backup()

       def ensure_consistency(self):
           return self.consensus.reach_agreement()

       def manage_load(self):
           return self.auto_scaler.adjust_capacity()
   ```

2. **Best Practices:**
   - Multiple availability zones
   - Regular health checks
   - Automated recovery procedures
   - Proactive monitoring

## References

- Distributed Systems: Principles and Paradigms
- Cloud Computing: Concepts, Technology & Architecture
- Designing Data-Intensive Applications

# Kanban Methodology

## Introduction

Kanban ("signboard" or "visual signal" in Japanese) is a visual workflow management method designed to help teams improve efficiency and maintain a steady flow of work. Originating from lean manufacturing at Toyota, it has evolved into a powerful methodology for software development and project management.

## Core Principles

_Source: [what-is-kanban-system-benefits-and-drawbacks-explained](https://asana.com/ja/resources/what-is-kanban)_

1. **Visualize the Workflow**

   - Use Kanban board to represent work items
   - Example: A software team's board columns
     - Backlog
     - In Development
     - Code Review
     - Testing
     - Ready for Deploy
     - Done
   - Why it helps:
     - Everyone can see what's being worked on
     - Easy to understand team progress
     - Clear view of who is doing what

2. **Limit Work in Progress (WIP)**

   - Set maximum items per stage
   - Example: Development column limited to 3 items
     - Prevents overloading developers
     - Ensures focus on completion
     - Reduces context switching
   - Why it helps:
     - Team can focus better
     - Work gets finished faster
     - Less stress for team members

3. **Manage Flow**

   - Monitor and optimize work movement
   - Example: Tracking cycle time for bug fixes
     - Average time: 3 days
     - Identify bottlenecks in testing phase
     - Implement automated testing to improve flow
   - Why it helps:
     - Find and fix slow points
     - Make work move faster
     - Better team performance

4. **Make Process Policies Explicit**
   - Clear rules for work items
   - Example: Definition of "Done"
     - Code reviewed by two peers
     - Tests written and passing
     - Documentation updated
     - Deployed to staging environment
   - Why it helps:
     - Everyone knows what to do
     - Quality stays consistent
     - Less confusion in the team

## Key Roles

### 1. Service Delivery Manager

**Responsibilities**:

- Monitors workflow efficiency
- Resolves bottlenecks
- Facilitates process improvements

**Example Activities**:

- Daily flow analysis
- Resource allocation adjustments
- Performance metric tracking

**Why this role is important**:

- Keeps work moving smoothly
- Helps team work better
- Makes sure work gets done on time

### 2. Kanban Coach

**Responsibilities**:

- Guides team in Kanban practices
- Facilitates continuous improvement
- Helps optimize processes

**Example Activities**:

- Leading Kanban training sessions
- Conducting flow efficiency workshops
- Implementing metrics tracking systems

**Why this role is important**:

- Helps team learn Kanban
- Makes work better over time
- Supports team growth

### 3. Service Request Manager

**Responsibilities**:

- Manages incoming work requests
- Prioritizes tasks
- Balances team capacity

**Example Activities**:

- Evaluating new feature requests
- Managing stakeholder expectations
- Coordinating with Product Owner

**Why this role is important**:

- Makes sure team isn't overloaded
- Helps choose what to work on next
- Keeps work organized

## Kanban Board Example

### Web Application Development Project

| Backlog   | In Dev (WIP:3) | Review (WIP:2) | Test (WIP:2) | Done  |
| --------- | -------------- | -------------- | ------------ | ----- |
| Feature C | Feature A      | Bug Fix #123   | Feature B    | Login |
|           |                |                |              | Auth  |

## Metrics and Measurements

### 1. Lead Time

- Time from request to delivery
- Example: Feature request to production
  - Average: 15 days
  - Target: 12 days

### 2. Cycle Time

- Time from work start to completion
- Example: Development to deployment
  - Average: 5 days
  - Target: 3 days

### 3. Flow Efficiency

- Ratio of active work to wait time
- Example: Code review process
  - Current: 30% efficiency
  - Target: 60% efficiency

## Real-World Application Examples

### 1. Software Maintenance Team

**Scenario**: Managing bug fixes and feature requests

- Backlog: Prioritized list of issues
- WIP Limits: 3 active bugs, 2 features
- Metrics: 24-hour response time for critical bugs

### 2. Content Publishing Team

**Scenario**: Managing content creation workflow

- Stages: Draft → Review → Edit → Publish
- WIP Limits: 4 articles in progress
- Metrics: 48-hour turnaround for news articles

### 3. DevOps Team

**Scenario**: Managing deployment requests

- Workflow: Request → Plan → Deploy → Verify
- WIP Limits: 2 deployments in progress
- Metrics: 99.9% successful deployment rate

## Case Study: BBVA's Kanban Implementation

### Challenges in Non-IT Sectors

BBVA, a global financial services company, faced several challenges when implementing Kanban in non-IT areas:

1. **Cultural Resistance**

   - Traditional banking mindset vs. agile thinking
   - Solution: Gradual implementation with clear benefits
   - Example: Started with small teams to show success

2. **Process Adaptation**

   - Complex banking regulations and procedures
   - Solution: Customized Kanban for banking needs
   - Example: Added compliance check columns

3. **Skill Gaps**
   - Limited agile knowledge in non-IT teams
   - Solution: Extensive training and coaching
   - Example: Created internal Kanban coaches

### Impact of Kanban Maturity Model

The adoption of the Kanban Maturity Model (KMM) brought significant changes:

1. **Cultural Transformation**

   - More collaborative work environment
   - Better cross-department communication
   - Increased transparency in processes

2. **Service Delivery Improvements**

   - Faster response to customer needs
   - More predictable delivery times
   - Better quality control

3. **Organizational Benefits**
   - Improved employee satisfaction
   - Better resource utilization
   - Enhanced customer experience

### Key Success Factors

1. **Leadership Support**

   - Strong commitment from top management
   - Clear vision and goals
   - Regular progress reviews

2. **Customized Approach**

   - Adapted Kanban to banking needs
   - Maintained regulatory compliance
   - Balanced agility with stability

3. **Continuous Learning**
   - Regular training programs
   - Knowledge sharing sessions
   - Feedback loops for improvement

## Benefits of Kanban

1. **Flexibility**

   - No fixed iterations
   - Continuous flow of work
   - Adaptable to changing priorities
   - Why it's good:
     - Can change plans easily
     - Work never stops
     - Responds to new needs quickly

2. **Visibility**

   - Clear work status
   - Easy identification of bottlenecks
   - Transparent workload distribution
   - Why it's good:
     - Everyone knows what's happening
     - Problems are easy to see
     - Work is fair for everyone

3. **Efficiency**

   - Reduced waste
   - Optimized flow
   - Better resource utilization
   - Why it's good:
     - Less time wasted
     - More work gets done
     - Better use of team time

4. **Predictability**
   - Reliable delivery times
   - Consistent quality
   - Better planning capability
   - Why it's good:
     - Know when work will be done
     - Quality stays high
     - Can plan better

## Common Challenges and Solutions

1. **Too Many Tasks**

   - Problem: Board gets too full
   - Solution: Set lower WIP limits
   - Example: Reduce from 5 to 3 tasks per person

2. **Slow Movement**

   - Problem: Work gets stuck
   - Solution: Find and fix bottlenecks
   - Example: Add more testers if testing is slow

3. **Team Resistance**
   - Problem: Team doesn't want to change
   - Solution: Start small and show benefits
   - Example: Try with one small project first

## Conclusion

Kanban's visual nature and flexibility make it an effective methodology for managing work across various industries. Its focus on continuous flow, limited work in progress, and process improvement helps teams deliver value more efficiently while maintaining quality and adaptability to change.

**Remember**:

- Start simple
- Keep improving
- Focus on flow
- Make work visible
- Limit work in progress

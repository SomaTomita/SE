# Testing Strategies and Techniques

## Test Strategy Fundamentals

### What is a Testing Strategy?

A testing strategy is a high-level document that outlines how testing will be conducted across an organization or project. It includes:

- Types of testing to be performed (e.g., functional, non-functional)
- Choice between manual and automated testing
- Quality guidelines and objectives
- Example: Financial applications prioritize "security and regulatory compliance" in their strategy

### What are Testing Techniques?

Testing techniques are specific methods used to check different aspects of software:

- Verify functionality, performance, usability, and security
- Different approaches to testing implementation

Types include:

- Black-box testing (verifying external behavior without seeing code)
- White-box testing (analyzing internal logic with code access)
- Grey-box testing (combination of external and internal verification)

## Test Classifications and Levels

### Types of Testing

1. **Functional Testing**

   - Verifies software works according to specifications

2. **Non-functional Testing**

   - Performance
   - Security
   - UI/UX

3. **Structural Testing**

   - Based on internal logic and structure

4. **Change-related Testing**
   - Regression testing
   - Re-testing

### Testing Levels

| Level                    | Description                                                    |
| ------------------------ | -------------------------------------------------------------- |
| Unit Testing             | Testing individual functions/modules (e.g., JUnit, PyTest)     |
| Integration Testing      | Verifying module interactions and data flow between components |
| System Testing           | Testing complete application (functional + non-functional)     |
| Acceptance Testing (UAT) | User/client verification (including alpha/beta testing)        |

## Practical Testing Techniques

### 1. Boundary Value Analysis (BVA)

- Based on principle that bugs often occur at boundaries
- Based on principle that bugs often occur at boundaries
- Example 1: For input range 1-100, test 0,1,100,101
- Example 2: For a password length requirement of 8-16 characters, test:
  - 7 characters (just below minimum)
  - 8 characters (minimum boundary)
  - 16 characters (maximum boundary)
  - 17 characters (just above maximum)
- Efficiently detects edge cases with minimal test cases

### 2. Equivalence Partitioning

- Groups input values into clusters with expected similar behavior
- Tests representative values from valid clusters (e.g., 1-100)
- Tests invalid clusters (e.g., -1, 0, 101)
- Reduces test cases while maintaining coverage

### 3. Exploratory Testing

- Flexible testing without strict scripts
- Simultaneous learning and testing
- Effective for UI and complex user interactions
- Leverages creativity to find unexpected bugs

## Use Case-Based Testing

### What is a Use Case?

- User operation scenarios for software
- Typically includes:
  - Actor (who)
  - Scenario (steps)
  - Expected results

Example:

- E-commerce flow: "Add to cart → Complete purchase"

### UML Relationship

- UML use case diagrams visualize user-function relationships
- Testing techniques closely relate to use cases
- Creates realistic test scenarios

Example Application:

- Banking app "account transfer" use case
  - Functional test: Can transfers complete successfully?
  - Security test: Can third parties intercept data?

## Automated vs Manual Testing

| Method            | Characteristics                                                              |
| ----------------- | ---------------------------------------------------------------------------- |
| Manual Testing    | Human verification, strong in usability and exploratory testing              |
| Automated Testing | Script-based execution, suitable for regression testing and repetitive tasks |

## Comprehensive Key Takeaways

### 1. Testing Strategy Provides a Consistent Organisational Framework

- Outlines overarching approach to testing across projects
- Includes test types, objectives, and risk assessments
- Defines entry/exit criteria and automation decisions
- Adapts to project size, complexity, and regulations
- Ensures alignment with business goals and compliance requirements

### 2. Testing Techniques Ensure Comprehensive Quality Assessment

- Structured methods for evaluating all aspects of software
- Selection based on development stage and testing level
- Combines multiple approaches:
  - Boundary Value Analysis for edge cases
  - Equivalence Partitioning for efficient coverage
  - Use case-based testing for real-world scenarios
- Critical for meeting user and technical requirements

### 3. Test Automation Enhances Efficiency and Accuracy

- Leverages tools like Selenium, Cypress, JUnit, PyUnit
- Improves efficiency in:
  - Test execution
  - Defect detection
  - Results reporting
- Particularly valuable for:
  - Large-scale applications
  - Continuous integration environments
  - Regression testing
  - Repetitive tasks

### 4. Best Practices in Automation Improve Test Reliability

- Focus on high-impact, repetitive tasks
- Integration with CI/CD pipelines
- Balanced combination with manual testing
- Emphasis on:
  - Maintainable test scripts
  - Edge case coverage
  - Clear documentation
  - Version control

### 5. Modern Testing Trends are Shaping Industry Practice

- Shift-Left Testing for early defect detection
- AI-driven testing for improved accuracy
- Codeless automation tools for accessibility
- DevSecOps integration
- Performance engineering focus
- Microservices testing strategies

### 6. The Future of Testing Emphasises Security, Performance, and Intelligence

- Growing importance of:
  - Security testing in DevSecOps
  - Performance engineering
  - AI-enhanced testing
- Adaptation to:
  - Cloud environments
  - Microservices architecture
  - IoT applications
- Integration with:
  - Agile methodologies
  - DevOps practices
  - Continuous delivery pipelines

### 7. Practical Implementation Considerations

- Test component interactions effectively
- Verify system communication paths
- Ensure data flow integrity
- Optimize test design for:
  - Efficiency
  - Coverage
  - Maintainability
- Balance automated and manual testing approaches

### 8. Strategic Success Factors

- Align testing with business objectives
- Prioritize based on risk assessment
- Consider regulatory requirements
- Maintain continuous improvement cycle
- Foster collaboration between development and testing teams
- Implement metrics-driven quality assessment

# Practical Example: Unit Testing with Python

### Class Diagram

<pre>
+------------------------+
| User |
+------------------------+
| - username: str |
| - email: str |
+------------------------+
| + is_email_valid(): bool |
| + send_welcome_email(): None |
+------------------------+
</pre>

### Implementation Code

```python
# user.py
import re

class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def is_email_valid(self) -> bool:
        # Simple email format check
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", self.email))

    def send_welcome_email(self) -> None:
        print(f"Welcome, {self.username}! Email sent to {self.email}")
```

### Test Code with PyTest

```python
# test_user.py
import pytest
from user import User

def test_is_email_valid():
    user = User(username="alice", email="alice@example.com")
    assert user.is_email_valid() is True

def test_is_email_invalid():
    user = User(username="bob", email="bob#example.com")
    assert user.is_email_valid() is False

def test_send_welcome_email(capsys):
    user = User(username="carol", email="carol@example.com")
    user.send_welcome_email()
    captured = capsys.readouterr()
    assert "Welcome, carol!" in captured.out
```

### Test Cases Explanation

1. **Valid Email Test**

   - Tests that a correctly formatted email is validated
   - Uses boundary value analysis for a valid input

2. **Invalid Email Test**

   - Tests that an incorrectly formatted email is rejected
   - Example of negative testing

3. **Welcome Email Test**
   - Tests the output functionality
   - Uses PyTest's capsys fixture to capture stdout
   - Example of behavior verification

## Practice Questions and Answers

### Question 1: Online Banking Security Testing

**Question:**
A financial company is developing an online banking system. To comply with industry regulations, they prioritise security testing to prevent fraud and data breaches. Which aspect of software testing does this scenario best illustrate?

**Options:**

- Testing Strategy
- Exploratory Testing
- Integration Testing
- System Testing

**Answer: Testing Strategy**

**Explanation:**
This scenario best illustrates a Testing Strategy because:

- It involves a planned approach to testing that aligns with business objectives (regulatory compliance)
- Prioritizes specific testing types (security) based on risk assessment
- Focuses on critical aspects of the system (fraud prevention and data security)
- Demonstrates strategic decision-making in test planning

### Question 2: Inventory Management System Testing

**Question:**
A development team is testing a newly built web-based inventory management system. They decide to evaluate how different modules, such as product tracking and order processing, communicate with each other. Which type of testing is most relevant in this scenario?

**Options:**

- Unit Testing
- Boundary Value Analysis
- Integration Testing
- User Acceptance Testing

**Answer: Integration Testing**

**Explanation:**
Integration Testing is most appropriate because:

- Tests interactions between different modules
- Verifies communication between system components
- Ensures data flow between product tracking and order processing
- Focuses on interface testing between integrated components

### Question 3: Login System Testing

**Question:**
A software tester is evaluating a new login system. They enter different combinations of usernames and passwords but do not examine the underlying code. What type of testing technique are they using?

**Options:**

- White-Box Testing
- Regression Testing
- Performance Testing
- Black-Box Testing

**Answer: Black-Box Testing**

**Explanation:**
This is Black-Box Testing because:

- Tester focuses on inputs and outputs without knowledge of internal code
- Testing is based on external behavior of the system

### Question 4: E-commerce Age Validation Testing

**Question:**
A company is developing an e-commerce platform. The testers decide to classify age-related data into three categories: under 18 (invalid), between 18 and 65 (valid), and over 65 (invalid). They then test only one value from each category instead of every possible age. Which testing technique is being used?

**Options:**

- Boundary Value Analysis
- Unit Testing
- Equivalence Partitioning
- Exploratory Testing

**Answer: Equivalence Partitioning**

**Explanation:**
This is Equivalence Partitioning because:

- Data is divided into distinct categories (partitions)
- Each partition represents a class of equivalent inputs
- Testing one value from each partition is considered sufficient
- Reduces number of test cases while maintaining effectiveness

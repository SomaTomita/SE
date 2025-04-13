# Configuration Management Quiz Explanations

## Question 1: Definition of Configuration Management

**Question:** Which of the following best defines Configuration Management in Software Engineering?

**Options:**

- A. A systematic approach to managing changes in software artefacts
- B. A process to ensure software is always updated with the latest features
- C. A technique used to design user interfaces
- D. A method to increase software execution speed

**Correct Answer:** A. A systematic approach to managing changes in software artefacts

### Explanation

Configuration Management (CM) is fundamentally about managing and controlling changes in software artifacts throughout the development lifecycle. Let's analyze each option:

✅ **A systematic approach to managing changes in software artefacts**

- This is correct because CM:
  ```
  Example: E-commerce System Version Control
  v1.0.0 - Initial release
  │
  ├── source code changes tracked
  ├── documentation updates logged
  ├── dependency changes recorded
  └── configuration files versioned
  ```

## Question 2: Key Activities of Configuration Management

**Question:** Which of the following is NOT a key activity of Configuration Management?

**Options:**

- A. Risk Analysis
- B. Build and Release Management
- C. Change Management
- D. Version Control

**Correct Answer:** A. Risk Analysis

### Explanation

Let's examine each activity:

✅ **Risk Analysis**

- This is correctly identified as NOT being a core CM activity
- While important for project management, it's not a primary CM function
- Example of actual risk analysis:
  ```
  Project Risk Assessment
  - Security vulnerabilities
  - System downtime
  - Data loss
  ```
  This belongs to Project Management, not CM.

## Question 3: Importance of Version Control

**Question:** Why is version control important in Configuration Management?

**Options:**

- A. It allows tracking of changes and collaboration among developers
- B. It prevents software from being modified
- C. It ensures software runs faster
- D. It eliminates the need for documentation

**Correct Answer:** A. It allows tracking of changes and collaboration among developers

### Explanation

Let's analyze each option with examples:

1. ✅ **It allows tracking of changes and collaboration among developers**

   - Correct because it enables:
     ```
     Team Collaboration Example:
     Developer A: Working on login feature
     │
     ├── Developer B: Working on payment system
     │   └── Merges changes without conflicts
     │
     └── Developer C: Fixing bugs
         └── Can see who made what changes
     ```

## Question 4: Purpose of Baselines

**Question:** What is the purpose of baselines in Configuration Management?

**Options:**

- A. To manage user interface elements
- B. To act as a reference point for software versions at a given time
- C. To permanently lock software artefacts from any further modification
- D. To increase system performance

**Correct Answer:** B. To act as a reference point for software versions at a given time

### Explanation

Let's examine each option:

✅ **To act as a reference point for software versions at a given time**

- Correct because baselines:
  ```
  Release Baseline Example:
  v1.0.0-BASELINE
  ├── Code freeze: 2024-01-15
  ├── Tested: All tests passing
  ├── Approved: Product owner sign-off
  └── Dependencies: Locked versions
  ```

## Key Takeaways

1. Configuration Management is about systematic change control
2. Core CM activities include version control, change management, and build/release management
3. Version control facilitates collaboration and change tracking
4. Baselines provide stable reference points for development

# Question : Canvas LMS Testing Strategy Analysis

## Scenario

Canvas is enhancing its learning management system (LMS) to introduce a real-time collaboration feature for group projects and live discussions. The development team must ensure that the system delivers a reliable user experience across multiple browsers and devices under heavy load. Given the need for both functional accuracy and responsive usability, the team must decide how much to rely on automated testing versus manual exploratory testing.

## Task

Critically evaluate the use of automated testing compared to manual testing in the context of Canvas's real-time collaboration feature development.

## Assessment Criteria

- Two advantages of automated testing for Canvas's collaboration feature, critically explained (4 marks, 2 marks each)
- Two limitations of automated testing in this context, critically explained (4 marks, 2 marks each)
- One scenario where automated testing is effective and clearly justified (2 marks)
- One scenario where manual testing is necessary and clearly justified (2 marks)

## Answer

In developing Canvas’s real-time collaboration feature, testing strategies must be evaluated by how effectively they reveal risks that could disrupt learning continuity. Automated testing offers clear advantages in this context. For one, it enables scalable load testing through continuous integration, where thousands of virtual users can be simulated via WebSocket clients performing simultaneous edits. This approach helps detect latency spikes above a 300 ms threshold—something impossible to identify manually with consistency—providing immediate feedback after each code change. Additionally, automated testing serves as a reliable safety net for cross-platform regression. Using headless browser automation, developers can routinely verify compatibility across twenty browser and device combinations, identifying visual or structural inconsistencies that might otherwise go unnoticed. This prevents user-facing defects like browser-specific UI failures, which could undermine trust among instructors during critical usage periods such as grading.

However, automated testing also faces limitations. It tends to miss unpredictable, human-driven edge cases in concurrent interactions. Scripts follow deterministic paths, meaning race conditions caused by users’ varied pacing—such as two students editing the same slide simultaneously—may never be triggered, resulting in false confidence. Moreover, maintaining automated tests in a fast-evolving UI poses logistical challenges. Real-time components often change weekly, and test scripts become brittle, leading to frequent breakages and slowing the development cycle—thus undercutting the efficiencies that automation seeks to provide.

Automation is most effective for verifying system resilience under concurrent usage, such as ensuring all clients receive synchronized updates with less than 500 ms latency and minimal data loss. Conversely, manual testing becomes indispensable when evaluating user experience aspects like conflict resolution flows during rubric editing under real-world network conditions. Ultimately, a hybrid strategy—automated testing for performance and regression, manual testing for UX evaluation—will best align with Canvas’s goals of reliability and pedagogical usability.

(299 words)

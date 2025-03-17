# The Software Development Lifecycle (SDLC)

The Software Development Lifecycle (SDLC) is a process that helps teams create high-quality software. Each phase of the SDLC produces important outputs called deliverables. These deliverables help teams move from one stage to the next in an organized way.

## Key Deliverables in the SDLC

### Requirement Documents

These documents explain what the software needs to do. They include:

- User stories (what users want to do with the software)
- Use cases (how users will interact with the software)
- Functional specifications (detailed descriptions of features)

Requirement documents help everyone understand what the software should do before building starts.

### Design Documents

Design documents show how the software will be built. They include:

- System architecture diagrams
- Component specifications
- Models showing how different parts work together

These documents serve as a blueprint for developers to follow when building the software.

### Source Code and Executables

These are the actual software products created during development:

- Source code: The written instructions in programming languages
- Executables: The runnable programs that users can use

This is what developers create based on the requirements and design.

### Test Reports

Test reports show if the software works correctly. They include:

- Test cases (planned tests)
- Bug reports (problems found)
- Fix confirmations (solutions applied)

These reports help ensure the software works as expected before release.

### Deployment Plans

Deployment plans explain how to release the software. They include:

- Steps to move from development to production
- Timelines for release
- Backup plans if problems occur

Good deployment plans help make software releases smooth and problem-free.

### Maintenance Reports

Maintenance reports track changes made after release. They include:

- Bug fixes
- Security updates
- New features added

These reports help teams keep track of how the software changes over time.

## Summary

The SDLC deliverables provide a clear path for software development. They help teams communicate better and stay organized. By creating good requirement documents, design documents, source code, test reports, deployment plans, and maintenance reports, teams can build better software that meets user needs.

# Quiz Answers

### Question 1: A software development team is building a mobile banking application. During which phase of the SDLC should they define security requirements and identify potential risks associated with online transactions?

**Correct Answer: Requirements Analysis**

Explanation of choices:

- **Planning**: Incorrect. While the Planning phase involves high-level project scoping, detailed security requirements are typically defined during Requirements Analysis.
- **Requirements Analysis**: Correct. This is the phase where all functional and non-functional requirements, including security requirements, are identified and documented. Security considerations for a banking application are critical requirements that must be clearly defined before design begins.
- **Design**: Incorrect. The Design phase implements security measures based on requirements already defined. While security architecture is created during Design, the actual requirements should be established earlier.
- **Implementation**: Incorrect. By the Implementation phase, security requirements should already be defined. This phase involves coding the security features according to the requirements and design.

### Question 2: A retail company is upgrading its inventory management system. They have finalised the design, and developers have started coding. However, a major change in regulatory compliance requirements has just been announced. What should they do next?

**Correct Answer: Pause development and return to the Requirements Analysis phase**

Explanation of choices:

- **Implement partial changes now and address the rest after deployment**: Incorrect. This approach risks creating an incomplete solution that may not fully comply with regulations, potentially leading to legal issues.
- **Continue coding as planned and address compliance in a later update**: Incorrect. Regulatory compliance is typically mandatory, and delaying implementation could result in a non-compliant system being deployed.
- **Pause development and return to the Requirements Analysis phase**: Correct. Major regulatory changes affect requirements and potentially the system design. The team should pause development, analyze the new requirements, update documentation, and adjust the design before continuing implementation.
- **Proceed with coding and adjust the design in the next SDLC cycle**: Incorrect. This would result in releasing non-compliant software, which could have legal and business consequences.

### Question 3: A retail company has just deployed a new warehouse management system. After a week, employees report that stock updates are not synchronising correctly, causing inaccurate inventory counts. Which SDLC phase should now be revisited?

**Correct Answer: Maintenance**

Explanation of choices:

- **Deployment**: Incorrect. The Deployment phase involves releasing the software to production. Since the system is already deployed and running, this phase is complete.
- **Maintenance**: Correct. The Maintenance phase deals with issues that arise after deployment. Bug fixes, performance improvements, and minor adjustments are handled during this phase. The synchronization issue is a post-deployment problem that requires maintenance.
- **Requirements Analysis**: Incorrect. Returning to Requirements Analysis would be necessary only if the issue revealed a fundamental misunderstanding of business needs, requiring a major redesign.
- **Design**: Incorrect. While the synchronization issue might involve design flaws, addressing it post-deployment falls under Maintenance unless a complete redesign is needed.

### Question 4: An education technology company is developing an online learning platform. Midway through the Implementation phase, the client requests several major changes to the way quizzes and assessments work. What are the possible consequences?

**Correct Answer: Increased development time AND Higher project costs**

Explanation of choices:

- **Increased development time**: Correct. Major changes during Implementation will require additional development time to implement the new requirements and potentially redo work that's already been completed.
- **Higher project costs**: Correct. Changes during Implementation are more expensive to address than changes identified earlier in the SDLC. Additional development time, rework, and potentially new design work will increase costs.
- **Reduced need for testing**: Incorrect. Changes to functionality will actually increase the need for testing to ensure the new features work correctly and don't introduce bugs.
- **Improved user experience**: Not necessarily correct. While the changes might eventually improve user experience if they're well-designed, making major changes midway through implementation often leads to integration issues and inconsistencies that can negatively impact user experience.

Note: This question appears to have multiple correct answers (both increased development time and higher project costs are valid consequences).

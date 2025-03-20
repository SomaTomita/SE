# EduAdvance Platform Requirements Analysis Exercise

## Original Task Description

### Scenario

You have been tasked with designing an online platform called EduAdvance, which supports students enrolled in a Software Engineering module. This platform will be a comprehensive learning hub, offering the following features:

- Access to Resources: Students can watch video lectures, engage with interactive exercises, and attempt quizzes.
- Assignment Management: Students can submit assignments and track their progress.
- Live Q&A Sessions: Students can participate in real-time discussions with instructors to clarify doubts.
- Discussion Forums: Peer-to-peer interaction is facilitated through vibrant discussion boards.
- Personalised Feedback: The platform provides tailored feedback and recommendations for further learning.
- Scheduling Feature: Students can book consultation slots with instructors, with slots visible and updatable by both parties.
- Third-Party Integration: Integration with tools like plagiarism checkers for assignment submission analysis.
- Polls Feature: Instructors can create and distribute polls during live Q&A sessions, with real-time voting and analytics.
- Offline Access: Support for offline access to video lectures and interactive materials, syncing progress once reconnected to the internet.

### Critical Requirements from Stakeholders

- Mobile-Friendly: The platform must support learning on the go.
- Data Security: Strong measures to protect sensitive information.
- Scalability: The platform must handle up to 10,000 simultaneous users during peak times.

### User Stories

- As a student, I want to watch video lectures on any device so that I can study on the go.
- As a student, I want to track my progress on quizzes and assignments so that I know how well I am doing in the course.
- As an instructor, I want to provide real-time feedback on assignments so that students can improve quickly.
- As a student, I want to join live Q&A sessions so that I can clarify doubts directly with the instructor.
- As an admin, I want to ensure the platform scales during peak hours so that no users experience delays.
- As a student, I want to book consultation slots with my instructor to discuss specific topics.
- As an instructor, I want to create polls during live Q&A sessions to gauge student understanding in real time.

### Task

Step 1:

- Identify at least 5 functional requirements for the EduAdvance platform.
- Identify at least 3 non-functional requirements for the EduAdvance platform.
- Ensure your requirements are clear, concise, and accurately categorised as functional or non-functional.
- Post your responses onto Padlet using the relevant link in the box below.

Step 2:

- Review the comments on the Padlet. Respond to at least 2 classmates. This could be to add something to their explanation or, if you disagree with their answer, to constructively counter their argument with alternative points of view.

## Model Answer and Solution

### Step 1: Identify Requirements

#### Functional Requirements (5+)

1. **Video Lecture Access**

   - System must allow students to stream video lectures
   - System must support pause/resume functionality
   - System must track viewing progress

2. **Assignment Management**

   - System must allow file uploads for assignment submission
   - System must integrate with plagiarism checking tools
   - System must maintain submission timestamps

3. **Interactive Sessions**

   - System must support real-time video Q&A sessions
   - System must enable live chat during sessions
   - System must allow creation and response to polls

4. **Scheduling System**

   - System must display available consultation slots
   - System must allow booking/cancellation of slots
   - System must send notifications for bookings

5. **Offline Functionality**
   - System must allow downloading of learning materials
   - System must track progress during offline usage
   - System must sync data when reconnected

#### Non-Functional Requirements (3+)

1. **Performance & Scalability**

   - Response Time Requirements:

     - Web page load time must be under 3 seconds (industry standard for educational platforms)
     - API responses must be under 1 second for critical operations
     - Video streaming must start within 2 seconds of request
     - Rationale:
       - Research shows 40% of users abandon websites that take more than 3 seconds to load
       - Educational platforms need quick response times to maintain student engagement
       - Google's PageSpeed Insights recommends under 3 seconds for optimal user experience

   - System Load Requirements:

     - Must support 10,000 concurrent users during peak times (based on stakeholder requirements)
     - Must handle at least:
       - 1,000 simultaneous video streams
       - 5,000 simultaneous quiz submissions
       - 2,000 simultaneous assignment uploads
     - Rationale: Based on expected usage patterns during exam periods and assignment deadlines

   - Scalability Metrics:

     - System must automatically scale to handle 25% increase in load
     - Database queries must complete within 500ms under peak load
     - File uploads must maintain minimum 10MB/s speed under peak load
     - Rationale: Based on typical educational institution growth patterns and usage spikes

   - Resource Utilization:
     - CPU usage should not exceed 70% under normal load
     - Memory usage should not exceed 80% of available RAM
     - Storage should have minimum 25% free space
     - Rationale: Industry best practices for maintaining system stability and performance

1. **Security & Privacy**

   - System must encrypt all sensitive data:

     - Student personal information (names, IDs, contact details) using AES-256 encryption
     - Assignment submissions and grades using AES-256 encryption
     - Authentication credentials (passwords must be hashed using bcrypt)
     - Session data and cookies must be encrypted
     - All data in transit must use TLS 1.3 encryption

   - System must implement secure authentication:

     - Multi-factor authentication for administrative access
     - Password requirements: minimum 12 characters, including uppercase, lowercase, numbers, and special characters
     - Account lockout after 5 failed login attempts
     - Session timeout after 30 minutes of inactivity
     - Secure password reset process with email verification

   - System must comply with data protection regulations:

     - GDPR compliance for EU students
     - FERPA compliance for educational records
     - Regular security audits and vulnerability assessments
     - Data retention policies must be implemented
     - Clear data privacy policies must be accessible to users

   - System must maintain audit logs:

     - All access attempts (successful and failed)
     - Changes to user permissions
     - File uploads and downloads
     - Changes to grades or assessment results
     - System configuration changes

   - System must implement access control:
     - Role-based access control (RBAC) for students, instructors, and administrators
     - IP-based access restrictions for administrative functions
     - Granular permissions for different types of content
     - Secure file upload validation and scanning

1. **Usability & Accessibility**
   - System must be mobile-responsive
   - System must be accessible on major browsers
   - System must meet WCAG 2.1 accessibility standards

## Model Answer and Explanation

### Functional Requirements Analysis

Good functional requirements should be:

- Specific and measurable
- Action-oriented
- Focused on what the system must do

Example explanation for "Video Lecture Access":
This is a functional requirement because it describes specific actions the system must perform (streaming, pausing, tracking). It directly relates to system behavior and can be tested for completion.

### Non-Functional Requirements Analysis

Good non-functional requirements should be:

- Quantifiable where possible
- Quality-focused
- System-wide in scope

Example explanation for "Performance & Scalability":
This is a non-functional requirement because it describes how well the system performs its functions rather than what it does. The specific number (10,000 users) makes it measurable and testable.

### Common Mistakes to Avoid

1. **Mixing Categories**

   - Incorrect: "System must be secure" (too vague)
   - Correct: "System must encrypt all data using AES-256 encryption"

2. **Unclear Requirements**

   - Incorrect: "System should be fast"
   - Correct: "System must respond to user requests within 2 seconds"

3. **Unmeasurable Requirements**
   - Incorrect: "System should be user-friendly"
   - Correct: "System must achieve a System Usability Scale (SUS) score of 80 or higher"

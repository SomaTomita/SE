# ExcelAcademy Registration Platform Case Study

## Problem Statement

Excel, an emerging academy, is developing a new online registration platform to better serve students, instructors, and IT administrators. The platform will:

- Store students' personal details
- Track module attendance
- Manage registration data securely

All users must authenticate before accessing the platform. Students register for modules, instructors update attendance records, and IT administrators manage database integrity.

### Task

Create a simplified UML use case diagram for ExcelAcademy's platform that demonstrates:

1. The three main actors (Student, Instructor, IT Administrator) each connected to one specific role-based functionality (e.g., register module, update attendance, manage database).

2. Modelling of multiple authentication flows by showing:

   - A shared Authenticate use case for all users
   - An optional Setup Two-Factor Authentication use case, modelled with either an include or extend relationship, based on your interpretation of the scenario

3. Justify your choice of using include or extend to model the Two-Factor Authentication step.

4. Provide a brief example from the scenario explaining when Two-Factor Authentication would be triggered or required.

Note: To gain marks, your diagram must use appropriate UML shapes and notation.

### Marking Criteria (14 marks total)

- 6 marks: 1 mark for each correctly identified actor and 1 mark for each correctly connected role-specific use case
- 2 marks: Correct use of inheritance (Student, Instructor, Admin inherit from User)
- 2 marks: Accurate modelling of Log In and Create Password relationship
- 3 marks: Justification of extended relationship, based on understanding of their usage for optionality
- 1 mark: Use of a relevant example from the scenario to support modelling choice

# Answer

@/academy_registration_platform/use_case_diagram_auth.png

```mermaid
%{init: {'theme': 'base'}}%%
usecaseDiagram
left to right direction

actor User
actor Student
actor Instructor
actor "IT Administrator" as Admin

rectangle "ExcelAcademy Registration System" {
  usecase "Authenticate" as UC_Auth
  usecase "Create Password" as UC_Pwd
  usecase "Setup Two-Factor Authentication" as UC_2FA
  usecase "Register Module" as UC_Register
  usecase "Update Attendance" as UC_Attend
  usecase "Manage Database" as UC_DB
}

User <|-- Student
User <|-- Instructor
User <|-- Admin

User <|-- Student
User <|-- Instructor
User <|-- Admin

User -- "1..1" UC_Auth
UC_Auth ..> "1..1" UC_Pwd : <<include>>
UC_Auth ..> "0..1" UC_2FA : <<extend>>

Student -- "0..*" UC_Register
Instructor -- "1..*" UC_Attend
Admin -- "1..1" UC_DB
```

## Justification Answer (150 words)

ExcelAcademy’s registration platform defines three specialized roles under a shared User actor, secured by a mandatory Authenticate use case (1..1).

Upon successful authentication, each actor invokes one primary operation: Students Register Module (0..\*), Instructors Update Attendance (1..\*), and IT Administrators Manage Database (1..1), ensuring clear separation of concerns and traceability.

The Create Password use case is factored into Authenticate via an «include» relationship (1..1), since every user must set or confirm credentials before proceeding. Two-Factor Authentication (2FA) is represented using an «extend» relationship (0..1) from Authenticate, reflecting its optional nature under risk conditions. For instance, 2FA triggers when a student logs in for the first time, an instructor accesses from an unfamiliar IP, or an administrator signs in on a new device.

This modelling accurately captures both mandatory and conditional security flows and satisfies the marking criteria for inheritance, multiplicity, and relationship stereotyping. It balances usability with robust protection.

(149 words)

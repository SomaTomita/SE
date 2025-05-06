## Question : (maximum of 150 words)

Canvas is developing a platform to support student group projects. The platform must allow:

- Students to form project groups,
- Groups to create and assign tasks to members,
- Supervisors to monitor project group activities.

Each group can have multiple students, but only one supervisoris is assigned.
Each task belongs to exactly one group and must be assigned to one or more students.

### Task

Create a simplified UML class diagram for the platform that includes the four core classes.
In your diagram:

- Show appropriate relationships between the classes (e.g., associations, compositions, multiplicities).
- Use correct UML notation (class shapes, relationships, cardinalities).
- Annotate the diagram with any key constraints, such as "One Supervisor oversees many Groups" or "Tasks must be assigned to at least one Student."

Finally, write a brief critical reflection (maximum 100 words) explaining how your design supports scalability and maintainability of the system over time.

_Note: Accuracy of UML shapes, relationship types, and clarity of annotations will be marked._

### Answer/Marking Criteria

- Accurate inclusion and definition of the four core classes (Student, Group, Task, Supervisor), 2 marks
- Correct and logical relationships between classes (association, composition, generalisation), 3 marks
- Accurate and clear UML notation (correct shapes, arrows, multiplicities where relevant), 2 marks
- Clear annotations explaining constraints on relationships (e.g., cardinalities, mandatory associations), 1 mark
- Critical reflection explaining how the design supports scalability and maintainability, 2 marks

## Answer

```mermaid
class Student
class Group
class Task
class Supervisor

Student "*" -- "1..*" Group : belongs to
Supervisor "1" -- "*" Group : oversees
Group "1" o-- "*" Task : owns
Student "1..*" -- "*" Task : assigned to

note right of Group
Each Group has exactly 1 Supervisor
and at least 1 Student.
end note

note bottom of Task
Task must belong to 1 Group
and be assigned to ≥1 Student.
end note
```

### Critical Reflection

The design supports scalability and maintainability through clear separation of concerns and flexible relationships. For scalability, the many-to-many relationship between Students and Tasks allows for dynamic task allocation as teams grow. The composition between Group and Task ensures proper encapsulation, making it easier to maintain and modify task management features independently. The design can be extended to support new features without breaking existing functionality - for example, adding different task types such as coding, documentation or implementing group categories such as research, development would require minimal changes to the core structure.

(90 words)

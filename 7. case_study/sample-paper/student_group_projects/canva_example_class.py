from typing import List, Set
from datetime import datetime
from uuid import uuid4


class Supervisor:
    def __init__(self, name: str, email: str):
        self.id = str(uuid4())
        self.name = name
        self.email = email
        self.groups: List[Group] = []

    def monitor_group(self, group):
        """Monitor activities of a specific group"""
        if group in self.groups:
            print(f"Monitoring group: {group.name}")
            return True
        return False

    def review_progress(self, group):
        """Review progress of a specific group"""
        if group in self.groups:
            task_count = len(group.tasks)
            completed_tasks = sum(
                1 for task in group.tasks if task.status == "Completed"
            )
            completion_rate = completed_tasks / task_count if task_count > 0 else 0
            print(
                f"Group {group.name} progress: {completion_rate:.0%} ({completed_tasks}/{task_count} tasks completed)"
            )
            return completion_rate
        return None

    def __repr__(self):
        return f"Supervisor(id={self.id}, name={self.name}, email={self.email})"


class Student:
    def __init__(self, name: str, email: str):
        self.id = str(uuid4())
        self.name = name
        self.email = email
        self.groups: List[Group] = []
        self.assigned_tasks: List[Task] = []

    def join_group(self, group):
        """Join a project group"""
        if group not in self.groups:
            self.groups.append(group)
            group.add_student(self)
            return True
        return False

    def complete_task(self, task):
        """Mark a task as completed"""
        if task in self.assigned_tasks:
            task.update_status("Completed")
            return True
        return False

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, email={self.email})"


class Group:
    def __init__(self, name: str, description: str, supervisor: Supervisor):
        self.id = str(uuid4())
        self.name = name
        self.description = description
        self.creation_date = datetime.now()
        self.supervisor = supervisor
        self.students: List[Student] = []
        self.tasks: List[Task] = []

        # Add this group to supervisor's groups
        supervisor.groups.append(self)

    def add_student(self, student: Student):
        """Add a student to the group"""
        if student not in self.students:
            self.students.append(student)
            if self not in student.groups:
                student.groups.append(self)
            return True
        return False

    def create_task(self, title: str, description: str, deadline=None):
        """Create a new task for this group"""
        task = Task(title, description, self, deadline)
        self.tasks.append(task)
        return task

    def assign_task(self, task, students: List[Student]):
        """Assign a task to student(s)"""
        if task in self.tasks and all(student in self.students for student in students):
            for student in students:
                task.assign_to_student(student)
            return True
        return False

    def __repr__(self):
        return f"Group(id={self.id}, name={self.name}, students={len(self.students)})"


class Task:
    def __init__(self, title: str, description: str, group: Group, deadline=None):
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.group = group
        self.deadline = deadline
        self.creation_date = datetime.now()
        self.status = "Pending"  # Pending, In Progress, Completed
        self.assigned_students: List[Student] = []

    def assign_to_student(self, student: Student):
        """Assign the task to a student"""
        if student in self.group.students and student not in self.assigned_students:
            self.assigned_students.append(student)
            if self not in student.assigned_tasks:
                student.assigned_tasks.append(self)
            self.status = "In Progress"
            return True
        return False

    def update_status(self, status: str):
        """Update the status of the task"""
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if status in valid_statuses:
            self.status = status
            return True
        return False

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"


# Example usage:
if __name__ == "__main__":
    # Create supervisor
    supervisor = Supervisor("Dr. Smith", "smith@university.edu")

    # Create group
    project_group = Group("Team Alpha", "Software Engineering Project", supervisor)

    # Create students
    alice = Student("Alice Johnson", "alice@university.edu")
    bob = Student("Bob Wilson", "bob@university.edu")
    charlie = Student("Charlie Brown", "charlie@university.edu")

    # Add students to group
    project_group.add_student(alice)
    project_group.add_student(bob)
    project_group.add_student(charlie)

    # Create tasks
    task1 = project_group.create_task(
        "Design UML Diagram", "Create class diagram for the system"
    )
    task2 = project_group.create_task(
        "Implement User Authentication", "Create login and registration system"
    )
    task3 = project_group.create_task(
        "Create Database Schema", "Design and implement database schema"
    )

    # Assign tasks
    project_group.assign_task(task1, [alice, bob])
    project_group.assign_task(task2, [bob, charlie])
    project_group.assign_task(task3, [alice, charlie])

    # Complete a task
    alice.complete_task(task1)

    # Supervisor monitors progress
    supervisor.review_progress(project_group)

    # Print information
    print(f"\nGroup: {project_group.name}")
    print(f"Supervisor: {project_group.supervisor.name}")
    print(f"Students: {', '.join(student.name for student in project_group.students)}")
    print("\nTasks:")
    for task in project_group.tasks:
        assigned_names = ", ".join(student.name for student in task.assigned_students)
        print(f"- {task.title} ({task.status}): assigned to {assigned_names}")

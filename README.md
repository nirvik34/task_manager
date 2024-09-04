# Task Management System

### This is a simple Python-based Task Management System that uses SQLite for storing and managing tasks. The system allows you to add, update, delete, list, and mark tasks as completed.

### Features
- **Add Tasks:** Create new tasks with a title, description, and due date
- __List Tasks:__ View all pending tasks or include completed tasks.
- __Update Tasks:__ Modify existing task details such as title, description, or due date.
- __Delete Tasks:__ Remove tasks from the database.
- __Mark Tasks as Completed:__ Mark tasks as completed to track progress.

### Requirements
- Python 3.x
- SQLite3 (built into Python)

### Usage

#### Upon running the script, you will be presented with a menu of options:
- Add Task: Choose option 1 to add a new task. You will be prompted to enter the task title, description, and due date.
- List Tasks: Choose option 2 to list all tasks. You can choose whether to include completed tasks in the listing.
- Update Task: Choose option 3 to update an existing task. You will need to enter the task ID and the new details.
- Delete Task: Choose option 4 to delete a task by its ID.
- Mark Task Completed: Choose option 5 to mark a task as completed.
- Exit: Choose option 6 to exit the program.

  ### Database Schema
#### The system uses a single SQLite table named tasks:

- id (INTEGER): Unique identifier for each task (Primary Key).
- title (TEXT): Title of the task.
- description (TEXT): Description of the task.
- due_date (TEXT): Due date of the task in YYYY-MM-DD format.
- completed (BOOLEAN): Status of the task (0 = Pending, 1 = Completed).

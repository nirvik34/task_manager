import sqlite3
from datetime import datetime

# Database connection
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create tasks table
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    due_date TEXT,
                    completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
                )''')

def add_task(title, description, due_date):
    """Add a new task to the database."""
    cursor.execute("INSERT INTO tasks (title, description, due_date, completed) VALUES (?, ?, ?, ?)",
                   (title, description, due_date, 0))
    conn.commit()
    print("Task added successfully.")

def list_tasks(show_completed=False):
    """List all tasks, optionally including completed tasks."""
    query = "SELECT * FROM tasks WHERE completed = 0" if not show_completed else "SELECT * FROM tasks"
    cursor.execute(query)
    tasks = cursor.fetchall()
    for task in tasks:
        status = "Completed" if task[4] else "Pending"
        print(f"ID: {task[0]}, Title: {task[1]}, Due Date: {task[3]}, Status: {status}")
        print(f"Description: {task[2]}")
        print("-" * 40)

def update_task(task_id, title=None, description=None, due_date=None):
    """Update task details."""
    if title:
        cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (title, task_id))
    if description:
        cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (description, task_id))
    if due_date:
        cursor.execute("UPDATE tasks SET due_date = ? WHERE id = ?", (due_date, task_id))
    conn.commit()
    print("Task updated successfully.")

def delete_task(task_id):
    """Delete a task from the database."""
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("Task deleted successfully.")

def mark_task_completed(task_id):
    """Mark a task as completed."""
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    print("Task marked as completed.")

def main():
    """Main program loop."""
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
        elif choice == '2':
            show_completed = input("Show completed tasks? (y/n): ").lower() == 'y'
            list_tasks(show_completed)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ")
            update_task(task_id, title, description, due_date)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

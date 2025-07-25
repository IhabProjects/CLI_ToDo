import typer
from datetime import datetime
from typing import Optional
from rich.console import Console
from rich.table import Table
from app.storage import Storage
from app.logic import TodoManager

app = typer.Typer()
console = Console()
storage = Storage()
todo_manager = TodoManager(storage)

def print_tasks(tasks, title: str):
    if not tasks:
        console.print(f"No {title.lower()} tasks found.", style="yellow")
        return

    table = Table(title=title)
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Description", style="blue")
    table.add_column("Due Date", style="magenta")
    table.add_column("Status", style="yellow")
    table.add_column("Days Left", style="red")

    for idx, task in enumerate(tasks):
        status = "✔️" if task.completed else "❌"
        days_left = task.days_until_due()
        days_left_str = f"{days_left} days" if days_left > 0 else "Overdue!"
        table.add_row(
            str(idx),
            task.title,
            task.description,
            task.due_date.strftime("%Y-%m-%d"),
            status,
            days_left_str
        )

    console.print(table)

@app.command()
def add(title: str, description: str, due_date: str = typer.Option(None, help="Due date in YYYY-MM-DD format")):
    """Add a new task"""
    try:
        due = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
        task = todo_manager.add_task(title, description, due)
        console.print(f"✅ Added task: {task.title}", style="green")
    except ValueError:
        console.print("❌ Invalid date format. Please use YYYY-MM-DD", style="red")

@app.command()
def list(status: str = typer.Option("all", help="Filter tasks by status: all/pending/completed/overdue")):
    """List tasks with optional status filter"""
    if status == "pending":
        tasks = todo_manager.get_pending_tasks()
        print_tasks(tasks, "Pending Tasks")
    elif status == "completed":
        tasks = todo_manager.get_completed_tasks()
        print_tasks(tasks, "Completed Tasks")
    elif status == "overdue":
        tasks = todo_manager.get_overdue_tasks()
        print_tasks(tasks, "Overdue Tasks")
    else:
        tasks = todo_manager.get_all_tasks()
        print_tasks(tasks, "All Tasks")

@app.command()
def complete(task_id: int):
    """Mark a task as completed"""
    if todo_manager.complete_task(task_id):
        console.print(f"✅ Task {task_id} marked as completed", style="green")
    else:
        console.print(f"❌ Task {task_id} not found", style="red")

@app.command()
def delete(task_id: int):
    """Delete a task"""
    if todo_manager.delete_task(task_id):
        console.print(f"🗑️ Task {task_id} deleted", style="green")
    else:
        console.print(f"❌ Task {task_id} not found", style="red")

@app.command()
def update(
    task_id: int,
    title: Optional[str] = typer.Option(None, help="New title"),
    description: Optional[str] = typer.Option(None, help="New description"),
    due_date: Optional[str] = typer.Option(None, help="New due date in YYYY-MM-DD format")
):
    """Update a task"""
    try:
        due = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
        if todo_manager.update_task(task_id, title, description, due):
            console.print(f"✅ Task {task_id} updated", style="green")
        else:
            console.print(f"❌ Task {task_id} not found", style="red")
    except ValueError:
        console.print("❌ Invalid date format. Please use YYYY-MM-DD", style="red")

if __name__ == "__main__":
    app()

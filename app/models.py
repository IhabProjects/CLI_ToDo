# I will define the tasks model in here 
from datetime import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Task:
    def __init__(self, title, description, created_at=None, due_date=None):
        self.title = title
        self.description = description
        self.created_at = created_at or datetime.now()
        self.due_date = due_date if due_date else datetime.now()
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        return f"[{status}] {self.title} - {self.description} (Due: {self.due_date.strftime('%Y-%m-%d')}) (Remaining: {self.days_until_due()} days)"

    def __repr__(self):
        return f"Task(title={self.title}, description={self.description}, created_at={self.created_at}, due_date={self.due_date}, completed={self.completed})"

    def is_overdue(self):
        return self.due_date < datetime.now() and not self.completed

    def days_until_due(self):
        if self.due_date < datetime.now():
            return 0
        return (self.due_date - datetime.now()).days + 1
    
# I will define the tasks model in here 
from datetime import datetime

class User:
    """
    Represents a user in the todo application.
    
    Attributes:
        username (str): The unique username of the user
        password (str): The user's password (Note: In production, this should be hashed)
    """
    def __init__(self, username: str, password: str):
        """
        Initialize a new user.
        
        Args:
            username (str): The username for the new user
            password (str): The password for the new user
        """
        self.username = username
        self.password = password

class Task:
    """
    Represents a todo task with title, description, dates, and completion status.
    
    Attributes:
        title (str): The title of the task
        description (str): Detailed description of the task
        created_at (datetime): When the task was created
        due_date (datetime): When the task is due
        completed (bool): Whether the task is completed
    """
    def __init__(self, title: str, description: str, created_at=None, due_date=None):
        """
        Initialize a new task.
        
        Args:
            title (str): The title of the task
            description (str): Detailed description of the task
            created_at (datetime, optional): When the task was created. Defaults to current time.
            due_date (datetime, optional): When the task is due. Defaults to current time.
        """
        self.title = title
        self.description = description
        self.created_at = created_at or datetime.now()
        self.due_date = due_date if due_date else datetime.now()
        self.completed = False

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def __str__(self) -> str:
        """
        Returns a string representation of the task.
        
        Returns:
            str: A formatted string showing task status, title, description, and due date
        """
        status = "✔️" if self.completed else "❌"
        return f"[{status}] {self.title} - {self.description} (Due: {self.due_date.strftime('%Y-%m-%d')}) (Remaining: {self.days_until_due()} days)"

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the task.
        
        Returns:
            str: A string containing all task attributes
        """
        return f"Task(title={self.title}, description={self.description}, created_at={self.created_at}, due_date={self.due_date}, completed={self.completed})"

    def is_overdue(self) -> bool:
        """
        Check if the task is overdue.
        
        Returns:
            bool: True if the task is past its due date and not completed
        """
        return self.due_date < datetime.now() and not self.completed

    def days_until_due(self) -> int:
        """
        Calculate the number of days until the task is due.
        
        Returns:
            int: Number of days until due date, or 0 if already overdue
        """
        if self.due_date < datetime.now():
            return 0
        return (self.due_date - datetime.now()).days + 1
    
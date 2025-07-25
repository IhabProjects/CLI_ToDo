from datetime import datetime
from typing import List, Optional
from .models import Task, User
from .storage import Storage

class TodoManager:
    """
    Manages the business logic for the todo application.
    
    This class handles all task and user operations, including authentication,
    task management, and filtering. It uses a Storage instance for persistence.
    
    Attributes:
        storage (Storage): The storage instance for persistence
        _current_user (Optional[User]): Currently authenticated user
    """
    
    def __init__(self, storage: Storage):
        """
        Initialize the TodoManager.
        
        Args:
            storage (Storage): Storage instance for data persistence
        """
        self.storage = storage
        self._current_user: Optional[User] = None

    @property
    def is_authenticated(self) -> bool:
        """
        Check if a user is currently authenticated.
        
        Returns:
            bool: True if a user is logged in, False otherwise
        """
        return self._current_user is not None

    def login(self, username: str, password: str) -> bool:
        """
        Authenticate a user.
        
        Args:
            username (str): Username to authenticate
            password (str): Password to verify
            
        Returns:
            bool: True if authentication successful, False otherwise
        """
        user = self.storage.get_user(username)
        if user and user.password == password:  # In a real app, use proper password hashing
            self._current_user = user
            return True
        return False

    def register(self, username: str, password: str) -> bool:
        """
        Register a new user.
        
        Args:
            username (str): Username for new user
            password (str): Password for new user
            
        Returns:
            bool: True if registration successful, False if username exists
        """
        if self.storage.get_user(username):
            return False
        user = User(username, password)
        self.storage.add_user(user)
        return True

    def logout(self) -> None:
        """Log out the current user."""
        self._current_user = None

    def add_task(self, title: str, description: str, due_date: Optional[datetime] = None) -> Task:
        """
        Create and store a new task.
        
        Args:
            title (str): Task title
            description (str): Task description
            due_date (Optional[datetime]): When the task is due
            
        Returns:
            Task: The created task object
        """
        task = Task(title, description, due_date=due_date)
        self.storage.add_task(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            List[Task]: List of all tasks
        """
        return self.storage.get_all_tasks()

    def get_pending_tasks(self) -> List[Task]:
        """
        Get all uncompleted tasks.
        
        Returns:
            List[Task]: List of pending tasks
        """
        return [task for task in self.get_all_tasks() if not task.completed]

    def get_completed_tasks(self) -> List[Task]:
        """
        Get all completed tasks.
        
        Returns:
            List[Task]: List of completed tasks
        """
        return [task for task in self.get_all_tasks() if task.completed]

    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all overdue tasks.
        
        Returns:
            List[Task]: List of overdue tasks
        """
        return [task for task in self.get_all_tasks() if task.is_overdue()]

    def complete_task(self, index: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            index (int): Index of the task to complete
            
        Returns:
            bool: True if task was completed, False if index invalid
        """
        tasks = self.storage.get_all_tasks()
        if 0 <= index < len(tasks):
            task = tasks[index]
            task.mark_completed()
            return self.storage.update_task(index, task)
        return False

    def delete_task(self, index: int) -> bool:
        """
        Delete a task.
        
        Args:
            index (int): Index of the task to delete
            
        Returns:
            bool: True if task was deleted, False if index invalid
        """
        return self.storage.delete_task(index)

    def update_task(self, index: int, title: Optional[str] = None, 
                   description: Optional[str] = None, due_date: Optional[datetime] = None) -> bool:
        """
        Update a task's attributes.
        
        Args:
            index (int): Index of the task to update
            title (Optional[str]): New title if provided
            description (Optional[str]): New description if provided
            due_date (Optional[datetime]): New due date if provided
            
        Returns:
            bool: True if task was updated, False if index invalid
        """
        tasks = self.storage.get_all_tasks()
        if 0 <= index < len(tasks):
            task = tasks[index]
            if title:
                task.title = title
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            return self.storage.update_task(index, task)
        return False

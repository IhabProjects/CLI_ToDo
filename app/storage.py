import json
from datetime import datetime
from typing import List, Dict
from .models import Task, User

class Storage:
    """
    Handles persistent storage of tasks and users using JSON files.
    
    This class provides methods to save and load tasks and users from JSON files.
    It handles serialization and deserialization of Task and User objects.
    
    Attributes:
        tasks_file (str): Path to the JSON file storing tasks
        users_file (str): Path to the JSON file storing users
    """
    
    def __init__(self, tasks_file: str = "tasks.json", users_file: str = "users.json"):
        """
        Initialize the storage with file paths.
        
        Args:
            tasks_file (str): Path to tasks JSON file. Defaults to "tasks.json"
            users_file (str): Path to users JSON file. Defaults to "users.json"
        """
        self.tasks_file = tasks_file
        self.users_file = users_file

    def _load_tasks(self) -> List[Dict]:
        """
        Load tasks from the JSON file.
        
        Returns:
            List[Dict]: List of task dictionaries. Empty list if file doesn't exist.
        """
        try:
            with open(self.tasks_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_tasks(self, tasks: List[Dict]) -> None:
        """
        Save tasks to the JSON file.
        
        Args:
            tasks (List[Dict]): List of task dictionaries to save
        """
        with open(self.tasks_file, 'w') as f:
            json.dump(tasks, f, indent=2, default=str)

    def _load_users(self) -> List[Dict]:
        """
        Load users from the JSON file.
        
        Returns:
            List[Dict]: List of user dictionaries. Empty list if file doesn't exist.
        """
        try:
            with open(self.users_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_users(self, users: List[Dict]) -> None:
        """
        Save users to the JSON file.
        
        Args:
            users (List[Dict]): List of user dictionaries to save
        """
        with open(self.users_file, 'w') as f:
            json.dump(users, f, indent=2)

    def add_task(self, task: Task) -> None:
        """
        Add a new task to storage.
        
        Args:
            task (Task): The task object to store
        """
        tasks = self._load_tasks()
        task_dict = {
            'title': task.title,
            'description': task.description,
            'created_at': task.created_at.isoformat(),
            'due_date': task.due_date.isoformat(),
            'completed': task.completed
        }
        tasks.append(task_dict)
        self._save_tasks(tasks)

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks from storage.
        
        Returns:
            List[Task]: List of Task objects
        """
        tasks = []
        for task_dict in self._load_tasks():
            task = Task(
                title=task_dict['title'],
                description=task_dict['description'],
                created_at=datetime.fromisoformat(task_dict['created_at']),
                due_date=datetime.fromisoformat(task_dict['due_date'])
            )
            task.completed = task_dict['completed']
            tasks.append(task)
        return tasks

    def update_task(self, index: int, task: Task) -> bool:
        """
        Update a task at the specified index.
        
        Args:
            index (int): Index of the task to update
            task (Task): Updated task object
            
        Returns:
            bool: True if task was updated, False if index is invalid
        """
        tasks = self._load_tasks()
        if 0 <= index < len(tasks):
            tasks[index] = {
                'title': task.title,
                'description': task.description,
                'created_at': task.created_at.isoformat(),
                'due_date': task.due_date.isoformat(),
                'completed': task.completed
            }
            self._save_tasks(tasks)
            return True
        return False

    def delete_task(self, index: int) -> bool:
        """
        Delete a task at the specified index.
        
        Args:
            index (int): Index of the task to delete
            
        Returns:
            bool: True if task was deleted, False if index is invalid
        """
        tasks = self._load_tasks()
        if 0 <= index < len(tasks):
            tasks.pop(index)
            self._save_tasks(tasks)
            return True
        return False

    def add_user(self, user: User) -> None:
        """
        Add a new user to storage.
        
        Args:
            user (User): The user object to store
        """
        users = self._load_users()
        user_dict = {
            'username': user.username,
            'password': user.password  # In a real app, this should be hashed
        }
        users.append(user_dict)
        self._save_users(users)

    def get_user(self, username: str) -> User | None:
        """
        Retrieve a user by username.
        
        Args:
            username (str): Username to search for
            
        Returns:
            User | None: User object if found, None otherwise
        """
        users = self._load_users()
        for user_dict in users:
            if user_dict['username'] == username:
                return User(
                    username=user_dict['username'],
                    password=user_dict['password']
                )
        return None

import json
from datetime import datetime
from typing import List, Dict
from .models import Task, User

class Storage:
    def __init__(self, tasks_file: str = "tasks.json", users_file: str = "users.json"):
        self.tasks_file = tasks_file
        self.users_file = users_file

    def _load_tasks(self) -> List[Dict]:
        try:
            with open(self.tasks_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_tasks(self, tasks: List[Dict]) -> None:
        with open(self.tasks_file, 'w') as f:
            json.dump(tasks, f, indent=2, default=str)

    def _load_users(self) -> List[Dict]:
        try:
            with open(self.users_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_users(self, users: List[Dict]) -> None:
        with open(self.users_file, 'w') as f:
            json.dump(users, f, indent=2)

    def add_task(self, task: Task) -> None:
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
        tasks = self._load_tasks()
        if 0 <= index < len(tasks):
            tasks.pop(index)
            self._save_tasks(tasks)
            return True
        return False

    def add_user(self, user: User) -> None:
        users = self._load_users()
        user_dict = {
            'username': user.username,
            'password': user.password  # In a real app, this should be hashed
        }
        users.append(user_dict)
        self._save_users(users)

    def get_user(self, username: str) -> User | None:
        users = self._load_users()
        for user_dict in users:
            if user_dict['username'] == username:
                return User(
                    username=user_dict['username'],
                    password=user_dict['password']
                )
        return None

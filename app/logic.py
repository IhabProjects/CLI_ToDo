from datetime import datetime
from typing import List, Optional
from .models import Task, User
from .storage import Storage

class TodoManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self._current_user: Optional[User] = None

    @property
    def is_authenticated(self) -> bool:
        return self._current_user is not None

    def login(self, username: str, password: str) -> bool:
        user = self.storage.get_user(username)
        if user and user.password == password:  # In a real app, use proper password hashing
            self._current_user = user
            return True
        return False

    def register(self, username: str, password: str) -> bool:
        if self.storage.get_user(username):
            return False
        user = User(username, password)
        self.storage.add_user(user)
        return True

    def logout(self) -> None:
        self._current_user = None

    def add_task(self, title: str, description: str, due_date: Optional[datetime] = None) -> Task:
        task = Task(title, description, due_date=due_date)
        self.storage.add_task(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.storage.get_all_tasks()

    def get_pending_tasks(self) -> List[Task]:
        return [task for task in self.get_all_tasks() if not task.completed]

    def get_completed_tasks(self) -> List[Task]:
        return [task for task in self.get_all_tasks() if task.completed]

    def get_overdue_tasks(self) -> List[Task]:
        return [task for task in self.get_all_tasks() if task.is_overdue()]

    def complete_task(self, index: int) -> bool:
        tasks = self.storage.get_all_tasks()
        if 0 <= index < len(tasks):
            task = tasks[index]
            task.mark_completed()
            return self.storage.update_task(index, task)
        return False

    def delete_task(self, index: int) -> bool:
        return self.storage.delete_task(index)

    def update_task(self, index: int, title: Optional[str] = None, 
                   description: Optional[str] = None, due_date: Optional[datetime] = None) -> bool:
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

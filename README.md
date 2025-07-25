# Command Line ToDo List with File Storage

A feature-rich command-line todo list application built with Python. Manage your tasks efficiently with a beautiful CLI interface.

## Features

- ✨ Beautiful CLI interface with colors and tables
- 📝 Create, read, update, and delete tasks
- 📅 Set due dates for tasks
- ✅ Mark tasks as completed
- 🔍 Filter tasks by status (all/pending/completed/overdue)
- 💾 Persistent storage using JSON files

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd CLI_ToDo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The application provides the following commands:

### Add a new task
```bash
python main.py add "Task Title" "Task Description" --due-date "2024-12-31"
```

### List tasks
```bash
# List all tasks
python main.py list

# List pending tasks
python main.py list --status pending

# List completed tasks
python main.py list --status completed

# List overdue tasks
python main.py list --status overdue
```

### Complete a task
```bash
python main.py complete TASK_ID
```

### Update a task
```bash
python main.py update TASK_ID --title "New Title" --description "New Description" --due-date "2024-12-31"
```

### Delete a task
```bash
python main.py delete TASK_ID
```

## Help
For detailed information about any command, use the --help option:
```bash
python main.py --help
python main.py COMMAND --help
```

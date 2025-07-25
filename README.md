# Command Line ToDo List with File Storage

A feature-rich command-line todo list application built with Python. Manage your tasks efficiently with a beautiful CLI interface.

## Features

- ✨ Beautiful CLI interface with colors and tables
- 📝 Create, read, update, and delete tasks
- 📅 Set due dates for tasks
- ✅ Mark tasks as completed
- 🔍 Filter tasks by status (all/pending/completed/overdue)
- 💾 Persistent storage using JSON files
- 🎨 Rich text formatting and emojis
- 📊 Task progress tracking
- ⏰ Due date management and overdue detection

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

## Quick Start

1. Add your first task:
```bash
python main.py add "Complete project" "Finish the CLI todo app" --due-date "2024-03-20"
```

2. List all tasks:
```bash
python main.py list
```

3. Mark a task as completed:
```bash
python main.py complete 0  # 0 is the task ID
```

## Detailed Usage

### Task Management

#### Adding Tasks
```bash
# Basic task
python main.py add "Task Title" "Task Description"

# Task with due date
python main.py add "Important Task" "Must do this" --due-date "2024-12-31"
```

#### Listing Tasks
```bash
# List all tasks
python main.py list

# List only pending tasks
python main.py list --status pending

# List completed tasks
python main.py list --status completed

# List overdue tasks
python main.py list --status overdue
```

#### Updating Tasks
```bash
# Update title
python main.py update 0 --title "New Title"

# Update description
python main.py update 0 --description "New description"

# Update due date
python main.py update 0 --due-date "2024-12-31"

# Update multiple attributes
python main.py update 0 --title "New Title" --description "New description" --due-date "2024-12-31"
```

#### Task Operations
```bash
# Mark task as completed
python main.py complete 0

# Delete task
python main.py delete 0
```

### Advanced Features

#### Date Formats
The application accepts dates in "YYYY-MM-DD" format. Examples:
- Today: Use current date
- Future date: "2024-12-31"
- Past date: "2023-12-31"

#### Task Status
Tasks can have the following statuses:
- Pending (❌): Task is not completed
- Completed (✔️): Task is marked as done
- Overdue: Task's due date has passed

#### Task Storage
Tasks are stored in a JSON file (`tasks.json`) in the following format:
```json
[
  {
    "title": "Example Task",
    "description": "This is a task",
    "created_at": "2024-03-15T10:00:00",
    "due_date": "2024-03-20T00:00:00",
    "completed": false
  }
]
```

## Project Structure

```
CLI_ToDo/
├── app/
│   ├── __init__.py
│   ├── models.py      # Data models (Task, User)
│   ├── storage.py     # JSON file storage
│   └── logic.py       # Business logic
├── main.py            # CLI interface
├── requirements.txt   # Dependencies
└── README.md         # Documentation
```

## Development

### Adding New Features

1. Models (`app/models.py`):
   - Add new model classes or attributes
   - Update string representations
   - Add validation methods

2. Storage (`app/storage.py`):
   - Implement data persistence
   - Add new storage methods
   - Handle serialization/deserialization

3. Logic (`app/logic.py`):
   - Implement business rules
   - Add new task operations
   - Handle task filtering and updates

4. CLI (`main.py`):
   - Add new commands using `@app.command()`
   - Implement command options
   - Update help messages

### Best Practices

1. Error Handling:
   - Use try-except blocks for file operations
   - Validate user input
   - Provide clear error messages

2. Code Style:
   - Follow PEP 8 guidelines
   - Use type hints
   - Add docstrings to classes and methods

3. Testing:
   - Test edge cases
   - Verify file operations
   - Check task operations

## Troubleshooting

### Common Issues

1. **Invalid Date Format**
   - Ensure dates are in "YYYY-MM-DD" format
   - Example: "2024-03-20"

2. **Task Not Found**
   - Verify task ID exists
   - List tasks to see available IDs

3. **File Permission Issues**
   - Check write permissions in directory
   - Verify JSON files are not locked

### Data Recovery

The application stores data in two files:
- `tasks.json`: Task data
- `users.json`: User data (if implemented)

To backup data:
1. Copy these files to a safe location
2. Restore by copying back to application directory

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

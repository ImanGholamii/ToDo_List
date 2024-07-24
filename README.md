# 📝 ToDo List CLI Application

Welcome to the ToDo List CLI Application! This project is a simple yet powerful task manager built using Python, designed to help you efficiently manage your tasks right from the command line.

## 🌟 Features

- **Add Tasks**: Create new tasks with optional priority settings.
- **Remove Tasks**: Delete tasks you no longer need.
- **Update Tasks**: Modify existing tasks with new details.
- **View Tasks**: Display all tasks in a clear and organized format.
- **Search Tasks**: Find tasks by title or content.
- **Filter by Priority**: View only the tasks marked as important.
- **Future Enhancements**: Plan to save task data to a JSON file for persistence.

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ImanGholamii/ToDo_List.git
   cd ToDo_List
   ```

2. Run the application:
   ```sh
   python todo_list.py
   ```

## 📚 Usage

1. **Add a new task:**
   ```sh
   What is your task Title? Task 1
   What is your task Component? Complete the report
   Do you want to set priority? (yes or no) yes
   ```

2. **Modify an existing task:**
   ```sh
   Updating task...
   What is your task Title to Update? Task 1
   What is your task Component? Complete the financial report
   Do you want to set priority? (yes or no) no
   ```

3. **Delete a task:**
   ```sh
   What is your task Title to delete? Task 1
   ```

4. **View all tasks:**
   ```sh
   📋 All tasks:
   ⚪ Title: Task 1
    |_>>> Priority: ⭐
    |_>>> Component: Complete the report
   ```

5. **Search for a task by title:**
   ```sh
   What is your task Title? Task 1
   ```

6. **Search for tasks by component:**
   ```sh
   Enter a Word to search in tasks content: report
   ```

7. **Filter tasks by priority:**
   ```sh
   Showing tasks with priority:
   ⚪ Title: Task 1
    |_>>> Priority: ⭐
    |_>>> Component: Complete the report
   ```

## 📈 Future Enhancements

- **Persisting Data**: Add functionality to save tasks to a JSON file for data persistence.
- **Update scenarios**: Add more logics to update tasks.
- **Task Categories**: Introduce categories or tags to group and filter tasks more efficiently.
- **Task Sorting**: Allow tasks to be sorted by priority, due date, or creation date.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgements

- Special thanks to the developers of the Python programming language.
- Inspiration from various task manager CLI tools.

## ⭐️ Support

If you like this project, please give it a ⭐️ on [GitHub](https://github.com/ImanGholamii/ToDo_List)!

tasks = {}
untitled_task_counter = 1
duplicate_title_counter = 1


def set_priority_to_task():
    """Setting priority to task"""
    set_priority = input("Do you want to set priority? (yes or no) ").lower()
    if set_priority == 'yes':
        set_priority = True
    elif set_priority == 'no':
        set_priority = False
    else:
        set_priority = False
    return set_priority


def check_title(title: str):
    """Check title Validity (repetitive and existence)"""
    global untitled_task_counter, duplicate_title_counter
    if title in tasks:
        title = title + str(".") + str(duplicate_title_counter)
        duplicate_title_counter += 1
        return title
    elif title == "":
        title = "No Title." + str(untitled_task_counter)
        untitled_task_counter += 1
        return title
    else:
        return title


def add_task():
    """Add a new task"""
    global untitled_task_counter
    title_input, component = input("What is your task Title? ").strip().title(), input(
        "What is your task Component? ").strip()
    title = check_title(title=title_input)
    tasks[title] = {
        "component": component,
        "is_important": set_priority_to_task(),

    }


def remove_task():
    """remove task from tasks dict by prompt title"""
    title = input("deleting task...\nWhat is your task Title to delete? ").title()
    if title in tasks:
        print(f"🔄 Deleting {title}...")
        del tasks[title]
        print(f"✔️ Deleted Successfully!")
    else:
        print("Task not found")


def update_task():
    """Update tasks component by prompt title"""
    title = input("Updating task...\nWhat is your task Title to Update? ").title()

    if title in tasks:
        new_component = input("What is your task Component? ")
        print(f"🔄 Updating {title}'s Content...")
        tasks[title] = {
            "component": new_component,
            "is_important": set_priority_to_task(),
        }
        print(f"✔️ Updated Successfully!")
    else:
        print("Task not found")


def show_task(dictionary, title):
    """show task by specific title"""
    if dictionary[title]["is_important"]:
        is_important = "⭐"
    else:
        is_important = "⬜"

    print(f"⚪ Title: {title}\n |_>>> Priority: {is_important}\n"
          f" |_>>> Component: {dictionary[title]['component']}")


def view_all_task(dictionary=tasks):
    """View all tasks by format"""
    print("📋 All tasks: ")
    if len(dictionary) > 0:
        for title in dictionary:
            show_task(dictionary, title=title)
    else:
        print("No tasks found!")


def search_task_title():
    """Search a specific task by title"""
    print("Searching task... 🔍")
    title = input("What is your task Title? ").title()
    if title in tasks:
        show_task(dictionary=tasks, title=title)
    else:
        print("Task not found")


def search_task_component():
    """Search in all task components"""
    global search_results
    search_results = {}
    print("Searching task components ... 🔍")
    word = input("Enter a Word to search in tasks content: ").lower()
    for title in tasks:
        if word in tasks[title]["component"]:
            search_results.update({
                title: tasks[title]
            })
    if len(search_results) > 0:
        view_all_task(dictionary=search_results)
        del search_results
    else:
        print(f"The {word} not found")


def filter_by_priority():
    """Filters tasks by priorities 🔻"""
    if len(tasks) != 0:
        print("Filtered tasks by priority (🔻)")
        important_task_found = False
        for title in tasks:
            if tasks[title]["is_important"]:
                show_task(dictionary=tasks, title=title)
                important_task_found = True
        if not important_task_found:
            print(" (❗) No important tasks found!")
    else:
        print("Task not found!")


def main():
    while True:
        what_to_do = input(
            "\nWhat do you want to do? \n_ 1) add new task\n_ 2)"
            " modify existing task\n_ 3) delete a task\n_ 4) view all tasks\n_ 5) search in task title\n"
            "_ 6) search in task component\n_ 7) filter by priority\n_ 8) exit the program\n>>> ")
        if what_to_do == "1":
            add_task()
        elif what_to_do == "2":
            update_task()
        elif what_to_do == "3":
            remove_task()
        elif what_to_do == "4":
            view_all_task()
        elif what_to_do == "5":
            search_task_title()
        elif what_to_do == "6":
            search_task_component()
        elif what_to_do == "7":
            filter_by_priority()
        elif what_to_do == "8":
            break


if __name__ == "__main__":
    main()

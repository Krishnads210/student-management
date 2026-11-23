from sms import operations, storage, validators
from sms.logger import logger


def show_menu() -> None:
    # print options: 1 Add, 2 Remove, 3 Update, 4 Search, 5 Display, 6 Exit
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display Student")
    print("6. Exit")


def get_user_choice() -> int:
    raw = input("Please choose an option (1-6): ").strip()
    try:
        choice = int(raw)
    except ValueError:
        raise ValueError("Please enter a number between 1 and 6")
    if choice < 1 or choice > 6:
        raise ValueError("Please enter a number between 1 and 6")
    return choice


def handle_add(students: dict) -> None:
    student_id = validators.validate_id(input("Enter student ID: "))
    name = validators.validate_name(input("Enter name: "))
    age = validators.validate_age(input("Enter age: "))
    major = validators.validate_major(input("Enter major: "))
    operations.add_student(students, student_id, name, age, major)
    storage.save_students(students)
    print(f"Student {student_id} added.")


def handle_remove(students: dict) -> None:
    # input + validate ID -> operations.remove_student -> save
    student_id = validators.validate_id(input("Enter student ID: "))
    operations.remove_student(students,student_id)
    storage.save_students(students)
    print(f"Student {student_id} removed.")


def handle_update(students: dict) -> None:
    # input + validate ID, field, new value (Age goes through validate_age)
    # -> operations.update_student -> save
    student_id = validators.validate_id(input("Enter student ID: "))
    field = validators.validate_field(input("Field to be updated (Name, Age, Major)"))
    raw = input(f"Please choose a {field}: ")
    if field == "Age":
        new_value = validators.validate_age(raw)
    elif field == "Name":
        new_value = validators.validate_name(raw)
    else:
        new_value = validators.validate_major(raw)
    operations.update_student(students,student_id,field,new_value)
    storage.save_students(students)
    print(f"Student {student_id} updated.")



def handle_search(students: dict) -> None:
    # input + validate ID -> operations.search_student -> print it
    student_id = validators.validate_id(input("Enter student ID: "))
    s = operations.search_student(students,student_id)
    print(f"ID: {student_id} | Name: {s['Name']} | Age: {s['Age']} | Major: {s['Major']}")


def handle_display(students: dict) -> None:
    all_students = operations.get_all_students(students)
    if not all_students:
        print("No students yet.")
        return
    for student_id, s in all_students.items():
        print(student_id, s["Name"], s["Age"], s["Major"])




MAX_ACTIONS = 100


def main() -> None:
    logger.info("Program started")
    students = storage.load_students()
    handlers = {1: handle_add, 2: handle_remove, 3: handle_update,
                4: handle_search, 5: handle_display}

    for _ in range(MAX_ACTIONS):
        try:
            show_menu()
            choice = get_user_choice()
            if choice == 6:
                logger.info("Program exited")
                print("Goodbye!")
                break
            handlers[choice](students)
        except ValueError as e:
            logger.warning(f"Invalid input: {e}")
            print(e)
        except OSError as e:
            logger.error(f"File problem: {e}")
            print(f"File problem: {e}")
        except KeyboardInterrupt:
            logger.info("Program stopped with Ctrl+C")
            print("\nGoodbye!")
            break
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print("Unexpected error. Check student.log")
    else:
        logger.info(f"Program ended after {MAX_ACTIONS} actions")
        print(f"Reached the limit of {MAX_ACTIONS} actions. Goodbye!")


if __name__ == "__main__":
    main()

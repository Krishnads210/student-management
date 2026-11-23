from sms.logger import logger
from sms.models import create_student


def find_student(students: dict, student_id: int) -> dict:
    # not in students -> log warning, raise KeyError(f"ID {student_id} not found")
    if student_id not in students:
        logger.warning(f"Student ID {student_id} not found")
        raise ValueError(f"Student ID {student_id} not found")
    # else return students[student_id]
    else:
        return students[student_id]


def add_student(students: dict, student_id: int, name: str, age: int, major: str) -> None:
    # ID already exists -> log warning, raise ValueError("... already exists")
    if student_id in students:
        logger.warning(f"Student ID {student_id} already exists")
        raise ValueError(f"Student ID {student_id} already exists")
    # else students[student_id] = create_student(name, age, major), log info
    else:
        students[student_id] = create_student(name,age,major)
        logger.info(f"Added student {student_id}: {name}")



def remove_student(students: dict, student_id: int) -> None:
    find_student(students, student_id)   # raises if missing
    students.pop(student_id)
    logger.info(f"Removed student {student_id}")


def update_student(students: dict, student_id: int, field: str, new_value) -> None:
    student = find_student(students, student_id)
    student[field] = new_value
    logger.info(f"Updated student {student_id}: {field} = {new_value}")





def search_student(students: dict, student_id: int) -> dict:
    logger.info(f"Searched for student {student_id}")
    return find_student(students, student_id)



def get_all_students(students: dict) -> dict:
    # log info, return students
    logger.info("All student data requested")
    return students

import json

from sms.logger import logger

DATA_FILE = "students.json"


def load_students() -> dict:
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        logger.warning("No students.json yet, starting empty")
        return {}

    students = {}
    for key, value in data.items():
        students[int(key)] = value      # JSON keys come back as text: "1" -> 1
    logger.info("Students loaded")
    return students


def save_students(students: dict) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)
    logger.info("Students saved")
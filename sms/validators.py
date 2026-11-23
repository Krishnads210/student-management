def validate_id(raw: str) -> int:
    # strip -> int() -> must be > 0, else raise ValueError
    raw = raw.strip()
    try:
        student_id = int(raw)
    except ValueError:
        raise ValueError("ID must be a number")
    if student_id <= 0:
        raise ValueError("ID must be greater than 0")
    return student_id



def validate_name(raw: str) -> str:
    name = raw.strip()
    if not name:
        raise ValueError("Name cannot be empty")
    if not name.replace(" ", "").isalpha():
        raise ValueError("Name must contain only letters and spaces")
    return name.title()


def validate_age(raw: str) -> int:
    # int() -> range check (e.g. 5 to 100), else raise ValueError
    age = raw.strip()
    try:
        age = int(raw)
    except ValueError:
        raise ValueError("age must be a number")
    if age < 5 or age > 100:
        raise ValueError("Age must be between 5 and 100")
    return age


def validate_major(raw: str) -> str:
    # strip -> not empty
    major = raw.strip()
    if not major:
        raise ValueError("Major cannot be blank")
    return major



def validate_field(raw: str) -> str:
    field = raw.strip().title()
    if field not in ("Name", "Age", "Major"):
        raise ValueError("Field must be Name, Age or Major")
    return field
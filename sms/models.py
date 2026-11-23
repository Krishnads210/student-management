def create_student(name: str, age: int, major: str) -> dict:
    """Build one student record. The ID is not stored here;
    it is the key in the students dictionary."""
    return {"Name": name, "Age": age, "Major": major}
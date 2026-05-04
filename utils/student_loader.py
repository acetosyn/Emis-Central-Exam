import csv
import os
import re
from flask import current_app


STUDENT_DATABASE_FILES = [
    "JSS1_Students.csv",
    "JSS2_Students.csv",
    "JSS3_Students.csv",
    "SS1_Students.csv",
    "SS2_Students.csv",
    "SS3_Students.csv",
]


def normalize_text(value):
    if not value:
        return ""

    value = str(value).strip().lower()
    value = re.sub(r"[^a-z0-9]", "", value)

    return value


def normalize_class_name(value):
    if not value:
        return ""

    value = str(value).strip().upper()
    value = value.replace("JS", "JSS", 1) if value.startswith("JS") and not value.startswith("JSS") else value
    value = re.sub(r"\s+", "", value)

    return value


def get_class_from_filename(filename):
    return filename.replace("_Students.csv", "").strip().upper()


def load_students_from_file(filename):
    csv_path = os.path.join(current_app.static_folder, "data", filename)
    students = []

    if not os.path.exists(csv_path):
        return students

    database_class = get_class_from_filename(filename)

    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = dict(row)

            student["Database_file"] = filename
            student["Database_class"] = database_class

            if not student.get("Class_category"):
                student["Class_category"] = database_class

            if not student.get("Class"):
                student["Class"] = database_class

            students.append(student)

    return students


def load_students():
    students = []

    for filename in STUDENT_DATABASE_FILES:
        students.extend(load_students_from_file(filename))

    return students


def find_student_by_login(admission_number, password):
    admission_number = normalize_text(admission_number)
    password = normalize_text(password)

    students = load_students()

    for student in students:
        student_admission = normalize_text(student.get("Admission_number", ""))
        student_last_name = normalize_text(student.get("Last_name", ""))

        if admission_number == student_admission and password == student_last_name:
            return student

    return None
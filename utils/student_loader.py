import csv
import os
import re
from flask import current_app


def normalize_text(value):
    if not value:
        return ""
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]", "", value)
    return value


def load_students():
    csv_path = os.path.join(current_app.static_folder, "data", "SS_Students.csv")
    students = []

    if not os.path.exists(csv_path):
        return students

    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    return students
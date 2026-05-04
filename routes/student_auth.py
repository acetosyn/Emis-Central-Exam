from flask import Blueprint, render_template, request, redirect, url_for, session
from utils.student_loader import find_student_by_login


student_auth_bp = Blueprint("student_auth", __name__)


@student_auth_bp.route("/student_login", methods=["GET", "POST"])
def student_login():
    if request.method == "POST":
        admission_number = request.form.get("admission_number", "")
        password = request.form.get("password", "")

        student = find_student_by_login(admission_number, password)

        if student:
            session["student"] = {
                "admission_number": student.get("Admission_number", ""),
                "last_name": student.get("Last_name", ""),
                "first_name": student.get("First_name", ""),
                "other_names": student.get("Other_names", ""),
                "phone": student.get("Phone", ""),
                "class": student.get("Class", ""),
                "class_category": student.get("Class_category", ""),
                "database_class": student.get("Database_class", ""),
                "database_file": student.get("Database_file", "")
            }

            return redirect(url_for("student_auth.dashboard"))

        return render_template(
            "student_login.html",
            error="Invalid admission number or password."
        )

    return render_template("student_login.html")


@student_auth_bp.route("/dashboard")
def dashboard():
    student = session.get("student")

    if not student:
        return redirect(url_for("student_auth.student_login"))

    return render_template("dashboard.html", student=student)


@student_auth_bp.route("/logout")
def logout():
    session.pop("student", None)
    return redirect(url_for("student_auth.student_login"))



@student_auth_bp.route("/test_students")
def test_students():
    from utils.student_loader import load_students

    students = load_students()

    return {
        "total_students_loaded": len(students),
        "sample": students[:3]
    }
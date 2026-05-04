from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import os
from dotenv import load_dotenv

load_dotenv()

admin_auth_bp = Blueprint("admin_auth", __name__)

@admin_auth_bp.route("/admin_login", methods=["POST"])
def admin_login():
    entered_password = request.form.get("admin_password", "").strip()
    correct_password = os.getenv("admin_password")

    if correct_password and entered_password == correct_password:
        session["admin_logged_in"] = True
        return redirect(url_for("admin_auth.admin_dashboard"))

    flash("Invalid admin password. Please try again.", "admin_error")
    return redirect(url_for("main.home"))


@admin_auth_bp.route("/admin")
def admin_dashboard():
    if not session.get("admin_logged_in"):
        flash("Please login as admin first.", "admin_error")
        return redirect(url_for("main.home"))

    return render_template("admin.html")


@admin_auth_bp.route("/admin_logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("main.home"))
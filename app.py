from flask import Flask
from routes.main import main_bp
from routes.student_auth import student_auth_bp
from routes.admin_auth import admin_auth_bp
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "emis_central_exam_secret_key")

app.register_blueprint(main_bp)
app.register_blueprint(student_auth_bp)
app.register_blueprint(admin_auth_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
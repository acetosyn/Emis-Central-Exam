from flask import Flask
from routes.main import main_bp
from routes.student_auth import student_auth_bp

app = Flask(__name__)
app.secret_key = "emis_central_exam_secret_key"

app.register_blueprint(main_bp)
app.register_blueprint(student_auth_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
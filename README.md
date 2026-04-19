# EMIS Central Exam

EMIS Central Exam is a Flask-based web application built for **Epitome Model Islamic Schools (EMIS)** to provide a centralized examination access portal for students and other academic-related services.

The platform currently includes:

- A modern **central exam landing page**
- A dedicated **student login portal**
- Authentication using **Admission Number** and **Last Name**
- Student data loading from a CSV file
- Blueprint-based Flask structure for cleaner project organization
- A scalable foundation for future modules such as dashboards, result checking, parent access, and more

---

## Features

### Central Exam Landing Page
The landing page serves as the main access point for EMIS examination services. It includes:

- Student Exam access
- Staff Recruitment access
- Senior Secondary School Exam Portal access
- Quick access cards and service overview
- Responsive design for desktop and mobile

### Student Login
Students log in using:

- **Username:** Admission Number  
- **Password:** Last Name

For password matching:
- All letters are converted to lowercase
- Spaces are removed
- Special characters are removed

#### Example:
- `Al-mumin` becomes `almumin`
- `Shafi'i` becomes `shafii`

### CSV-Based Authentication
Student records are loaded from:

```bash
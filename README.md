# 🚆 RailMaint

**RailMaint** is a web-based Railway Maintenance Management System (CMMS) built with Django and PostgreSQL. It digitizes the process of recording, tracking, and managing railway maintenance activities by replacing paper-based records with a centralized digital platform.

---

## 📖 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [System Workflow](#system-workflow)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Project](#running-the-project)
- [Default Admin Account](#default-admin-account)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Developer](#developer)

---

# Overview

RailMaint is a Railway Maintenance Management System designed to help railway organizations manage maintenance operations digitally.

Instead of storing maintenance records on paper, RailMaint provides a centralized database where maintenance supervisors and technicians can:

- Register railway assets
- Register maintenance employees
- Create maintenance work orders
- Assign technicians
- Record maintenance activities
- View complete maintenance history
- Monitor maintenance progress

---

# Problem Statement

Many railway organizations still rely on manual paperwork to record maintenance activities.

This approach creates several challenges:

- Lost or damaged maintenance records
- Slow retrieval of historical information
- Poor maintenance tracking
- Duplicate records
- Lack of accountability
- Difficulty generating reports
- Inefficient maintenance planning

---

# Solution

RailMaint replaces manual record keeping with a centralized web application that allows maintenance information to be stored securely in a PostgreSQL database.

The system provides:

- Digital maintenance records
- Instant maintenance history
- Work order tracking
- Technician accountability
- Centralized asset management

---

# Features

## Authentication

- Secure Login
- Django Authentication

---

## Dashboard

Displays:

- Total Employees
- Total Assets
- Open Work Orders
- Completed Work Orders
- Maintenance Logs

---

## Employee Management

- Add Employee
- Edit Employee
- Delete Employee
- View Employee

---

## Asset Management

- Register Assets
- Update Assets
- Delete Assets
- View Asset Details
- Asset Maintenance History

---

## Work Order Management

- Create Work Orders
- Automatic Work Order Number Generation
- Assign Employees
- Track Status
- Edit/Delete Work Orders

---

## Maintenance Logs

- Record Maintenance
- Update Maintenance Records
- Delete Maintenance Records
- View Maintenance History

---

## Asset Maintenance History

Each asset displays:

- Previous Work Orders
- Maintenance Logs
- Technicians
- Hours Worked
- Maintenance Dates

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Backend | Django |
| Language | Python 3 |
| Database | PostgreSQL |
| Frontend | HTML5 |
| CSS Framework | Bootstrap 5 |
| ORM | Django ORM |

---

# System Workflow

```
Employee
     │
     ▼
Asset
     │
     ▼
Work Order
     │
     ▼
Maintenance Log
     │
     ▼
Maintenance History
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/RailMaint.git
```

---

## 2. Navigate into the project

```bash
cd RailMaint
```

---

## 3. Create a virtual environment

Windows

```bash
python -m venv venv
```

Linux/macOS

```bash
python3 -m venv venv
```

---

## 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

Create a PostgreSQL database.

Example:

```
Database Name:
railmaint_db
```

Update your `settings.py` database configuration.

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railmaint_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

# Run Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts.

---

# Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

# Project Structure

```
RailMaint/

│
├── assets/
├── dashboard/
├── employees/
├── maintenance_logs/
├── workorders/
├── templates/
├── static/
├── media/
├── railmaint/
├── manage.py
└── requirements.txt
```

---

# Future Improvements

Planned features include:

- Spare Parts Inventory
- Preventive Maintenance Scheduling
- Email Notifications
- SMS Notifications
- QR Code Asset Identification
- Mobile Application
- Reports (PDF & Excel)
- REST API
- Role-Based Permissions
- Audit Logs
- Analytics Dashboard

---

# Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/new-feature
```

5. Create a Pull Request

---

# License

This project is released under the MIT License.

Feel free to use, modify and distribute it in accordance with the license terms.

---

# Developer

**Morgan Owanyi**

Diploma in Information Technology

Cybersecurity Enthusiast

Django Developer

Uganda

---

## Acknowledgements

This project was inspired by a real-world operational challenge observed during an internship at a railway company, where maintenance activities were recorded manually on paper. RailMaint was developed to demonstrate how software can improve maintenance management through digitization, centralized record keeping, and efficient workflow tracking.

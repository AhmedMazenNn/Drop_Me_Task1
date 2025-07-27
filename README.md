# 🧱 Project Workflow – RVM Rewards API Git Branching & Collaboration Guide

## 🚀 Overview

This project is part of **Drop Me’s Backend Internship Challenge** and represents a real-world component of our AI-powered Recycling Vending Machine (RVM) platform.

### ✅ Features
- Secure registration and login using JWT authentication.
- Submit recyclable deposits (type, weight, machine).
- Auto-calculation of reward points based on material type.
- View total weight and reward points.
- Admin panel access for managing data.

---

## 🧠 ERD (Entity Relationship Diagram)

[Click here to view the ERD diagram](https://drive.google.com/file/d/1WuNODUWEBhkcA9vdJRn7VEMFXnH0iuxN/view?usp=sharing)

---

## 📚 API Documentation

After running the server, view all API endpoints at:

👉 [`http://127.0.0.1:8000/api/docs/`](http://127.0.0.1:8000/api/docs/)

---

## 🗂 Branching Strategy

| Branch       | Purpose                                |
| ------------ | -------------------------------------- |
| `main`       | Stable, production-ready code          |
| `dev`        | Integration branch for tested features |
| `feature/*`  | New features                           |

---

## 📦 Required Software

- Python 3.11
- PostgreSQL 15
- Git

---

## 🚀 Getting Started (First Time Setup)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/AhmedMazenNn/Drop_Me_Task1.git
   cd Drop_Me_Task1
   ```
2. **Check remote info**:

   ```bash
   git remote -v
   ```

3. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies (if applicable)**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set environment variables**:

   ```bash
   DEBUG=True
   SECRET_KEY='your-secret-key-here'
   DATABASE_URL='postgres://your_db_user:your_db_password@localhost:5432/your_db_name'
   ```

6. run migrations :

   ```bash
   python manage.py migrate
   ```

7. run the server :

   ```bash
   python manage.py runserver
   ```

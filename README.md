# ♻️ RVM Deposit & Rewards API

This project is a secure, token-authenticated Django REST API that allows users to log recyclable material deposits and automatically earn reward points based on material type.

---

## 🚀 Overview

As part of Drop Me’s Backend Internship Challenge, this API reflects a real-world component of our AI-driven Recycling Vending Machine (RVM) platform. Users can:

- Register/login with secure token-based authentication.
- Submit recyclable material deposits with weight, type, and machine ID.
- Earn reward points automatically (based on material type).
- View their total recycled weight and accumulated reward points.

---

## 🏗️ Project Structure & Workflow

- The project uses a **modular app structure**, with at least two Django apps:
  - `users`: Handles registration, login, and authentication
  - `recycling`: Manages deposits and reward calculation

- ✅ **Branching Strategy**
  - `main`: Stable, production-ready code
  - `dev`: Integration and testing branch
  - `feature/<name>`: Feature development (e.g., `feature/deposit-endpoint`, `feature/swagger-setup`)

This separation ensures clean development → testing → production workflows.

---

## 📦 How to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/AhmedMazenNn/Drop_Me_Task1.git
cd core

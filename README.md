# 🚀 Nivara: Hyperlocal E-Commerce Platform

> A backend-focused, production-inspired system that solves real-world inventory visibility and reservation problems for nearby retail stores.

---

## 📌 Problem Statement

In real life, users often visit nearby stores only to discover that the desired product is **out of stock**. This leads to:

* Wasted time and effort
* Poor customer experience
* Lack of real-time visibility

---

## 💡 Solution

**Nivara** is a hyperlocal e-commerce backend system that enables users to:

* Browse products
* Check **store-wise real-time inventory**
* Compare pricing across stores
* **Reserve items before visiting**
* Avoid unnecessary store visits

---

## 🧠 Key Engineering Highlights

This is **NOT a CRUD project** — it focuses on real backend challenges:

### 🔐 Authentication & Security

* JWT-based authentication (SimpleJWT)
* Secure API access using `IsAuthenticated`
* User identity derived from token (no spoofing)

---

### ⚙️ Inventory System Design

* Inventory is **store-specific**, not global
* Each store has:

  * Different stock
  * Different pricing
* Clean relational modeling using Django ORM

---

### 🧮 Reservation Logic

* Prevents overbooking
* Validates stock before reservation
* Automatically reduces stock on success

---

### ⚡ Concurrency Handling (🔥 Important)

* Used `transaction.atomic`
* Used `select_for_update()` (row-level locking)
* Prevents **race conditions** in concurrent reservations

---

### 👥 Role-Based Access Control

* Users → view only their own reservations
* Store Owners → view reservations for their store
* Unauthorized access → blocked (403)

---

## 🏗️ Tech Stack

* **Backend**: Django, Django REST Framework
* **Database**: PostgreSQL
* **Authentication**: JWT (SimpleJWT)
* **ORM**: Django ORM

---

## 🧱 System Architecture

```text
Client (Postman / Frontend)
        ↓
DRF APIs (Views)
        ↓
Business Logic (Validation + Transactions)
        ↓
Django ORM
        ↓
PostgreSQL Database
```

---

## 🗂️ Core Models

### 👤 User

* Custom user model (`AbstractUser`)
* Role: `is_store_owner`

---

### 🏪 Store

* Linked to owner (User)
* Location-based (latitude, longitude)

---

### 📦 Product

* Global entity
* Shared across all stores

---

### 📊 Inventory (Core Entity)

* Store + Product mapping
* Stock
* Price
* Discount Price

---

### 🧾 Reservation

* User → Inventory
* Quantity
* Timestamp

---

## 🔗 API Endpoints

### 🔐 Authentication

* `POST /api/token/`
* `POST /api/token/refresh/`

---

### 📦 Products

* `GET /api/products/`

---

### 🏪 Stores

* `GET /api/stores/`

---

### 📊 Inventory

* `GET /api/inventory/<product_id>/`

---

### 🧾 Reservations

* `GET /api/reservations/` → current user
* `GET /api/reservations/?store_id=<id>` → store owner
* `POST /api/reservations/` → create reservation

---

## 🧪 Testing Strategy

Tested using:

* DRF Browsable API
* Postman

### Covered Cases:

* Valid reservation
* Insufficient stock
* Zero stock
* Concurrent reservation scenario (conceptually handled)

---

## 🚀 How to Run Locally

### 1. Clone repository

```bash
git clone https://github.com/oyeanmol/nivara-hyperlocal-ecommerce.git
cd nivara-hyperlocal-ecommerce
```

---

### 2. Setup virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup database (PostgreSQL)

Update `settings.py` with your DB credentials.

---

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create superuser

```bash
python manage.py createsuperuser
```

---

### 7. Run server

```bash
python manage.py runserver
```

---

## 📌 Design Decisions

* Used **monolithic architecture** for simplicity
* Focused on **backend engineering depth over UI**
* Designed APIs to be **frontend-agnostic**
* Used **database-level locking** for consistency

---

## 🎯 Why No Frontend?

The focus of this project was:

> **Backend system design, data consistency, and API architecture**

The system is fully ready to integrate with:

* React frontend
* Mobile apps
* Any REST client

---

## 🧠 Interview Talking Points

You can confidently say:

* Designed a **real-world inventory system**
* Solved **concurrent booking problem**
* Implemented **JWT authentication**
* Built **role-based access system**
* Ensured **data consistency at DB level**

---

## 📈 Future Improvements

* Pagination & filtering
* Search functionality
* Redis caching
* Async tasks (Celery)
* Full frontend integration

---

## 👨‍💻 Author

**Anmol Shah**
GitHub: https://github.com/oyeanmol

---

## ⭐ Final Note

This project reflects **backend engineering thinking**, not just coding.

> Focus: Correctness > Completeness > UI

---

🔥 If you liked this project, give it a star.

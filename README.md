# 🏫 School Management API — FastAPI & SQLAlchemy Architecture

A robust RESTful API built with Python and FastAPI for managing academic ecosystems, featuring relational database modeling, schema validations, and modular route architecture.

---

### 🚀 Technical Features & Architecture

- **Modular Architecture:** Clean separation of concerns with dedicated layers for Models, Schemas, Routers, and Database Config.
- **Data Validation & Serialization:** Request and response body validation using **Pydantic** schemas.
- **Relational ORM Mapping:** Database entities, constraints, and relationships mapped with **SQLAlchemy**.
- **RESTful Endpoints:** CRUD operations for students, courses, grades, and academic records.
- **Interactive API Documentation:** Auto-generated interactive OpenAPI/Swagger documentation.

---

### 🛠️ Tech Stack

- **Framework:** FastAPI
- **ORM & Database:** SQLAlchemy, SQLite / PostgreSQL
- **Data Validation:** Pydantic
- **Server:** Uvicorn

---

### 📂 Directory Structure

school-management-api/
├── app/
│   ├── database.py    # Database engine & session setup
│   ├── models.py      # SQLAlchemy ORM models
│   ├── schemas.py     # Pydantic data validation schemas
│   └── routers/       # API route handlers
├── main.py            # Application entry point
└── requirements.txt

---

### 💻 Local Execution

git clone https://github.com/brenowz/school-management-api.git
cd school-management-api

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload

---

### 👤 Author & Maintainer

**Breno Barros** — Backend & Software Engineering  
- **LinkedIn:** [linkedin.com/in/brenobarrosdev](https://linkedin.com/in/brenobarrosdev)  
- **GitHub:** [@brenowz](https://github.com/brenowz)

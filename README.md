# 📝 Smart ToDo API (JWT Protected + MongoDB)

A secure backend REST API for task management built using **FastAPI + MongoDB + JWT**.  
Users can sign up, log in, and manage personal tasks safely.

---

## 🚀 Features

| Feature | Status |
|--------|-------|
| User Signup & Login | ✅ |
| Password Hashing | 🔐 bcrypt |
| JWT Authentication | 🔥 |
| Create / Read / Update / Delete Tasks | 📝 |
| User-Specific Tasks Only | 🔒 Protected |
| Swagger API Docs | ✔ Available |
| MongoDB Integration | 🌿 |

---

## 🛠 Tech Stack

- **Python**
- **FastAPI**
- **MongoDB**
- **JWT Auth**
- **Uvicorn**
- **Pydantic**
- **Passlib**

---

## 📂 Project Structure

smart-todo-api/
├── main.py # Main API routes & JWT auth
├── auth.py # Password hashing + token generation
├── models.py # Pydantic models
├── database.py # MongoDB connection
├── requirements.txt # Required packages
└── README.md


---

## ⚙ Installation & Run

```bash
# Clone repository
git clone <repo-link>
cd smart-todo-api

# Install packages
pip install -r requirements.txt

# Run server
uvicorn main:app --reload

---

🔗 API Endpoints
Auth
Method	Endpoint	Description
POST	/signup	Register user
POST	/login	Login & get token
Tasks (Requires Authorization Bearer <token>)
Method	Endpoint	Description
POST	/tasks	Create task
GET	/tasks	View user tasks
PUT	/tasks/{task_id}	Update task
DELETE	/tasks/{task_id}	Delete task
🧪 Testing with Swagger UI

Open:

http://127.0.0.1:8000/docs


Login → copy token

Click Authorize → paste Bearer <token>

Use Tasks routes

Database Used

MongoDB Local / Atlas
Collections created automatically:

todo_db > users
todo_db > tasks

⭐ Project Completed Successfully!
Smart ToDo API by <Sibam Sen>
Submitted as part of Technical Assessment.

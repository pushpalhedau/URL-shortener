
# 🔗 Flask URL Shortener

A lightweight and functional URL Shortener built using **Flask** and **SQLite** — supporting anonymous URL shortening and logged-in user support for custom short URLs.

✅ No ORM used — all database operations use raw SQL.

🖥️ Built with: `Flask`, `SQLite`, `HTML`, and `CSS` (no JS frameworks like React/Angular).

---

## 📌 Features

- 🔓 **Anonymous URL shortening**
- 🔐 **User authentication system** (Register/Login/Logout)
- ✏️ **Custom short URLs** available for logged-in users
- 🗃️ **SQLite Database** used directly (no ORM or SQLAlchemy)
- 🧪 **Unit tests** written using Python's `unittest` module
- 💡 Minimalist UI using plain **HTML + CSS**

---

## 🛠️ Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Backend      | Python (Flask)     |
| Database     | SQLite (no ORM)    |
| Frontend     | HTML & CSS         |
| Authentication | Flask Sessions + Werkzeug Security |
| Testing      | Python `unittest`  |

---

## 📂 Project Structure
```Project Structure
url-shortener/ 
├── app.py # Main application entry 
├── db.py # DB connection + initialization 
├── test_app.py # Unit tests 
├── templates/ # HTML Templates 
│     ├── index.html 
│     └── login.html 
├── static/ 
│     └── style.css # Basic CSS 
├── view_db.py # To view Database records in terminal
├── requirements.txt # Python dependencies 
└── README.md # Project overview
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize the Database
```bash
python
>>> from db import init_db
>>> init_db()
>>> exit()
```

### 4. Run the Application
```bash
python app.py
```
Or using Flask CLI:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Visit http://localhost:5000 in your browser.

## 🔐 Authentication
- Users can Register and Login via /login.

- Session-based authentication using Flask sessions.

- Passwords are hashed using Werkzeug before storage.

- Logged-in users can generate custom short links.

## ✨ Functionality Overview

| Function       | Access        | Description                                                  |
|----------------|---------------|--------------------------------------------------------------|
| `/`            | Public        | Home page to submit URLs (with optional custom code if logged in) |
| `/login`       | Public        | Login + Registration form                                   |
| `/logout`      | Authenticated | Logout current user                                         |
| `/custom_code` | Public        | Redirect to original URL based on short code                |

## 🧪 Running Unit Tests
```bash 
python test_app.py
```
## Tests included:

- Homepage accessibility

- URL shortening logic

- Invalid short URL redirection

redirection

## 🛡️ Security Notes
- User passwords are hashed using Werkzeug’s generate_password_hash.

- SQL queries are parameterized — safe from SQL injection.

- Short codes are checked for duplication before insert.

## 📄 License
This project is for assignment evaluation and educational demonstration purposes.

## 👤 Author
Pushpal Hedau
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pushpal-hedau-04479124a/)

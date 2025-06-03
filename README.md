# EventUp

**EventUp** is a comprehensive event management service platform built with Django, HTML, CSS, and JavaScript. It allows users to create accounts, browse and order event packages, view reviews, and manage their event history. EventUp also provides an intuitive admin interface for managing items and packages.

---

## 🚀 Features

✅ **Customer Account Management**  
- Create an account, log in, and log out  
- Update profile information, including profile picture  
- View and manage current and past orders  

✅ **Event Packages & Items**  
- Browse a range of event decoration items and curated packages  
- Filter items by location and event date  
- Place orders and view order details  

✅ **Admin Interface**  
- Add/edit/remove event items and packages  
- Manage user orders and track order status  

✅ **Customer Reviews**  
- View customer reviews and ratings for items and packages  

✅ **Interactive UI**  
- Video support on item pages  
- Success messages for actions like login, logout, and order placement  

---

## 🛠️ Tech Stack

- **Backend:** Django Framework  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (development), supports migration to MySQL/PostgreSQL  
- **Version Control:** Git & GitHub  

---

## ⚙️ Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/EventUp.git
   cd EventUp
    ```

2. **Set up Virtual Environment**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3. **Install Dependencies**
  ```bash
  pip install -r requirements.txt
  ```
4. **Apply Migrations**
  ```bash
  python manage.py migrate
  ```
5. **Create Superuser (for admin access)**
  ```bash
  python manage.py createsuperuser
  ```

## 📂 Project Structure

```
EventUp-Event_Management_Service_Providing_Platform/
├── authentication/         # Authentication app
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── backends.py
│   ├── context_processors.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│           
├── Decoration/            # Decoration app
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── templatetags/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── built_in_func.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── EventUp/                # Main project directory
│   ├── __pycache__/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── asgi.py
│   ├── forms.py
│   ├── settings.py
│   ├── urls.py
│   ├── user_auth.py
│   ├── views.py
│   └── wsgi.py
│
├── media/                  # User-uploaded media files
├── client\profile_pictures
├── decorations
│   ├── items
│   └── packages
│
├── others/                 # Additional resources or scripts
├── venv/                   # Virtual environment
├── .gitattributes
├── .gitignore
├── build_files.sh
├── db.json
├── db.sqlite3
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```


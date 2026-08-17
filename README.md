# EventUp - Event Management & Decoration Service Platform

**EventUp** is a full-featured Django-based event management platform that connects event organizers with professional decoration service providers. The platform enables customers to browse curated decoration packages and individual items, filter by location and availability dates, place orders, and leave reviews—all through an intuitive, responsive web interface.

---

## 🚀 Key Features

### 👤 Customer Account Management
- **User Authentication:** Secure registration, login, and logout functionality
- **Profile Management:** Update personal information, upload profile pictures, and manage account settings
- **Location-based Services:** Store preferred districts, thanas (sub-districts), and delivery addresses
- **Order History:** Track current and past orders with complete order details and status

### 🎉 Decoration Packages & Items Catalog
- **Browse & Filter:** Explore event decoration items and curated packages
- **Smart Filtering:** Search by location, event date range, and product categories
- **Availability Management:** Real-time availability checking with date-range selection
- **Dynamic Pricing:** Support for individual items and bundled package pricing
- **Rich Media:** Images and videos for each item and package to showcase details

### 📅 Booking & Availability System
- **Date-Range Booking:** Select custom start and end dates for rental periods
- **Availability Tracking:** Automatic management of booked and available time slots
- **Booking Validation:** Prevents double-booking and ensures date integrity
- **Legacy Cleanup:** Automatic deletion of expired bookings

### ⭐ Customer Reviews & Ratings
- **Review System:** Customers can rate packages with detailed written reviews (1-5 stars)
- **Transparent Ratings:** Aggregated ratings displayed on package detail pages
- **Quality Assurance:** Helps maintain service quality standards

### 🛠️ Admin Dashboard
- **Full CRUD Operations:** Add, edit, update, and remove decoration items and packages
- **Category Management:** Organize products into categories for better browsing
- **Order Management:** View, track, and update customer order statuses
- **Inventory Control:** Manage quantities and availability for all products
- **User Management:** Monitor customer accounts and activity

### 🎨 User Interface Features
- **Responsive Design:** Optimized for desktop, tablet, and mobile devices
- **Interactive Elements:** Dynamic filtering, real-time search, and smooth navigation
- **Rich Media Support:** Image galleries and embedded video demonstrations
- **User Feedback:** Success messages for login, logout, order placement, and profile updates
- **Component Reusability:** Consistent header, footer, and back-button components

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Django 5.0.3 |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Database** | SQLite3 (Development), PostgreSQL/MySQL ready |
| **Image Storage** | FileField for media uploads (decorations, profile pictures) |
| **Authentication** | Django User Model with custom backends |
| **Deployment** | Heroku-ready (includes Procfile and runtime.txt) |
| **Version Control** | Git & GitHub |

---

## 📦 Requirements

Python 3.8+ with the following key dependencies:
- `Django 5.0.3` - Web framework
- `asgiref 3.8.1` - ASGI server implementation
- `dj-database-url` - Database configuration
- `Pillow` - Image processing
- `gunicorn` - Production WSGI server
- Additional dependencies listed in `requirements.txt`

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/EventUp.git
cd EventUp
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
```bash
python manage.py migrate
```

### 5. Create Admin Account (Superuser)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin credentials.

### 6. Collect Static Files (for production)
```bash
python manage.py collectstatic --noinput
```

### 7. Run Development Server
```bash
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000`

### 8. Access Admin Panel
Navigate to `http://127.0.0.1:8000/admin` with your superuser credentials.

---

## 📂 Project Structure

```
EventUp-Event_Management_Service_Providing_Platform/
│
├── 📁 authentication/              # User authentication app
│   ├── migrations/
│   ├── backends.py                 # Custom authentication backends
│   ├── context_processors.py       # Template context data
│   ├── models.py
│   ├── views.py                    # Auth views (login, logout, signup)
│   ├── admin.py
│   └── tests.py
│
├── 📁 Decoration/                  # Main decoration service app
│   ├── 📁 migrations/              # Database migrations
│   ├── 📁 static/
│   │   ├── 📁 css/                 # Styling sheets
│   │   │   ├── global.css          # Global styles
│   │   │   ├── decoration.css
│   │   │   ├── decoration_detail.css
│   │   │   ├── login.css
│   │   │   ├── signup.css
│   │   │   ├── profile.css
│   │   │   ├── order_view.css
│   │   │   └── ...
│   │   ├── 📁 js/                  # Client-side JavaScript
│   │   │   ├── decoration.js       # Main app logic
│   │   │   └── ...
│   │   └── 📁 img/                 # Static images
│   ├── 📁 templates/               # HTML templates
│   │   ├── decoration.html         # Main catalog page
│   │   ├── decoration_detail.html  # Individual item details
│   │   ├── 📁 components/          # Reusable components
│   │   │   ├── header.html
│   │   │   ├── footer.html
│   │   │   └── back_button.html
│   │   └── ...
│   ├── 📁 templatetags/            # Custom template filters
│   │   └── custom_filters.py
│   │
│   ├── models.py                   # Core data models:
│   │                               # - Customer, Product_Catagory
│   │                               # - Package, Item
│   │                               # - PackageBooked, ItemBooked
│   │                               # - Order_Info, Review, Profile
│   ├── views.py                    # Main application views
│   ├── urls.py                     # URL routing
│   ├── forms.py                    # Django forms
│   ├── signals.py                  # Django signals for model events
│   ├── built_in_func.py            # Utility functions
│   ├── admin.py                    # Admin interface configuration
│   └── tests.py
│
├── 📁 EventUp/                     # Project settings & configuration
│   ├── settings.py                 # Django configuration
│   ├── urls.py                     # Project-level URL routing
│   ├── wsgi.py                     # WSGI entry point
│   ├── asgi.py                     # ASGI entry point
│   ├── user_auth.py                # Custom authentication
│   ├── views.py                    # Project-level views
│   ├── forms.py                    # Project-level forms
│   ├── 📁 static/                  # Global static files
│   │   ├── package.json
│   │   ├── 📁 css/
│   │   ├── 📁 js/
│   │   └── 📁 img/
│   └── 📁 templates/               # Global templates
│       ├── 📁 Registrations/       # Auth templates
│       │   ├── login.html
│       │   └── signup.html
│       ├── profile.html
│       ├── edit_profile.html
│       ├── order_view.html
│       ├── order_confirmation.html
│       └── 📁 components/
│
├── 📁 media/                       # User-uploaded files
│   ├── 📁 client/
│   │   └── profile_pictures/       # User profile images
│   ├── 📁 decorations/
│   │   ├── items/                  # Item images
│   │   └── packages/               # Package images
│
├── 📁 staticfiles/                 # Collected static files (production)
│
├── 📁 .git/                        # Git version control
│
├── .gitattributes                  # Git attributes
├── .gitignore                      # Git ignore rules
├── Procfile                        # Heroku deployment configuration
├── runtime.txt                     # Python version specification
│
├── manage.py                       # Django management script
├── db.sqlite3                      # SQLite database
├── requirements.txt                # Python dependencies
│
├── LICENSE                         # Project license
├── README.md                       # This file
└── README copy.md                  # Backup documentation
```

---

## 🗄️ Database Models

### Core Models

| Model | Purpose |
|-------|---------|
| **Customer** | Legacy customer info (name, email, location) |
| **Product_Category** | Product categorization (weddings, birthdays, etc.) |
| **Package** | Bundled decoration services with pricing |
| **Item** | Individual decoration items available for rental |
| **Order_Info** | Customer orders with UUID tracking |
| **PackageBooked** | Availability slots for packages with date ranges |
| **ItemBooked** | Availability slots for items with date ranges |
| **Package_Detail** | Media files (images/videos) for packages and items |
| **Review** | Customer ratings and written reviews |
| **Profile** | Extended user profile with phone, location, picture |

---

## 🔐 Authentication & Security

- **Django Authentication:** Leverages Django's built-in User model
- **Custom Backends:** Custom authentication backends in `backends.py`
- **Session Management:** Cookie-based session tracking
- **CSRF Protection:** Built-in Django CSRF middleware
- **Profile Pictures:** Secure file upload handling with Pillow


---

## 📝 Usage Guide

### For Customers
1. **Sign Up:** Create a new account with email and password
2. **Browse:** Search for decorations by location and date
3. **Select:** Choose desired items/packages and check availability
4. **Order:** Complete the booking with delivery details
5. **Review:** Leave ratings and reviews after service completion

### For Administrators
1. **Login to Admin Panel:** `/admin` with superuser credentials
2. **Add Products:** Create categories, items, and packages
3. **Manage Inventory:** Update quantities and availability
4. **Review Orders:** Monitor and update order statuses
5. **Analytics:** View customer data and review trends

---

## 🔧 Development Tips

### Adding Custom Filters
Extend template tags in `Decoration/templatetags/custom_filters.py`:
```python
@register.filter
def your_custom_filter(value):
    return processed_value
```

### Extending Models
All core models support Django's ORM for easy extensions:
```python
from Decoration.models import Package
packages = Package.objects.filter(location='Dhaka').order_by('-price')
```

### Creating Admin Actions
Configure admin actions in `Decoration/admin.py` for bulk operations.

---

## 📞 Support & Contributions

- **Issues:** Report bugs and feature requests on GitHub Issues
- **Pull Requests:** Contributions welcome! Follow Django/PEP8 standards
- **Documentation:** Keep README and docstrings up to date

---

## 📄 License

This project is licensed under the [LICENSE](LICENSE) file included in the repository.

---

## 👨‍💻 Author & Version

**EventUp v1.9**  
A comprehensive event management and decoration service platform built with Django.

For questions or support, please open an issue on the repository.


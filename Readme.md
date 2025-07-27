# 🛒 Django Ecommerce Shopping Cart

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
</div>

<div align="center">
  <h3>🚀 A full-featured ecommerce web application built with Django</h3>
  <p>Complete shopping cart functionality with user authentication, payment integration, and order management</p>
</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🏗️ Project Structure](#️-project-structure)
- [⚙️ Installation](#️-installation)
- [🚀 Quick Start](#-quick-start)
- [🔧 Configuration](#-configuration)
- [📱 Usage](#-usage)
- [🔒 Authentication Features](#-authentication-features)
- [💳 Payment Integration](#-payment-integration)
- [📊 Models](#-models)
- [🎨 Frontend](#-frontend)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)

---

## ✨ Features

### 🛍️ **Core Ecommerce Features**
- **Product Catalog**: Browse products by categories and subcategories
- **Shopping Cart**: Add/remove products with dynamic cart management
- **Product Search**: Find products quickly and efficiently
- **Order Management**: Complete order processing workflow
- **Responsive Design**: Mobile-friendly interface

### 👤 **User Management**
- **User Registration**: Secure account creation with email verification
- **Login/Logout**: Authentication system with session management
- **Password Reset**: Secure password recovery via email
- **User Profiles**: Personalized user dashboard
- **Account Activation**: Email-based account verification

### 💰 **Payment & Checkout**
- **Paytm Integration**: Secure payment gateway integration
- **Order Tracking**: Real-time order status updates
- **Payment Status**: Success/failure handling
- **Invoice Generation**: Automated order confirmations

### 📧 **Communication**
- **Contact Form**: Customer inquiry system
- **Email Notifications**: Automated email alerts
- **Order Updates**: Real-time order status notifications

---

## 🏗️ Project Structure

```
ecommerce-shopping-cart/
├── ecommerce/                      # Main Django project
│   ├── manage.py                   # Django management script
│   ├── db.sqlite3                  # SQLite database
│   │
│   ├── ecommerce/                  # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py             # Django configurations
│   │   ├── urls.py                 # Main URL routing
│   │   ├── wsgi.py                 # WSGI configuration
│   │   └── asgi.py                 # ASGI configuration
│   │
│   ├── ecommerceapp/               # Main ecommerce application
│   │   ├── models.py               # Product, Order, Contact models
│   │   ├── views.py                # Business logic & controllers
│   │   ├── urls.py                 # App URL patterns
│   │   ├── admin.py                # Django admin configuration
│   │   ├── keys.py                 # Payment gateway keys
│   │   └── migrations/             # Database migrations
│   │
│   ├── authcart/                   # Authentication application
│   │   ├── models.py               # User-related models
│   │   ├── views.py                # Authentication views
│   │   ├── urls.py                 # Auth URL patterns
│   │   ├── utils.py                # Authentication utilities
│   │   └── migrations/             # Auth migrations
│   │
│   ├── PayTm/                      # Payment integration
│   │   └── Checksum.py             # Paytm checksum utilities
│   │
│   ├── templates/                  # HTML templates
│   │   ├── base.html               # Base template
│   │   ├── index.html              # Homepage
│   │   ├── login.html              # Login page
│   │   ├── signup.html             # Registration page
│   │   ├── checkout.html           # Checkout page
│   │   ├── profile.html            # User profile
│   │   ├── contact.html            # Contact form
│   │   ├── about.html              # About page
│   │   └── paytm.html              # Payment page
│   │
│   ├── static/                     # Static files
│   │   ├── assets/
│   │   │   ├── css/                # Stylesheets
│   │   │   ├── js/                 # JavaScript files
│   │   │   └── vendor/             # Third-party libraries
│   │   └── images/                 # Static images
│   │
│   └── media/                      # User uploads
│       └── images/                 # Product images
```

---

## ⚙️ Installation

### 📋 Prerequisites

- **Python 3.8+** installed on your system
- **pip** package manager
- **Git** for version control

### 🔽 Clone Repository

```bash
git clone https://github.com/Shivu384/ecommerce-shopping-cart.git
cd ecommerce-shopping-cart
```

### 🐍 Set up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 📦 Install Dependencies

```bash
pip install django
pip install Pillow  # For image handling
pip install pycryptodome  # For Paytm integration
```

---

## 🚀 Quick Start

### 1️⃣ **Navigate to Project Directory**
```bash
cd ecommerce
```

### 2️⃣ **Apply Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3️⃣ **Create Superuser (Optional)**
```bash
python manage.py createsuperuser
```

### 4️⃣ **Run Development Server**
```bash
python manage.py runserver
```

### 5️⃣ **Access the Application**
- **Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Authentication**: http://127.0.0.1:8000/auth/

---

## 🔧 Configuration

### 💳 **Payment Gateway Setup**

1. **Edit** `ecommerce/ecommerceapp/keys.py`:
```python
MID = "your_paytm_merchant_id"
MK = "your_paytm_merchant_key"
```

### 📧 **Email Configuration**

Update `ecommerce/ecommerce/settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

### 🔒 **Security Settings**

For production, update `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
SECRET_KEY = 'your-secret-key'
```

---

## 📱 Usage

### 🏠 **Homepage**
- Browse featured products
- Navigate by categories
- View product details

### 🛒 **Shopping Cart**
- Add products to cart
- Update quantities
- Remove items
- Proceed to checkout

### 👤 **User Account**
- Register new account
- Login/logout
- Reset password
- Activate account via email

### 💰 **Checkout Process**
1. Add items to cart
2. Proceed to checkout
3. Fill shipping details
4. Make payment via Paytm
5. Receive order confirmation

---

## 🔒 Authentication Features

### 📝 **User Registration**
- **Email Verification**: Account activation via email
- **Password Validation**: Secure password requirements
- **Duplicate Prevention**: Unique email validation

### 🔐 **Login System**
- **Session Management**: Secure user sessions
- **Remember Me**: Optional persistent login
- **Logout**: Secure session termination

### 🔄 **Password Recovery**
- **Email Reset**: Password reset via email
- **Token Security**: Time-limited reset tokens
- **New Password**: Secure password update

---

## 💳 Payment Integration

### 🏦 **Paytm Gateway**
- **Secure Transactions**: Encrypted payment processing
- **Multiple Payment Methods**: Cards, wallets, net banking
- **Real-time Status**: Instant payment verification
- **Checksum Validation**: Enhanced security

### 📊 **Order Tracking**
- **Order Creation**: Automatic order generation
- **Status Updates**: Real-time order tracking
- **Payment Status**: Success/failure handling
- **Order History**: Complete transaction records

---

## 📊 Models

### 🛍️ **Product Model**
```python
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images')
```

### 📦 **Orders Model**
```python
class Orders(models.Model):
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField()
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=200)
    # ... additional fields
```

### 📞 **Contact Model**
```python
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    phonenumber = models.IntegerField()
```

---

## 🎨 Frontend

### 🎨 **Design Framework**
- **Bootstrap 5**: Responsive grid system
- **Custom CSS**: Tailored styling
- **FontAwesome**: Icon library
- **JavaScript**: Interactive features

### 📱 **Responsive Design**
- **Mobile First**: Optimized for mobile devices
- **Tablet Support**: Perfect tablet experience
- **Desktop**: Full desktop functionality

### 🖼️ **Templates**
- **Base Template**: Consistent layout
- **Component Templates**: Reusable components
- **Form Templates**: User-friendly forms
- **Error Pages**: Custom error handling

---

## 🚀 Deployment

### 🌐 **Production Setup**

1. **Update Settings**:
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
```

2. **Static Files**:
```bash
python manage.py collectstatic
```

3. **Database Migration**:
```bash
python manage.py migrate
```

4. **Environment Variables**:
Set sensitive data as environment variables

---

## 🔧 Development

### 🛠️ **Adding New Features**

1. **Create App**:
```bash
python manage.py startapp newapp
```

2. **Add to Settings**:
```python
INSTALLED_APPS = [
    # ... existing apps
    'newapp',
]
```

3. **Create Models**:
```python
# newapp/models.py
class NewModel(models.Model):
    # model fields
```

4. **Run Migrations**:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧪 Testing

### 🔍 **Run Tests**
```bash
python manage.py test
```

### 📊 **Test Coverage**
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🔀 **Fork & Clone**
1. Fork the repository
2. Clone your fork
3. Create a feature branch

### 🎯 **Development Workflow**
1. **Create Branch**: `git checkout -b feature/new-feature`
2. **Make Changes**: Implement your feature
3. **Test**: Ensure all tests pass
4. **Commit**: `git commit -m "Add new feature"`
5. **Push**: `git push origin feature/new-feature`
6. **Pull Request**: Create a PR with description

### 📋 **Contribution Guidelines**
- Follow PEP 8 coding standards
- Write meaningful commit messages
- Add tests for new features
- Update documentation
- Respect existing code style

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Shivu384**
- GitHub: [@Shivu384](https://github.com/Shivu384)
- Repository: [ecommerce-shopping-cart](https://github.com/Shivu384/ecommerce-shopping-cart)

---

## 🙏 Acknowledgments

- **Django Community** for the amazing framework
- **Bootstrap Team** for the responsive CSS framework
- **Paytm** for payment gateway integration
- **Contributors** who helped improve this project

---

## 📞 Support

If you encounter any issues or have questions:

1. **Check Documentation**: Review this README thoroughly
2. **Search Issues**: Look through existing GitHub issues
3. **Create Issue**: Open a new issue with detailed description
4. **Contact**: Reach out via the contact form in the application

---

<div align="center">
  <h3>⭐ Star this repository if you found it helpful!</h3>
  <p>Made with ❤️ by <a href="https://github.com/Shivu384">Shivu384</a></p>
</div>

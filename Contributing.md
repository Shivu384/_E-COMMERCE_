# Contributing to Django Ecommerce Shopping Cart

Thank you for considering contributing to the **Django Ecommerce Shopping Cart** project!  
We value your ideas, time, and expertise in improving this application.  
This guide explains how to get started, make changes, and submit your contributions.

---

## 📜 Code of Conduct
Please note that this project follows a **Code of Conduct**.  
By participating, you agree to uphold a respectful, inclusive, and harassment-free environment for everyone.

---

## 🛠 Development Setup

Follow these steps to set up a local development environment:

1. **Fork the Repository**
   - Click the **Fork** button on the top right of this repository.

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/<your-username>/ecommerce-shopping-cart.git
   cd ecommerce-shopping-cart
3. **Create a Virtual Environment**
   ```bash
   python -m venv venv
  # Activate on Windows
  ```bash
  venv\Scripts\activate
  ```
  # Activate on macOS/Linux
  ```bash
  source venv/bin/activate
  ```
4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   
🌱 #  How to Contribute
    We welcome all kinds of contributions:
    
- 🐛 Bug Reports — Help us identify and fix issues.
- 💡 Feature Requests — Suggest new functionalities.
- 🎨 UI/UX Improvements — Enhance frontend and responsiveness.
- 🧪 Test Coverage — Add unit tests and integration tests.\
- 📄 Documentation — Improve or add project documentation.

🧪 # Testing
Before submitting a PR: Run the test suite:
```bash
python manage.py test
```

📤 # Submitting a Pull Request
1. **Push your branch to your fork:**
   ```bash
   git push origin feature/add-wishlist
   ```
   
2. Open a Pull Request (PR)
3. Provide a clear PR description:
- What problem does it solve?
- What changes were made?
- Any dependencies introduced?

💡# Tips for Contributors
 - Keep your changes small and focused.
 - Make sure all tests pass before submitting.

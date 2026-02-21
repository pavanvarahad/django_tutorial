# Django Authentication Guide

This guide provides a step-by-step walkthrough for implementing user authentication in Django, covering registration, login, session management, and logout.

## Table of Contents
1. [Create Django Project & App](#step-1-create-django-project--app)
2. [Configure Templates Folder](#step-2-configure-templates-folder)
3. [Create Register View](#step-3-create-register-view)
4. [Register HTML & Messages](#step-4-register-html--messages)
5. [Create Login View](#step-5-create-login-view-authentication--session)
6. [Login HTML](#step-6-login-html)
7. [Dashboard & Access Control](#step-7-dashboard-only-for-logged-in-users)
8. [Logout View](#step-8-logout-view)
9. [URLs Setup](#step-9-urls-setup)
10. [Session Mechanism](#how-session-works-in-django)
11. [Important Settings](#important-settings)

---

## Step 1: Create Django Project & App

First, initialize your project and create a dedicated app for authentication.

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp accounts
```

Add the app to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'accounts',
]
```

---

## Step 2: Configure Templates Folder

Ensure Django knows where to look for your HTML files. In `settings.py`, update the `TEMPLATES` list:

```python
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
```

Create the following directory structure:

```
myproject/
    templates/
        register.html
        login.html
        dashboard.html
```

---

## Step 3: Create Register View

The registration view handles both showing the form (GET) and processing the data (POST). We use `User.objects.create_user()` because it automatically handles password hashing.

### accounts/views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Basic check for existing users
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        # create_user hashes the password automatically
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'register.html')
```

---

## Step 4: Register HTML & Messages

To see the error or success messages defined in your views, you must include a message loop in your template.

### templates/register.html

```html
<!DOCTYPE html>
<html>
<body>
    <h2>Register</h2>

    {% if messages %}
        {% for message in messages %}
            <p style="color: red;">{{ message }}</p>
        {% endfor %}
    {% endif %}

    <form method="POST">
        {% csrf_token %}
        <input type="text" name="username" placeholder="Username" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>
    <p>Already have an account? <a href="{% url 'login' %}">Login here</a></p>
</body>
</html>
```

---

## Step 5: Create Login View (Authentication + Session)

Login involves two steps: `authenticate()` (checking if credentials are correct) and `login()` (creating the browser session).

### accounts/views.py

```python
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Verifies credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   # This starts the session
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')
```

---

## Step 6: Login HTML

### templates/login.html

```html
<!DOCTYPE html>
<html>
<body>
    <h2>Login</h2>

    {% if messages %}
        {% for message in messages %}
            <p style="color: red;">{{ message }}</p>
        {% endfor %}
    {% endif %}

    <form method="POST">
        {% csrf_token %}
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
</body>
</html>
```

---

## Step 7: Dashboard (Only for Logged-in Users)

The `@login_required` decorator ensures that only authenticated users can access this view. If an unauthenticated user tries to visit this page, they will be redirected to the login page.

### accounts/views.py

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    # request.user is automatically populated by Django
    return render(request, 'dashboard.html')
```

### templates/dashboard.html

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Welcome, {{ user.username }}!</h1>
    <p>You are now logged into your dashboard.</p>
    <a href="{% url 'logout' %}">Logout</a>
</body>
</html>
```

---

## Step 8: Logout View

### accounts/views.py

```python
def logout_view(request):
    logout(request) # Clears the session data
    return redirect('login')
```

---

## Step 9: URLs Setup

### accounts/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
```

### myproject/urls.py

```python
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')), # Includes all routes from accounts app
]
```

---

## How Session Works in Django

When you call `login(request, user)`, Django performs several actions behind the scenes:

1.  **Session Generation**: Creates a unique session ID.
2.  **Storage**: Saves the session data (linked to the user ID) in the `django_session` table in your database.
3.  **Cookie**: Sends a cookie named `sessionid` to the user's browser.
4.  **Middleware**: On subsequent requests, the `AuthenticationMiddleware` reads this cookie, looks up the session, and attaches the user object to `request.user`.

This allows you to check `request.user.is_authenticated` anywhere in your project.

---

## Important Settings

In `settings.py`, you should define these constants to control redirection behavior:

```python
# The URL where @login_required redirects unauthenticated users
LOGIN_URL = 'login'

# Where to go after a successful login (if no 'next' parameter is provided)
LOGIN_REDIRECT_URL = 'dashboard'

# Where to go after logging out
LOGOUT_REDIRECT_URL = 'login'
```

---

## Security Best Practices

1.  **Password Hashing**: Never store passwords as plain text. Always use `create_user` or `set_password()`, which use PBKDF2 by default.
2.  **CSRF Protection**: Always include `{% csrf_token %}` inside every POST form.
3.  **Secure Cookies**: In production, set `SESSION_COOKIE_SECURE = True` so cookies are only sent over HTTPS.
4.  **Built-in Views**: While custom views are good for learning, Django provides `django.contrib.auth.views` which handle edge cases and security patterns automatically.

---

## Execution

After writing your code, run the migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/register/` to test your implementation.

# Jinja2 Template Engine

Jinja2 is a powerful templating engine for Python, widely used for generating dynamic content in web applications. This document provides an overview of Jinja2, its features, and examples of usage.

---

## 1. **Introduction**
- Jinja2 is a template engine designed to work with Python applications.
- It allows dynamic rendering of HTML pages by embedding Python code within templates.

---

## 2. **Key Features**
- **Template Inheritance**: Enables the reuse of common structures across multiple templates.
- **Filters**: Allows transformation of data before rendering.
- **Loops and Conditionals**: Provides control flow mechanisms like loops (`for`) and conditionals (`if`).
- **Macros**: Supports reusable blocks of code similar to functions.
- **Escaping**: Protects against XSS attacks by auto-escaping data.

---

## 3. **Template Syntax**

### **Variables**
```html
<p>Hello, {{ user.name }}!</p>
```
- `{{ ... }}` is used to output variables.

### **Conditionals**
```html
{% if user.is_admin %}
  <p>Welcome, Admin!</p>
{% else %}
  <p>Welcome, User!</p>
{% endif %}
```

### **Loops**
```html
<ul>
{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
```

### **Filters**
```html
<p>{{ name|upper }}</p>
```
- Filters are applied using the `|` symbol, transforming values before rendering.

---

## 4. **Template Inheritance**

### **Base Template (base.html)**
```html
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
  <header>
    {% block header %}<h1>Header</h1>{% endblock %}
  </header>
  <main>
    {% block content %}{% endblock %}
  </main>
</body>
</html>
```

### **Child Template (index.html)**
```html
{% extends 'base.html' %}

{% block title %}Home Page{% endblock %}

{% block content %}
<p>Welcome to the Home Page!</p>
{% endblock %}
```

---

## 5. **Common Filters**
- `length`: Returns the length of a list or string.
- `lower`: Converts text to lowercase.
- `upper`: Converts text to uppercase.
- `default`: Provides a fallback value if a variable is undefined.
- `join`: Joins a list into a string.

Example:
```html
<p>{{ ['apple', 'banana', 'cherry']|join(', ') }}</p>
```

---

## 6. **Installation**
```bash
pip install jinja2
```

---

## 7. **Integration with Python**
```python
from jinja2 import Environment, FileSystemLoader

# Set up template environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')

# Render template with data
data = {'user': {'name': 'John'}}
output = template.render(data)
print(output)
```

---

## Final Notes
Jinja2 simplifies dynamic HTML rendering and integrates seamlessly with Python frameworks like Flask and FastAPI. For additional examples and advanced usage, refer to the [Jinja2 Documentation](https://jinja.palletsprojects.com/).


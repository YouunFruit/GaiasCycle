# Installation Guide

This guide provides a step-by-step process to set up the Gaia Cycle web application locally. Follow the instructions below to ensure a smooth installation.

---

## 1. **Clone the Repository**
Use Git to clone the project repository. Run the following command in your terminal or command prompt:

```bash
git clone <repository-url>
```
Replace `<repository-url>` with the actual URL of the repository.

---

## 2. **Navigate to the Project Directory**
Move into the cloned repository folder:

```bash
cd GaiasCycle
```

---

## 3. **Install Dependencies**
Install all required dependencies listed in `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

---

## 4. **Set Up Environment Variables**
1. Create a `.env` file in the root directory.
2. Add the required environment variables, such as database credentials and API keys:

```
DATABASE_URL=mysql://user:password@localhost/dbname
SECRET_KEY=your_secret_key
API_KEY=your_api_key
```

Replace the placeholders with actual values specific to your setup.

---

## 5. **Initialize the Database**
Run database migrations to set up tables and schema:

```bash
python manage.py migrate
```

---

## 6. **Run the Application**
Start the development server:

```bash
python manage.py runserver
```

Access the application in your browser at:
```
http://localhost:8000
```

---

## 7. **Verify Setup**
- Confirm that all dependencies are installed and the server is running without errors.
- Navigate through the application to test the features.

---

## Troubleshooting
If you encounter errors during installation:
- Verify dependencies using:
```bash
pip freeze
```
- Check logs for specific error messages.
- Ensure database configurations are correct.

---

## Final Notes
This installation guide covers the basic setup steps for Gaia Cycle. For additional support, refer to the [GitHub repository](https://github.com/MarieBelle88/GaiasCycle).


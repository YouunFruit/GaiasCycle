# Running the Application

<!-- 
Include:
1. Steps to run the app locally.
2. Commands to start the frontend and backend servers.
3. Using tools like Docker to simplify the process.
4. Testing the app to ensure it’s running properly.
-->

Follow these steps to run the web application and its documentation locally.

---

## 1. Set Up a Virtual Environment
To isolate the project dependencies, create and activate a virtual environment.


### Create the Virtual Environment
Run the following command :
```bash
python3 -m venv <environment-name>
```

### Activate the Virtual Environment
#### On Mac/Linux:
```bash
source <environment-name>/bin/activate
```
### On Windows:
```bash
<environment-name>\Scripts\Activate.ps1
```
You’ll know the virtual environment is active when its name appears at the beginning of your terminal prompt.

## 2. Install Dependencies
   Dependencies for the project are listed in the requirements.txt file.

### Run this command to install them:

```bash
pip install -r requirements.txt
```

### Key Dependencies:
-  **fastapi**: For the web framework.
- **jinja2**: For HTML templating.
-  **uvicorn**: For running the FastAPI application.
-  **mkdocs-material**: For building and serving the documentation.

#### Ensure the virtual environment is active before running the above command.

## 3. Run the Web Application
   Navigate to the app directory, then use Uvicorn to start the server:

```bash
cd app
```

```bash
uvicorn main:app --reload
```
The application will be accessible at:

```bash
http://127.0.0.1:8000
```

## 4. Run the Documentation
   To view the MkDocs-based documentation locally, use the following steps:

Ensure the virtual environment is activated.
Start the MkDocs server:
```bash
mkdocs serve --dev-addr 127.0.0.1:5000
```
Access the documentation in your browser at:

```bash
http://127.0.0.1:5000
```
By following these steps, you can run both the application and its documentation locally for development and testing purposes.


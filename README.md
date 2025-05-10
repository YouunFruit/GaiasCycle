(Forked here for easy access)

# To activate
### Open Terminal
- ## For Mac
- source (enviroment name)/bin/activate
- - cd app
- uvicorn main:app --reload
- ## For Windows
venv\Scripts\activate.bat
 or
venv\Scripts\Activate.ps1
- cd app
- uvicorn main:app --reload


# Installing Dependancies
Make sure you install within your virtual environment 

- Directory Gaiacycle
- pip install -r requirements.txt

# mkdocs activation
- activate v. env
- mkdocs serve --dev-addr 127.0.0.1:5000

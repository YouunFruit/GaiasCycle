# Setup

To setup and run our web app locally, follow this guide.


**Clone the Github**
    
    insert code for cloning github

### Setup Virtual Environment

---

**Create the virtual Environment**

 *For Mac and windows*


    python3 venv (environment name)




**Activate it**


*For Mac*


    source (enviroment name)/bin/activate

*For Windows*

    venv\Scripts\Activate.ps1



-  uvicorn main:app --reload

Activates it

    


`code`

## Installing Dependencies

All the required dependencies are listed in *requirements.txt*. 

    fastapi
    jinja2
    uvicorn
    mkdocs-material
*Explanation of Dependencies found in build*

Make sure you are in your venv before running this code and installing:

    pip install -r requirements.txt


## Server Activation
Using Uvicorn, we are able to create a template based website. 

Activate uvicorn using the following.Make sure you run this in the *app* directory

    uvicorn main:app --reload



## mkdocs activation
- activate v. env
- mkdocs serve --dev-addr 127.0.0.1:5000 

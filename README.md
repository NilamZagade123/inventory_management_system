______________________________________________________________________________________________________

DESCRIPTION:
Inventory Management System
______________________________________________________________________________________________________

SETUP:

1. install Python -3
2. clone the repository:
3. Create Virtual environment

    python3 -m pip install --user virtualenv
    create virtual environment : 
    virtualenv venv

4. Activate virtual environment : 
    source venv/bin/activate

5. For installing packeges run below command:
        pip install -r requirement.txt


6. Database
    We are using default database Sqlite3
    After creating  model, we need to run two commands in order to create Database for the same. 
    creating new migrations based on the changes you have made to your models.
    
       python manage.py makemigrations 
       python manage.py migrate

7. Command for create super user
    python manage.py createsuperuser

8. Command for run project
    python manage.py runserver
    admin console
    http://127.0.0.1:8000/admin/

9. for checking unit test cases run below command
    python manage.py test

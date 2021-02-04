1. To run this application, open it in terminal or CMD, and type '  python manage.py runserver  '  . e.g 

            terminal$   cd FREELIFE
            
            ~FREELIFE$   ls
            
            ~FREELIFEl$   accounts    day     db.sqlite3    FREELIFE    mainapp     manage.py     README.txt      templates
            
            ~FREELIFE$   python manage.py runserver


2. In case you make changes to the database, you have to make the migrations in order to solidify the changes. e.g:

           ~FREELIFE$   python manage.py makemigrations
           
           ~FREELIFE$   python manage.py migrate
           
           ~FREELIFE$   python manage.py runserver

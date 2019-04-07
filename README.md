- Go to the desired folder

- open cmd or terminal.

- setup virtual directory using command <python3 -m venv /path/to/new/virtual/environment>

- Unzip the "FortinetBackend" folder(contains Backend part of Application in Django ).

- copy "WorldBhojanalaya" folder and "requirements.txt" and paste it next to virtualDirectory made.

- Set up Database:

  - Open mysql workbench.
  - make mysql connection with following credentials:
  - Hostname: 127.0.0.1
  - Port: 3306
  - Username: root
  - Password: Set any desired Password

  - create a schema with a name "Bhojanalayas"

* activate virtual Environment using command : <source venv/bin/activate> in terminal or <C:\Users\suryav> \venv\Scripts\activate> in cmd  
  (reference :https://docs.python-guide.org/dev/virtualenvs/)

* pip install -r requirements.txt -- to install all python packages needed

* open "WorldBhojanalaya/WorldBhojanalaya/settings.py" and in 79th line set Password which was set during DB setup for Mysql connection.

* traverse upto "WorldBhojanalaya/" folder in terminal or in cmd
* Run following commands:
  - <python manage.py makemigrations>
  - <python manage.py makemigrations bhojanalayas>
  - <python manage.py migrate>
  - <python manage.py moveCSVToDb > -- for dumping into DB from CSV which is located locally in FortinetBackend folder.
  - <python manage.py runserver> -- for actiavting server

NOTE: dbScripts is submitted in separate folder named as "dbScripts" as well as located in "WorldBhojanalaya/WorldBhojanalaya/bhojanalayas/management/commands/moveCSVToDb.py"

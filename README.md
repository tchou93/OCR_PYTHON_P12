# Project P12

## Steps to install the environment:
```
* Clone the project from github:
$ git clone https://github.com/tchou93/OCR_PYTHON_P12.git

* Install the last version of python
https://www.python.org/downloads/

* Use a virtual environment
$ python -m venv env
$ source env/Scripts/activate

* Install some specific packets on this virtual environment
$ pip install -r requirements.txt
```

## Documentation of the API (in french):
```
For management team:
https://documenter.getpostman.com/view/23071143/2s8YeuMBqh

For commercial and support  teams:
https://documenter.getpostman.com/view/23071143/2s8YevnUfH
```

# Autorization for each teams:
OK = It is possible 
KO = It is not possible 
OKA = It is possible with autorization

## Management team
| Object | Create | Retrieve | Update | Destroy |
| --- | --- | --- | --- | --- |
| User | OK | OK | OK | OK |
| Client | OK | OK | OK | OK |
| Contract | OK | OK | OK | OK |
| Event | OK | OK | OK | OK |

## Sale team
| Object | Create | Retrieve | Update | Destroy |
| --- | --- | --- | --- | --- |
| User | KO | KO | KO | KO |
| Client | OK | OKA | OKA | KO |
| Contract | OK | OKA | OKA | KO |
| Event | KO | KO | KO | KO |

## Support team
| Object | Create | Retrieve | Update | Destroy |
| --- | --- | --- | --- | --- |
| User | KO | KO | KO | KO |
| Client | KO | OKA| KO | KO |
| Contract | KO | KO | KO | KO |
| Event | KO | OKA | OKA | KO |

## More informations about how to test the API:
```
* Use pgAdmin to import a database
1) Install pgAdmin from https://www.pgadmin.org/download/
2) Create a new database
3) Click right on the database then restore the backup : api_tests/database/db_epicevents_for_testing
* Use postman to run some integration tests
1) Install postman from https://www.postman.com/downloads/
2) Create new project, then import:
- api_tests/postman/LOCAL TEST ENV.postman_environment.json
- api_tests/postman/INTEGRATION TESTS.postman_collection.json
3) Run the server from the project root
$ cd src
$ python manage.py runserver
4) Run the collections on postman and check the results
```

## Informations about the database using for tests:
```
| Admin |
username: "admin",
password: "admin123"

| SALES1 |
username: user_test_sales1
password: user_sales1!!!

| SALES2 |
username: user_test_sales2
password: user_sales2!!!

| SUPPORT1 |
username: user_test_support1
password: user_support1!!!

| SUPPORT2 |
username: user_test_support1
password: user_support1!!!
```

## Complementary informations about how to configure postgresql database:
```
* Install PostgreSQL:
https://www.postgresql.org/download/

* Use the admin account to connect to the database then enter those command lines:
psql -U postgres
CREATE DATABASE <project_name>;
CREATE USER <user_name> WITH PASSWORD '<password>';
ALTER ROLE <user_name> SET client_encoding TO 'utf8';
ALTER ROLE <user_name> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <user_name> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <project_name> TO <user_name>;
ALTER USER <user_name> CREATEDB;

* Modify the setting file "setting.py" on django project :
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<project_name>',
        'USER': '<user_name>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


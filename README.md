# helpo [![CircleCI](https://circleci.com/gh/Jumpi96/helpo.png?circle-token=:circle-token)](https://circleci.com/gh/Jumpi96/helpo.png?circle-token=:circle-token) [![Coverage](https://codecov.io/gh/jumpi96/helpo/branch/master/graph/badge.svg)](https://codecov.io/gh/jumpi96/helpo/branch/master/graph/badge.svg)

> Proyecto Final - UTN FRC - 2018

Created with [Django React Boilerplate](https://github.com/vintasoftware/django-react-boilerplate).

## Conventions
### Coding
- To be defined
### Documenting
- English or spanish accepted

## Running
### Prerequisites
- Python 3.6.5: Full install, select "Add to PATH", for all users, including debugging binaries (select all options).
- NodeJS and NPM LTS 8.11.1
- Docker and latest pgAdmin if you have W10 Pro, MacOS or Linux:
```
docker pull postgres:latest
docker run -d -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres --name db-helpo -p 5432:5432 --restart=always postgres
```
  - PostgreSQL 10.3.2 otherwise: Full install, select all options, password=postgres, port=5432, next.
- Run CMD as Administrator and:
```
python -m pip install --upgrade pip
pip install pipenv
```
### Setup
- On pgAdmin, open Servers, PostgreSQL 10, right click on Databases and create db with name: `db-helpo`
- On project folder `helpo-api/`:
  - Create file with name `.env` and text `DJANGO_SETTINGS_MODULE="helpo.settings.local"`
- Run on `helpo-api/`: 
```
pipenv install --dev
pipenv shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
- Run on `helpo-web/`: 
```
npm update
npm update --save
npm install
npm run start
```




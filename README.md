# SimpleATMApiService

## Introduction

Developed with leveraging Python, Django Rest Framework and sqlite technologies.

### Aim of the project
Simple ATM API service to withdraw specified amount of cash with as small as possible numbers of paper money.
Let's say ATM has 200, 100, 50, 20, 10, 5, and 1 units for azn currency and 70AZN needed to be withdrawn, so ATM service will produce
(50, 20) which is 2 paper money that is the minimum amount of paper.

## Steps to run the project with docker
1) Clone the project
```bash
git clone <this project link>
```

2) Build the project on the top of docker 
```bash
docker-compose up --build
```

3) Update database tables
```bash
docker-compose exec web python manage.py migrate
```

4) Go to the link: http://localhost:8000

5) For swagger ui go to the link: http://localhost:8000/swagger

## Steps to run project without docker
1) Clone the project
```bash
git clone <this project link>
```

2) Create virtual environment
```bash
python -m venv .venv
```

3) Install project libraries
```bash
python -m pip install -r requirements.txt
```

4) enter into src folder and run the server
```bash
python manage.py runserver
```

5) Finally you can checkout the endpoints on link:  http://localhost:8000





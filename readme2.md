In order to Run this API in development mode, one should:

- Create a Virtual Environment with Python with:
    `python -m virtualenv venv` (Windows)
- Activate the Virtual Environment:
    `.\venv\Scripts\activate` (Windows)
- Install the requirements:
    `pip intall -r requirements.txt`
- Run Docker Compose:
    `docker-compose up`

- Create a .env file in the root folder with the following parameters:
    
    SECRET_KEY=s)qw=n4p&pa(&2)qi*01o&_@di*ap(hsnf!7r3nwgs5!s-af%z
    ENGINE=django.db.backends.postgresql
    NAME=challenge
    USER=postgres
    PASSWORD=challenge
    HOST=db
    PORT=5432

- Create a superuser by running 
    `docker exec -it container_id python manage.py createsuperuser`
    - To know your container_id, run docker ps and find the django-challenge-001_web id.

- Now you are free to test the api with the postman collection located on this repository root.





In order to Run this API in production mode, do it instead:





    
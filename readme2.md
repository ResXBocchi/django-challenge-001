In order to Run this API in development mode, one should:

- Create a .env file in the root folder with the following parameters:
    
    SECRET_KEY=s)qw=n4p&pa(&2)qi*01o&_@di*ap(hsnf!7r3nwgs5!s-af%z
    ENGINE=django.db.backends.postgresql
    NAME=challenge
    USER=postgres
    PASSWORD=challenge
    HOST=db
    PORT=5432

- Run Docker Compose:
    `docker-compose up`

- Create a superuser by running 
    `docker exec -it container_id python manage.py createsuperuser`
    - To know your container_id, run docker ps and find the django-challenge-001_web id.

- Now you are free to test the api with the postman collection located on this repository root.
- In order to do it the following sequence is advised:

- 1 - collection/authentication/POST LOGIN REQUEST - with the created admin credentials
in order to get the token.

- 2 - collection/api/admin/authors/ADMIN POST REQUEST - input the data on the form-data tab
and the token on the authorization header

- 3 - collection/api/admin/articles/ADMIN POST REQUEST - input the data on the raw tab on JSON format,
and use the id of the created author as the author parameter

- 4 - collection/authentication/SIGN UP POST REQUEST - then you provide the fields especified in the body tab,
and get your authenticated user key

- 5 - collection/authentication/RESET PASSWORD POST REQUEST - insert your email as provided on the sign up post request,
then, in the terminal which is running docker, you will receive the link to choose a new password.

- 6 - collection/authentication/RESET PASSWORD CONFIRMATION POST REQUEST - the link provided in the previous step
looks like this:
    `http://example.com/reset/Mg/ajlty4-fa838f82f991a9475f8438977643a16e/`
      
     it consists on http://exemple.com/reset/UID/TOKEN/

     Provide this values on the postman raw body tab and the new password, and you password will be reseted.

- 7 - collection/authentication/AUTH CHANGE PASSWORD POST REQUEST - provide your authentication token on the headers tab
and the specified fields on the raw body data.

Now you can play around with the remaining requests. All fields are provided in the collection requests.





In order to Run this API in production mode, do it instead:





    
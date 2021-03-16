## Prerequisites

- [Python 3](https://www.python.org)
- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- [Git](https://git-scm.com/)


- Create a .env file in the root folder with the following parameters:
```  
    SECRET_KEY=s)qw=n4p&pa(&2)qi*01o&_@di*ap(hsnf!7r3nwgs5!s-af%z
    ENGINE=django.db.backends.postgresql
    NAME=challenge
    USER=postgres
    PASSWORD=challenge
    HOST=db
    PORT=5432
```
In order to Run this API in development mode, one should:

- Run Docker Compose:
    `docker-compose up`

- Create a superuser by running 
    `python manage.py createsuperuser`

- Now you are free to test the api with the postman collection located on this repository root.

- In order to do it the following start sequence is advised:

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

*************************************************************************************************************************

In order to Run this API in production mode, do it instead:

- Set DEBUG = False in the .env file

- Add the server domain to the ALLOWED_HOSTS parameter in the settings.py file

- Run Docker Compose:
    `docker-compose -f docker-compose.prod.yml up`

- Create a superuser by running 
    `docker exec -it container_id python manage.py createsuperuser`
    - To know your container_id, run docker ps and find the django-challenge-001_web id.


**************************************************************************************************************************

# Jungle Devs - Django Challenge #001

## Description

**Challenge goal**: The purpose of this challenge is to give an overall understanding of a backend application. You’ll be implementing a simplified version of a news provider API. The concepts that you’re going to apply are:

- REST architecture;
- Authentication and permissions;
- Data modeling and migrations;
- PostgreSQL database;
- Query optimization;
- Serialization;
- Production builds (using Docker).

**Target level**: This is an all around challenge that cover both juniors and experience devs based on the depth of how the concepts were applied.

**Final accomplishment**: By the end of this challenge you’ll have a production ready API.

## Acceptance criteria

- Clear instructions on how to run the application in development mode
- Clear instructions on how to run the application in a Docker container for production
- A good API documentation or collection
- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- Administrator restricted APIs:
  - CRUD `/api/admin/authors/`
  - CRUD `/api/admin/articles/`
- List article endpoint `/api/articles/?category=:slug` with the following response:
```json
[
  {
    "id": "39df53da-542a-3518-9c19-3568e21644fe",
    "author": {
      "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
      "name": "Author Name",
      "picture": "https://picture.url"
    },
    "category": "Category",
    "title": "Article title",
    "summary": "This is a summary of the article"
  },
  ...
]
```
- Article detail endpoint `/api/articles/:id/` with different responses for anonymous and logged users:

    **Anonymous**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>"
    }
    ```

    **Logged user**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>",
      "body": "<div><p>Second paragraph</p><p>Third paragraph</p></div>"
    }
    ```

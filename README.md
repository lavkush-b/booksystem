# booksystem

## Introduction

This is a Django app. it's contained a simple CRUD (Create, Read, Update, Delete) API with a local database. There is a
end point Which is used to get books data using external API. The external API that will be used here is the Ice And
Fire API.

### App deployed on heroku

This app deployed on heroku on https://vast-plateau-62808.herokuapp.com/ (Only backend service, No UI)
We can access api using mention base url from remote server. Please find the 
end points below.


### Setup for running on local machine
 0. Install postgres in your local and create a database. Once database is created set environment variables mentioned below.
        ```textmate
        export PG_DB_USER=<db user|Example = 'postgres'>
        export PG_DB_NAME=<db name|Example = 'kush'>
        export PG_DB_PASS=<db password|Example = 'kush'>
        export PG_DB_HOST=<db host|Example = 'localhost'>
        export PG_DB_PORT=<db port|Example = '5432'>
        ```
 1. Create a virtual environment and activate environment. (for help you can check this link: https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/)
 2. Clone repository in local machine from given url https://github.com/lavkush-b/booksystem/tree/master
 3. Navigate to `booksystem` folder using `cd` command.
 4. Checkout on `master` branch using `git checkout master` command.
 5. Run command `pip install requirements.txt`
 6. For running test cases on local we have to run command  `python manage.py test`
 7. Starting server run command `python manage.py runserver`.

After completing successful these steps we are ready to hit `end points` using 
base url `http://localhost:8000`. End points listed below

### End point details

1. GET `http://localhost:8080/api/external-books?name=:nameOfABook`
is requested, application querying the Ice And Fire API and use the data received to respond with precisely the following JSON if there are results:
```json
{
"status_code": 200,
"status": "success",
"data": [
        {
"name": "A Game of Thrones",
"isbn": "978-0553103540",
"authors": [
"George R. R. Martin"
            ],
"number_of_pages": 694,
"publisher": "Bantam Books",
"country": "United States",
"release_date": "1996-08-01"
        },
        {
"name": "A Clash of Kings",
"isbn": "978-0553108033",
"authors": [
"George R. R. Martin"
            ],
"number_of_pages": 768,
"publisher": "Bantam Books",
"country": "United States",
"release_date": "1999-02-02"
        }
    ]
}
```
where :nameOfABook is a variable. Example value for :nameOfABook can be A Game Of Thrones.

2. Create : POST call `http://localhost:8080/api/v1/books`
is requested with the following data:
```textmate 
• name
• isbn
• authors
• country
• number_of_pages
• publisher
• release_date
```
Response looks like:
```json
{
"status_code": 201,
"status": "success",
"data": [
        { "book": {
                    "name": "My First Book",
                    "isbn": "123-3213243567",
                    "authors": [
                    "John Doe"
                                ],
                    "number_of_pages": 350,
                    "publisher": "Acme Books",
                    "country": "United States",
                    "release_date": "2019-08-01"
                    }
        }
    ]
}
```

3. Reading : GET `http://localhost:8080/api/v1/books`
Following response pattern should be getting:
```json
{
"status_code": 200,
"status": "success",
"data": [
        {
"id": 2,
"name": "A Clash of Kings",
"isbn": "978-0553108033",
"author": [
"George R. R. Martin"
            ],
"number_of_pages": 768,
"publisher": "Bantam Books",
"country": "United States",
"release_date": "1999-02-02"
        }
    ]
}
```
The Books API searchable by name (string), country (string), publisher (string) and release date.

4. Update : PATCH `http://localhost:8080/api/v1/books/:id`
is requested with the following data:
```textmate 
• name
• isbn
• authors
• country
• number_of_pages
• publisher
• release_date
```

Response looks like:
```json
{
"status_code": 200,
"status": "success",
"data": {
        "id": 2,
        "name": "A Clash of Kings",
        "isbn": "978-0553108033",
        "author": [
        "George R. R. Martin"
                    ],
        "number_of_pages": 768,
        "publisher": "Bantam Books",
        "country": "United States",
        "release_date": "1999-02-02"
        }
}
```

5.  Deleting a book : DELETE `http://localhost:8080/api/v1/books/:id`  or POST `http://localhost:8080/api/v1/books/:id/delete`

Response looks like:
```json
{
"status_code": 200,
"status": "success",
"message": "The book My First Book was deleted successfully",
"data": []
}
```

6. Getting a book details using book id GET `http://localhost:8080/api/v1/books/:id`

Response looks like:
```json
{
"status_code": 200,
"status": "success",
"data": {
"id": 1,
"name": "My First Book",
"isbn": "123-3213243567",
"authors": [
"John Doe"
        ],
"number_of_pages": 350,
"publisher": "Acme Books Publishing",
"country": "United States",
"release_date": "2019-01-01"
    }
}
```

Note: If you want to access heroku environment you can replace `http://localhost:8080` to `https://vast-plateau-62808.herokuapp.com`


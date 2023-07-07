# Fibonacci API

This is a simple Django app that provides an API for generating Fibonacci numbers.

## Requirements

- Python 3.11
- Django 4.2

## Design Document
Pdf created by running the following command:-

`docker run -v $PWD:/opt/docs auchida/markdown-pdf markdown-pdf -o DesignDocument.pdf DesignDocument.md`


## How to run

### Virtualenv

## Running in a Virtual Environment

To run the Fibonacci API in a virtual environment, you can follow these steps:

1. Create and activate a virtual environment:

```shell
python -m venv venv       # Create a new virtual environment
source venv/bin/activate # Activate the virtual environment

```

Install the project dependencies:

```shell
pip install -r requirements.txt
```

Run the Django development server:

```shell
python manage.py runserver 8080
Access the Fibonacci API:
```

Run tests:

```shell
python manage.py test
```

Open your web browser and visit http://localhost:8080/to retrieve the next Fibonacci number. Each time you refresh the page or make a request to the API, it will generate and return the next number in the Fibonacci sequence.

### Docker

To run the Fibonacci API using Docker, you can follow these steps:

1. Build the Docker image:

```shell
docker build -t my-django-app .
```

Run a container from the Docker image:

```shell
docker run -p 8080:8080 my-django-app
```

Open your web browser and visit http://localhost:8080/ to retrieve the next Fibonacci number. Each time you refresh the page or make a request to the API, it will generate and return the next number in the Fibonacci sequence.

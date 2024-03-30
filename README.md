# WeirdlyWired.CoreAPIs

## Getting Started

- This project uses Google Gemini for LLM calls.
- To get started you need to have a Google Gemini account and a Google Cloud Project.
- Create an API key for Google Gemini from https://aistudio.google.com/app/apikey.
- Clone `.env.sample` to `.env` and add the API key to the `.env` file.
- Install the requirements using the following command.

```bash
pip install -r requirements.txt
```

- The project uses local postgres and redis sever.
- Using docker-compose you can start the local postgres and redis server.

```bash
docker-compose up -d
```

- Create a database in the local postgres server.
- Add the database name, username and password to the `.env` file.
- Add the redis server details to the `.env` file.
- Run the migrations using the following command.

```bash
python manage.py migrate
```

- Create a superuser using the following command.

```bash
python manage.py createsuperuser
```

## To run the local server

- Running local machine

```bash
run command: uvicorn weirdlywired.asgi:application --reload --debug
```

- Running at local network along with [WeirdlyWired.WebClient](https://github.com/aj-jaiswal007/WeirdlyWired.WebClient)

```bash
daphne -b <local-network> -p 8000 --ping-interval 2 --ping-timeout 5 weirdlywired.asgi:application

# For eg
daphne -b 192.168.1.7 -p 8000 --ping-interval 2 --ping-timeout 5 weirdlywired.asgi:application

```

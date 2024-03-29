FROM python:3.9.18

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend

COPY requirements.txt /app/backend/

# Build psycopg2-binary from source -- add required required dependencies
RUN pip install --upgrade pip \
        && pip install --no-cache-dir -r requirements.txt 

COPY . /app/backend/

EXPOSE 8000

# make migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "uvicorn", " weirdlywired.asgi:application", "--reload",  "--debug" ]
FROM python:3.7-alpine

# Create working dir for web app
WORKDIR /app

# Add pyscopg2 dependencies
RUN apk update && \
    apk add libpq && \
    apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

# Copy requirements
COPY requirements.txt /app

# Install app dependencies
RUN pip install -U pip && \
    pip install -U gunicorn && \
    pip install -r requirements.txt

# Remove build dependencies
RUN apk del .build-deps

# Copy web app source code to container
COPY . /app

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

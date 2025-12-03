# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock /app/

# Install project dependencies
RUN pipenv install --system --deploy --ignore-pipfile

# Copy the rest of the application code to the working directory
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Expose the port the app runs on
EXPOSE 8000

# Run the Gunicorn server
CMD ["gunicorn", "--bind", ":8000","--workers","2", "portfolioServer.wsgi:application"]
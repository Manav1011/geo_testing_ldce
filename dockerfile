# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y libiw-dev

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=geolocation_django.settings
ENV SECRET=django-insecure-v(84_((p$qs44e)_k6s^bl45yheje(_@!(&muo_yrp3gtk5$!1
ENV POSTGRES_INTERNAL_URL=postgres://manav1011:5pAa5uHE6FjCMFTXM3TzKQVpWd1SCXzs@dpg-cnb5u7md3nmc73dpbigg-a.singapore-postgres.render.com/geo_rk1q
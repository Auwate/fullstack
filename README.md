# Fullstack Final Project - Summary

This is the solo final project created for Human Computer Interaction (HCI 4104). This uses the SLMD tech stack, which stands for `Streamlit`, `Linux`, `MySQL`, and `Django REST Framework`, with the entire application wrapped in `Docker`. The rules for the project was that `Streamlit` must be used in the final product.

The overall idea of the project was to create a fullstack application that could take a website and tell you what is on the website using `ChatGPT`. Future iterations may also include a web scraper that provides the HTML content of the webpage, but this was not included to conserve ChatGPT tokens.

# Streamlit

The frontend portion of this application uses `Streamlit`, a robust frontend framework that abstracts many of the complicated UI elements that developers may struggle with. Rather, it focuses on building sleek websites with easy-to-use functions, such as write(), which is the "swiss-army knife" of the `Streamlit` kit.

We use `Streamlit` to ask the user for a website, then send a **POST** request to the backend container which returns some data.

# Linux

The environment this application runs on is `Linux`, specifically the Debian distribution *Bullseye*. This was chosen for the Docker image for its ease of use and relative comfortability the developer already had with the operating system. In addition, its stability and fault tolerant ecosystem was a major benefit for this application.

# MySQL

`MySQL` was used for the database because the stored information is structured data, as well as the ease of use with MySQL. In addition, the developer had prior experience using MySQL with Django, especially in the context of `Docker`.

# Django REST Framework

`Django` is a robust framework that allows developers to quickly create HTML/CSS/JS driven websites. `Django` can serve both frontend and backend purposes, but it also provides a sleek `REST Framework` library for developers to use it solely as a backend application.

For this application, `Django` is used with the `REST Framework` to service *GET* and *POST* requests, where *POST* requests provide the web address and *GET* requests receive ChatGPT's response and recent queries.

# Docker | Docker Compose

To make this application deployable in any environment, `Docker` was used to package dependencies with the application, instead of hoping the future environment might have requirements like `mysqlclient`, version 2.2.4.

We accomplish dependency packaging by using `pipreqs` and a *requirements.txt* file, which the Dockerfile would then read and install.

In addition, `Docker` was used to standardize communications between applications using the built-in network available to `Docker` containers. This allowed the frontend container could easily communicate with the backend container, and the backend container could communicate with the database.

# Get Started

To get started, clone the git repository into your local filesystem using `git clone`.

## IMPORTANT

This application uses the ChatGPT API, which uses "tokens". For this application to run, you must put your API key into api_key.txt in the backend directory.

`cd` into the /deploy folder, which is where the `docker-compose.yml` file lives. You can then run the following command:
```
docker-compose build
```
After it builds, run the next command:
```
docker-compose up
```
The frontend application should be on `localhost:8080`, and the backend application should be on `localhost:8000`.

If you would like to stop the application, press `ctrl+c` or:
```
docker-compose down
```

# To Do
- Fix Docker-Compose functionality
    - Check frontend's ports
    - Do a full removal of all docker builder caches
- Add Streamlit functionality to grab all recent queries and store them in the sidebar
- Work on web scraper
- Add ChatGPT API

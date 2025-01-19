# Exercise 2 - docker

These exercises aim for you to train in docker fundamentals.

## 0. Navigating in docker

a) Create this file structure

```bash
exercise_2
├── dockerfile
└── src
    └── os_data.py
    └── athelete_events.csv
```

b) Create a dockerfile with base image Python 3.9 and with the following packages.

- matplotlib
- pandas

Make sure os_data.py runs when the container starts. Also specify the working directory to /app inside of the container.

c) Create a docker image with name ex0-image

d) Spin up your docker container and name it ex0-container.

e) Go into your container and make sure that these packages are installed.

f) Now create a Python script that prints out the installed packages and the version of Python.

h) Spin up the container in interactive mode. Here are some stuffs you can explore

- check your current directory path
- list all files
- navigate to parents and list files
- list all files inside app
- count all files and folders inside app
- check your operative system
- check the current date
- go up to root and check what files are there

i) Now create your os_data.py app to read in athelete_events.csv as a dataframe, print out df.head(), plot a graph and export it to src folder.

j) You can't see the figure when the container closes, so open it in interactive mode and run your python script from there and check if the figure is there.

## 1. Docker compose

Rewrite exercise 0 using docker compose and do a bind mount of your src folder. Spin up a container and see if the plot appears in your host system.

## 2. Theory questions

&nbsp; a) What is the purpose of a dockerfile?

&nbsp; b) What is the purpose of dockerizing an app?

&nbsp; c) What is the difference between dockerfile and docker compose?

&nbsp; d) What is Docker, and how does it differ from traditional virtualization?

&nbsp; e) What are the key components of Docker?

&nbsp; f) What is a Docker image, and how is it different from a container?

&nbsp; g) What is a Docker volume, and why is it used?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology               | explanation |
| ------------------------- | ----------- |
| host system               |             |
| virtualization            |             |
| spin up                   |             |
| dockerize                 |             |
| docker build              |             |
| docker run                |             |
| docker layers             |             |
| container                 |             |
| image                     |             |
| docker compose up -d      |             |
| docker compose up --build |             |
| docker compose down       |             |
| docker exec -it /bin/bash |             |
| docker inspect            |             |
| docker ps                 |             |
| docker volume ls          |             |
| docker container ls -a    |             |
| docker image ls -a        |             |
| docker image prune        |             |
| docker container prune    |             |
| tag                       |             |
| docker rm                 |             |

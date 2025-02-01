# Exercise 4 - postgres and API

These exercises aim for you to train in postgres, docker and API

## 0. Further explore MYH data

In this task you will continue exploring MYH data which we started on in lecture 09. Use postgres SQL in docker compose and work with sql scripts that you call inside of the docker container.

&nbsp; a) Find out how many data engineer programs have been applied and which schools have applied them along

&nbsp; b) Find out number of data engineer programs that got approved. 

&nbsp; c) Count number of approved programs in each of the education categories (utbildningsområde)

&nbsp; d) Count nubmer of approved programs for each municipality (kommun).

&nbsp; e) Calculate the percentage of approved programs within each education category. 

## 1. EDA on coins data 

Create an account and get an [API key from coinmarketcap](https://coinmarketcap.com/api/documentation/v1/#tag/cryptocurrency). Make sure to store your API key in a file called .env and make sure that you have .env in your .gitignore so that you don't leak your API key. 

&nbsp; a) Explore the endpoint https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest and find out how you can get out relevant data. 

&nbsp; b) Explore the endpoint https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest and find out how you can get out relevant data. 

&nbsp; c) Choose some data from the API endpoints and store it into postgres.



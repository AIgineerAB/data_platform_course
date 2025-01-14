# Exercise 0 - Pandas repetition

These exercises aim for you to train in fundamental pandas.

## 0. Working with national test data

Skolverket is a school authority in Sweden that has collected lots of data for schools in Sweden. We'll analyze national tests results. Data is found [in this repository here](https://github.com/AIgineerAB/data_platform_course/tree/main/exercises/data).

&nbsp; a) Start with reading in the file riket2023_åk9_np.xlsx and the sheets for the different subjects.

&nbsp; b) Change the column names to get something similar to this:

|     | Plats | Huvudman   | Totalt (A-F) | Flickor (A-F) | Pojkar (A-F) | Totalt (A-E) | Flickor (A-E) | Pojkar (A-E) | Totalt (poäng) | Flickor (poäng) | Pojkar (poäng) |
| --: | :---- | :--------- | -----------: | ------------: | -----------: | -----------: | ------------: | -----------: | -------------: | --------------: | -------------: |
|   0 | Riket | Samtliga   |        93225 |         45800 |        47425 |         96.1 |          97.9 |         94.4 |           13.6 |            14.5 |           12.7 |
|   1 | Riket | Kommunal   |        72771 |         35484 |        37287 |         95.7 |          97.6 |         93.8 |           13.3 |            14.3 |           12.4 |
|   2 | Riket | Enskild    |        20414 |         10297 |        10117 |         97.6 |          98.7 |         96.6 |           14.4 |            15.2 |           13.5 |
|   3 | Riket | Skolverket |           40 |            19 |           21 |          100 |           100 |          100 |             15 |            15.9 |           14.2 |

&nbsp; c) Do some initial exploratory data analysis on this dataset. Use methods such as info, value_counts, columns, describe and some more to get a first insight into the dataset.

&nbsp; d) Find out the amount of students that got F in mathematics (both girls and boys).

&nbsp; e) Draw a bar chart on the total points for each of the subjects

&nbsp; f) Feel free to do more EDA on this dataset

## 1. Working with grades data

The dataset is called [betyg_o_prov_riksnivå.xlsx and found here](https://github.com/AIgineerAB/data_platform_course/tree/main/exercises/data).

&nbsp; a) Draw a line chart for proportion of students that are missing approved grade for one or more subjects for the years 18-23.

&nbsp; b) Examine other variable(s) of your choice and check how they affect the students grade. For example you could choose "föräldrarnas utbildningsbakgrund", parents grades.

&nbsp; c) Feel free to do more EDA on this dataset.

## 2. Olympic games data

In this exercise we'll explore the [olympic games data 120 years back](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) in time to see if we can find anything interesting. Many things that we can do in pandas can be done much faster and simpler by using duckdb, so lets use duckdb in this exercise.

We will not create a separate duckdb database in this exercise, instead we'll query a pandas dataframe directly and return a dataframe.

&nbsp; a) Start with reading in the dataset into a dataframe using pandas.

&nbsp; b) Now here is the code for using duckdb on pandas and it will return a df

```from duckdb import query
query(SELECT * FROM df).df()
```

> [!NOTE]
> By combining both pandas and duckdb you will have immense powers and flexibility.

&nbsp; c) Use pandas columns method to find out the columns

&nbsp; d) Find out the 10 oldest atheletes, their age and the sport

&nbsp; e) Find out the 10 youngest atheletes, their age and the sport

&nbsp; e) Find out the five sports with highest median age

&nbsp; f) Find out the five sports with lowest median age

&nbsp; f) Find out top 10 countries after number of gold medals

&nbsp; g) Find out top 10 countries after number of medals

&nbsp; h) Plot a time series line chart of number of female and male atheletes in same graph.

&nbsp; i) Do more explorations on your own

## 3. Theory questions

&nbsp; a) Why could it be good to combine duckdb and pandas?

&nbsp; b) How do you create a DataFrame in Pandas from a dictionary, a list of dictionaries, and a CSV file, json object?

&nbsp; c) What is the difference between .loc[] and .iloc[] for indexing in Pandas?

&nbsp; d) What is the purpose of the .groupby() method in Pandas? How is it used in data aggregation?

&nbsp; e) How do you export a pandas dataframe into a csv file?

&nbsp; f) How do you save a pandas dataframe into a duckdb database?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology           | explanation |
| --------------------- | ----------- |
| dataframe             |             |
| series                |             |
| pandas concat         |             |
| pandas appply         |             |
| csv                   |             |
| pandas isnull         |             |
| masking in pandas     |             |
| pandas transpose      |             |
| pandas value_counts() |             |
| json                  |             |
| tabular data          |             |
| zero-based indexing   |             |

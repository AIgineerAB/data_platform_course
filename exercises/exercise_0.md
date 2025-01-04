# Exercise 0 - Python repetition

These exercises aim for you to train in fundamental Python programming in order to follow along with the course.

## 0. User input for ETL Parameters

Ask the user for 2 inputs:

- source file path
- destination file path

For example:

```
# source path
/Users/aigineer/Documents/data_platform_course/data/file.csv

# destination
/Users/aigineer/Documents/data_platform_course/cleaned_data/file.csv
```

Then the output should be

```
source: /Users/aigineer/Documents/data_platform_course/data/file.csv

destination: /Users/aigineer/Documents/data_platform_course/cleaned_data/file.csv
```

## 1. Schema validation

In order to maintain data quality, consistency and reliability, a system needs to validate that it conforms to certain predefined structure or format. This is called schema validation and you'll practice this in the following exercises.

&nbsp; a) Create a dictionary that look like this

| Key       | Value |
| --------- | ----- |
| id        | 101   |
| name      | Erika |
| is_active | True  |
| age       | 45    |

&nbsp; b) Validate that the id is integer, name is string, is_active is boolean and age is integer. It should return true if valid and false if not valid.

&nbsp; c) The dictionary created can be seen as one row, now lets create more records and store each record (dictionary) in a list.

| id  | name   | is_active | age  |
| --- | ------ | --------- | ---- |
| 102 | Marcus | True      | 34   |
| 103 | David  | False     | 29   |
| 104 | Anna   | True      | 41.5 |
| 106 | Ingrid | NOPE      | 8    |

Note that this list of dictionary is also a JSON array of objects.

&nbsp; d) Do schema validation on the JSON array in c) 

&nbsp; e) Make a function for schema validation and try input the two examples and see if you get correct answer. Also make other examples and test your function. 


## 3. Aggregating json data 



## 2. Theory questions

DESCRIPTION

&nbsp; a)

&nbsp; b)

&nbsp; c)

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology | explanation |
| ----------- | ----------- |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |

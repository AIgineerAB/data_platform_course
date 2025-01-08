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

## 2. Data quality check

Create a function that checks a list that it contains exactly ten elements, and none of them contains None. If they contain None, print out an error message that says that it is invalid and print out what a valid format should be.

## 3. Extract data from logs

In data engineering, log files and log messages are very common. Sometimes you need to parse them to find valuable information, for example for debugging reasons.

Read in `network.log` and extract source IP, destination IP, protocol and data size.

Expected output:

```yaml
Source: 10.0.0.1 | Destination: 10.0.0.2 | Protocol: TCP | Bytes: 1024
Source: 10.0.0.2 | Destination: 10.0.0.3 | Protocol: UDP | Bytes: 2048
Source: 10.0.0.3 | Destination: 10.0.0.1 | Protocol: TCP | Bytes: 512

Data Transfer Summary:
TCP: 1536 bytes
UDP: 2048 bytes
```

Hint: you could probably find some complex regexp pattern, but a more strategic approach is to check the formatting and make a strategy based on that.

## 4. Aggregating json data

Here we will do group by and sum aggregation without using pandas or sql, but plain python to practice the underlying mechanics behind the language.

&nbsp; a) Read in the file paid.json inside of the data folder. Hint: use `load()` function from the `json` library.

&nbsp; b) Now group each name and sum over the total payment. Hint: use `defaultdict(int)` from collections library

&nbsp; c) Output the result into a new json file called `payment_sum.json`.

## 5. Simulating data streams

In this task we will simulate data streams and process it.

```py
simualated_stream = ["record1", "record2", "record3", "record4", "STOP", "record5"]
```

Based on this simulated stream, print out the result `processed record` if the record is not the STOP signal. Print out with 1 second delay between each processed record.

Output for this example is:

```
Starting data stream srocessing...

Processed: record1
Processed: record2
Processed: record3
Processed: record4
STOP signal encountered. Ending stream processing.

Data stream processing completed. Have a nice day
```

## 6. Theory questions

&nbsp; a) What are the fundamental data types in Python?

&nbsp; b) What is the difference between a list and a tuple in Python?

&nbsp; c) How does Python handle mutable and immutable data types?

&nbsp; d) Explain the difference between for and while loops and when to use one or the other.

&nbsp; e) How do you read a file line-by-line in Python?

&nbsp; f) What is a context manager and why would you need to use it?

&nbsp; g) Explain the difference between try, except, else, and finally.

&nbsp; h) What is the difference between ETL and ELT?

&nbsp; i) Differentiate between batch processing and streaming processing.

&nbsp; j) What is a data platform?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology          | explanation |
| -------------------- | ----------- |
| assign               |             |
| logical error        |             |
| handling error       |             |
| indexing             |             |
| slicing              |             |
| iterable             |             |
| iterate over         |             |
| list comprehension   |             |
| collections          |             |
| tuples               |             |
| \_\_repr\_\_         |             |
| dunder methods       |             |
| pythonic             |             |
| idiomatic            |             |
| DRY                  |             |
| spaghetti code       |             |
| keyword arguments    |             |
| positional arguments |             |
| \*args               |             |
| \*\*kwargs           |             |
| unpacking list       |             |
| return statement     |             |
| ternary operator     |             |
| json                 |             |
|                      |             |

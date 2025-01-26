# Exercise 3 - kafka

These exercises aim for you to train in kafka fundamentals.

## 0. Setup kafka local without docker (optional)

In this task you will try to install Kafka locally on your computer without using docker in order for you to feel the pain without docker and appreciate dockers power more.

> [!NOTE]
> This task is meant for your curiosity and is not neccessary to follow along in your kafka journey.

- [mac installation instructions](https://learn.conduktor.io/kafka/how-to-install-apache-kafka-on-mac-without-zookeeper-kraft-mode/)
- [windows installation instructions](https://learn.conduktor.io/kafka/how-to-install-apache-kafka-on-windows-without-zookeeper-kraft-mode/)
- [linux installation instructions](https://learn.conduktor.io/kafka/how-to-install-apache-kafka-on-linux-without-zookeeper-kraft-mode/)

## 1. Explore orders data

Use the dataset orders.json, which simulates a few orders from an electronic shop. 

&nbsp; a) Load the json file, read it in and try to understand the data. 

&nbsp; b) Use python and perhaps pandas to print out each order with the product, quantity, price and total price. One order could have the following output 

```python
Input: {'order_id': 'ORD-1009', 'customer': 'George Clark', 'products': [{'name': 'Smartwatch', 'price': 199.99, 'quantity': 1}, {'name': 'USB-C Cable', 'price': 14.99, 'quantity': 2}, {'name': 'Iphone 15', 'price': 600.99, 'quantity': 1}], 'order_date': '2024-01-17', 'status': 'Processing'}
Product: Smartwatch           Quantity: 1                    Price: 199.99              
Product: USB-C Cable          Quantity: 2                    Price: 14.99               
Product: Iphone 15            Quantity: 1                    Price: 600.99              
Total price: 830.96
```


## 2. Stream the orders data into Kafka

Now do similar outputs as in exercise 1 but using a producer to produce the data to a topic in Kafka and then consuming the data. In the consumer, you will process the data to print out similar to above. 


## 3. Theory questions

&nbsp; a) What is Apache Kafka, and how does it work?

&nbsp; b) What is a Kafka topic?

&nbsp; c) How does the Kafka broker, cluster and partitions relate to each other?

&nbsp; d) What are Kafka producers and consumers and the publish-subscribe model?

&nbsp; e) How does Kafka guarantee message ordering?

&nbsp; f) What is key-based partitioning in Kafka?

&nbsp; g) How do you setup Kafka locally? 


## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology             | explanation |
| ----------------------- | ----------- |
| kafka                   |             |
| event                   |             |
| message                 |             |
| producer                |             |
| consumer                |             |
| topic                   |             |
| publish                 |             |
| subscribe               |             |
| sink                    |             |
| publish-subscribe model |             |
| source system           |             |
| partition               |             |
| serialization           |             |
| deserialization         |             |
| pull model              |             |
| push model              |             |
| client                  |             |
| advertise               |             |
| ports mapping           |             |
| detached mode           |             |
| docker exec -it         |             |
|                         |             |

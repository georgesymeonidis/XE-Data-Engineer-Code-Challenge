# XE-Data-Engineer-Code-Challenge

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [How to use](#how-to-use)

## General info
When a customer creates a classified, the system emit a record of it and publish it to a Kafka topic. For that reason we created an application that consumes these records, record them in a MySQL database and write a SQL script to analyse this information. To be more specific, we connected to the Kafka Topic and from there we parse the data and save it in our SQL database. The values that we stored are the id, customer_id, created_at, text, ad_type, price, currency, payment_type, payment_cost and offset. In some cases that the ad_type was "Free" we did not have the columns price, currency, payment_type, payment_cost so we seted the values as Null. Furthermore, we added the offset column so we know every time which was the last offset value that we imported in the database. By having these values stored in our Database we then calculated the margin based on the payment_time and ad_type over time. Last but not least we created an event scheduler in order for the stored procedure to run automatically avoiding in that way running the same aggregations again and again. 
	
## Setup
In order to use the application, we have first to create the MySQL tables in order to save our results. Then we have to run the application in our terminal by using the command below.
	
## How to use?
To run this project clone it in your directory and then open a terminal and run the command below inside the directory you saved the project:

```
$ python Data_Engineer_Code_Challenge.py
```

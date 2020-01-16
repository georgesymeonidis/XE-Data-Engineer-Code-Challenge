# XE-Data-Engineer-Code-Challenge

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [How to use](#how-to-use)

## General info
When a customer creates a classified, the system emit a record of it and publish it to a Kafka topic. For that reason we created an application that consumes these records, record them in a MySQL database and write a SQL script to analyse this information.
	
## Setup
In order to use the application, we have first to create the MySQL tables in order to save our results. Then we have to run the application in our terminal by using the command below.
	
## How to use?
To run this project clone it in your directory and then open a terminal and run the command below inside the directory you saved the project:

```
$ python Data_Engineer_Code_Challenge.py
```

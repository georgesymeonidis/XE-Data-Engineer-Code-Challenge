from kafka import KafkaConsumer, TopicPartition
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import json

def insert_into_db(id, customer_id, created_at, text, ad_type, price, currency, payment_type, payment_cost, offset):
    try:
        #here we connect to the database
        connection = mysql.connector.connect(host='gsdataengineer.cg2t1fioak49.eu-west-3.rds.amazonaws.com',
                                             database='gsdataengineer',
                                             user='root',
                                             password='eTypgr78Lp9tWL9sfLkpWsFs9Vnhtcv2')
        #connection cursor
        cursor = connection.cursor()
        #sql query for inserting the values into classifieds table
        mySql_insert_query = """INSERT IGNORE INTO Classifieds (id, customer_id, created_at, text, ad_type, price, currency, payment_type, payment_cost, offset) 
                               VALUES 
                               (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        #passing the values into sql query
        recordTuple = (id, customer_id, created_at, text, ad_type, price, currency, payment_type, payment_cost, offset)            
        #executing query
        cursor.execute(mySql_insert_query, recordTuple)
        #commiting the values into db and closing the cursor 
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Classifieds table")
        cursor.close()

    #exception in case something goes wrong
    except mysql.connector.Error as error:
        print("Failed to insert record into Classifieds table {}".format(error))
    #closing connection
    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")
            
def check_offset_number():
    try:
        connection = mysql.connector.connect(host='gsdataengineer.cg2t1fioak49.eu-west-3.rds.amazonaws.com',
                                             database='gsdataengineer',
                                             user='root',
                                             password='eTypgr78Lp9tWL9sfLkpWsFs9Vnhtcv2')

        #selection query for checking if we have offset values in db
        mySql_select_query = " SELECT offset FROM Classifieds ORDER BY offset DESC LIMIT 1 "
        
        cursor = connection.cursor()
        cursor.execute(mySql_select_query)
        records = cursor.fetchall()
        return records
        cursor.close()
        
    except mysql.connector.Error as error:
        print("Failed to select record from Classifieds table {}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()

def main():
    try:
        #conenction to kafka and setting the parameters and arguments
        consumer = KafkaConsumer('data',
                             group_id='my-group',
                             consumer_timeout_ms=10000,
                             fetch_max_wait_ms = 100,
                             bootstrap_servers=['35.180.144.76'])
        
        #fetching data from topic
        consumer.poll()
        #we are checking the results from select query so we if its the first time that we are running
        #the application. We need to know if it is the first time or not.
        if (len(check_offset_number()) == 0):
            consumer.seek_to_beginning()
        
        while True:
            #we are using while true so the program will run forever until we stop it.
            #we are using the insert_into_db function to pass the values into db
            for message in consumer:
                print(message.offset)
                data = eval(message.value)
                if (data["ad_type"] == "Free"):
                    insert_into_db(data["id"], data["customer_id"], data["created_at"], data["text"], data["ad_type"], None, None, None, None, message.offset)
                else:
                    insert_into_db(data["id"], data["customer_id"], data["created_at"], data["text"], data["ad_type"], data["price"], data["currency"], data["payment_type"], data["payment_cost"], message.offset)
            #we are using commit_async so we dont wait for the values to commited and then continue
            #in that way it will be much faster.       
            consumer.commit_async()
    except Exception:
        print("There was an error")
    finally:
        consumer.close()

if __name__== "__main__":
  main()

    

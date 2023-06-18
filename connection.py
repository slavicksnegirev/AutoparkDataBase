import pandas as pd
import mysql.connector
from mysql.connector import Error


class DataBase():
    def __init__(self):
        super(DataBase, self).__init__()
        self.connection = self.create_connection("localhost", "root", "142536475869", "mydb")
        self.create_database(self.connection, "USE mydb")
        # self.insert_into_driver_SSI('1', '2', '3', '2023-01-01', '5', '6', '7')
        # self.update_driver_SSI('Дроздов', '2', '3', '2023-01-01', '5', '6', '23 56 857375', 11)
        # self.delete_driver_SSI(12)

    def create_connection(self, host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def create_database(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, connection, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def insert_into_driver_SSI(self, surname, name, patronymic, date_of_birth, address, phone_number,
                               license_number):
        query = f"""INSERT INTO driver_SSI (`surname`, `name`, `patronymic`, `date_of_birth`, `address`, 
        `phone_number`, `license_number`) VALUES ("{surname}", "{name}", "{patronymic}", "{date_of_birth}", "{address}", "{phone_number}", 
        "{license_number}")"""
        # cursor = self.connection.cursor()
        # cursor.executemany(query, [(surname, name, patronymic, date_of_birth, address, phone_number, license_number)])
        # self.connection.commit()
        self.execute_query(self.connection, query)

    def update_driver_SSI(self, surname, name, patronymic, date_of_birth, address, phone_number,
                               license_number, driver_ID):
        query = f"""UPDATE driver_SSI SET surname = "{surname}", name = "{name}", patronymic = "{patronymic}", date_of_birth =
         "{date_of_birth}", address = "{address}", phone_number = "{phone_number}", license_number = "{license_number}" WHERE driver_ID = {driver_ID}"""
        self.execute_query(self.connection, query)

    def delete_driver_SSI(self, driver_ID):
        query = f"""DELETE FROM driver_SSI WHERE driver_ID = {driver_ID}"""
        self.execute_query(self.connection, query)

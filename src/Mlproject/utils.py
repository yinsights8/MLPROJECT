import os
import sys   # to handle custom exception
from src.Mlproject.exception import CustomException
from src.Mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql as sql

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')


def read_sql_data():
    logging.info("Reading sql database started...")

    try:
        mydb = sql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info("Connection established...",mydb)

        df = pd.read_sql_query("select * from students", mydb)
        print(df.head())

        return df


    except Exception as e:
        raise CustomException(e)
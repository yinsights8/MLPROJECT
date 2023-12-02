# read the data from datasource and apply train test split the output will be in dataset in train test split
# 1. MySQL ---> train test split -- > dataset

import os
import sys   # to handle custom exception
from src.Mlproject.exception import CustomException
from src.Mlproject.logger import logging
import pandas as pd
from src.Mlproject.utils import read_sql_data

from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts", "train.csv")
    test_data_path:str=os.path.join("artifacts", "test.csv")
    raw_data_path:str=os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.Ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        try:

            # reading data from mysql 
            df = read_sql_data()
            logging.info("Reading from mysql database...")

            os.makedirs(os.path.dirname(self.Ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.Ingestion_config.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)     
            df.to_csv(self.Ingestion_config.train_data_path, index=False, header=True)
            df.to_csv(self.Ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion is completed successfully")



        except Exception as e:
            raise CustomException(e, sys)



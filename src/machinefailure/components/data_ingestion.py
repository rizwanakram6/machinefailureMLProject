import os
import sys
from src.machinefailure.exception import CustomException
from src.machinefailure.logger import logging
from src.machinefailure.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
  train_data_path = os.path.join('artifact', 'train.csv')
  test_data_path = os.path.join('artifact', 'test.csv')
  raw_data_path = os.path.join('artifact', 'raw.csv')

class DataIngestion:
  def __init__(self) -> None:
    self.data_ingestion_config = DataIngestionConfig()

  def initiate_data_ingestion(self):
    try:
      df= read_sql_data()
      logging.info("READING DATA FROM DATABASE COMPLETED")

      os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)

      df.to_csv(self.data_ingestion_config.raw_data_path, index=False, header=True)

      train_set, test_set = train_test_split(df, random_state=42, test_size=0.2)

      train_set.to_csv(self.data_ingestion_config.train_data_path,index=False, header=True)
      test_set.to_csv(self.data_ingestion_config.test_data_path, header=True, index=False)

      logging.info("DATA INGESTION COMPLETED")
      return(
        self.data_ingestion_config.test_data_path,
        self.data_ingestion_config.test_data_path
      )

    except Exception as e:
      raise CustomException(e, sys)
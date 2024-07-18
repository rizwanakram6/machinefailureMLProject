from src.machinefailure.logger import logging
from src.machinefailure.exception import CustomException
from src.machinefailure.components.data_ingestion import DataIngestion
import sys


if __name__== "__main__":
  logging.info("EXECUTION STARTED")
  
  try:
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()

    


  except Exception as e:
    logging.info("CUSTOM EXCEPTION RAISED")
    raise CustomException(e, sys)


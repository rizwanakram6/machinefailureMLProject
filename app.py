from src.machinefailure.logger import logging
from src.machinefailure.exception import CustomException
from src.machinefailure.components.data_ingestion import DataIngestion
from src.machinefailure.components.data_transformation import DataTransformation
import sys


if __name__== "__main__":
  logging.info("EXECUTION STARTED")
  
  try:
    data_ingestion = DataIngestion()
    train_df, test_df =data_ingestion.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_df, test_df)


  except Exception as e:
    logging.info("CUSTOM EXCEPTION RAISED")
    raise CustomException(e, sys)


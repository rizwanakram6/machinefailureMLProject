from src.machinefailure.logger import logging
from src.machinefailure.exception import CustomException
import sys


if __name__== "__main__":
  logging.info("EXECUTION STARTED")



  try:
    a=1/0
  except Exception as e:
    logging.info("CUSTOM EXCEPTION RAISED")
    raise CustomException(e, sys)


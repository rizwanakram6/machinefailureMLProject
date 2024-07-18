import os
import sys
import pymysql
import pandas as pd
from src.machinefailure.exception import CustomException
from src.machinefailure.logger import logging
from dotenv import load_dotenv

import pandas as pd
import pickle



load_dotenv()

host = os.getenv("host")
username = os.getenv("username")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
  logging.info("READING SQL DATABASE STARTED")
  try:
    mydb = pymysql.connect(
      host= host,
      user= username,
      password= password,
      db= db
    )

    logging.info("Connection Established ", mydb)
    df = pd.read_sql_query("Select * from machinefailuredata", mydb)

    print(df.head())
    return df

  except Exception as e:
    raise CustomException(e,sys)




def save_object(file_path, obj):
  try:
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "wb") as file_obj:
      pickle.dump(obj, file_obj)
  
  except Exception as e:
    raise CustomException(e,sys)

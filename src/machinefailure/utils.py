import os
import sys
import pymysql
import pandas as pd
from src.machinefailure.exception import CustomException
from src.machinefailure.logger import logging
from dotenv import load_dotenv

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




import os
import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass
from src.machinefailure.exception import CustomException
from src.machinefailure.logger import logging
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer


@dataclass
class DataTransformationConfig:
  preprocessor_obj_path = os.path.join('artifact', 'preprocessor.pkl')

class DataTransformation:
  def __init__(self) -> None:
    self.data_transformation_obj = DataTransformationConfig()

  def data_transformer_obj(self):
    try:
      num_cols = ['footfall','tempMode', 'AQ', 'USS', 'CS', 'VOC', 'RP', 'IP', 'Temperature']

      num_pipeline = Pipeline(steps= [
        ('impute', SimpleImputer(strategy='median')),
        ('scalar', StandardScaler())
      ])

      logging.info("Numerical Columns {}".format(num_cols))

      preprocessor = ColumnTransformer([
        ('num_pipeline', num_pipeline, num_cols)
      ])

      return preprocessor

    except Exception as e:
      raise CustomException(e,sys)
    
  def initiate_data_transformation(self, train_path, test_path):
    try:
      train_df = pd.read_csv(train_path)
      test_df = pd.read_csv(test_path)

      logging.info("Reading the train and test file")

      preprocessing_obj = self.data_transformer_obj()

      target_cols_name = ["fail"]
      num_cols_name = ['footfall','tempMode', 'AQ', 'USS', 'CS', 'VOC', 'RP', 'IP', 'Temperature']

      

    except Exception as e:
      raise CustomException(e,sys)
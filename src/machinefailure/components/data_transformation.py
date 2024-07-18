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
from src.machinefailure.utils import save_object

@dataclass
class DataTransformationConfig:
  preprocessor_obj_path = os.path.join('artifact', 'preprocessor.pkl')

class DataTransformation:
  def __init__(self) -> None:
    self.data_transformation_config = DataTransformationConfig()

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

      ## Divide the train dataset to independent and dependent feature
      input_features_train_df = train_df.drop(columns=target_cols_name, axis=1)
      target_features_train_df = train_df[target_cols_name]


      input_features_test_df = test_df.drop(columns=target_cols_name, axis=1)
      target_features_test_df = test_df[target_cols_name]

      logging.info("Applying Preprocessing on train & test DataFrame")

      input_feature_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
      input_feature_test_arr = preprocessing_obj.transform(input_features_test_df)

      test_arr = np.c_[
        input_feature_test_arr, np.array(target_features_test_df)
      ]

      train_arr = np.c_[
        input_feature_train_arr, np.array(target_features_train_df)
      ]

      logging.info("Save Preprocessing Object")

      save_object(
        file_path= self.data_transformation_config.preprocessor_obj_path,
        obj= preprocessing_obj
      )
      logging.info("DATA TRANSFORMATION COMPLETED")

      return(
        train_arr,
        test_arr,
        self.data_transformation_config.preprocessor_obj_path
      )

    except Exception as e:
      raise CustomException(e,sys)
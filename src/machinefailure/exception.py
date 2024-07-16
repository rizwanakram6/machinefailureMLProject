import sys
from src.machinefailure.logger import logging

def error_msg_detail(error, error_detail:sys):
  _,_, exc_tb = error_detail.exc_info()
  file_name = exc_tb.tb_frame.f_code.co_name
  error_message = "Error occured in python script name [{0}] line number [{1}] error message".format(file_name, exc_tb.tb_lineno, str(error_message))

  return error_message

class CustomException(Exception):
  def __init__(self,error_message, error_details:sys) -> None:
    super().__init__(error_message)
    self.error_message = error_msg_detail(error_message, error_details)

  def __str__(self) -> str:
    return self.error_message
  

 
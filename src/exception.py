import sys
from src.logger import logging
def error_message_details(error, error_details:sys ):
    _,_,exec_tb=error_details.exc_info()
    file_name= exec_tb.tb_frame.f_code.co_filename
    error_message= "Error occured in script [{0}] in line no. [{1}] error message[{2}]".format(
    file_name,exec_tb.tb_lineno,str(error))

class customException(Exception) :
    def __init__(self, error_message, error_details:sys): 
        super().__init__(error_message)
        self.error_message= error_message_details(error_message, error_details=error_details) 
    def _str_(self):
        return self.error_message
if __name__=="__main__":
    try:
        a=1/0
        logging.info("This is a test log message")
    except Exception as e:
        logging.info("arithmetic exception")
        raise customException
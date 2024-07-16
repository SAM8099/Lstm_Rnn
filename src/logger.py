import logging
import os
from datetime import datetime

log_file=f"{datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(log_path,exist_ok=True)
log_file_path = os.path.join(log_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
)


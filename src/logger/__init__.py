import os
import sys
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "Logs" , LOG_FILE)
os.makedirs(log_path , exist_ok=True)

Log_file_path = os.path.join(log_path , LOG_FILE)

logging.basicConfig(
    filename= Log_file_path,
    format= '[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level= logging.INFO
)
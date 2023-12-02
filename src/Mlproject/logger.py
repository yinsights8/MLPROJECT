import os
import logging
from datetime import datetime as dt

## This logger.py file is responsible for reporting errors when happens during runtime.



LOG_FILE = f"{dt.now().strftime('%Y_%m_%d%I_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d  %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
    )

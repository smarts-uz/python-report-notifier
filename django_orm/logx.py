import logging
import os
from datetime import datetime


class Logger():
    def __init__(self,module_name,fm):
        self.logger = logging.getLogger(module_name)
        formater = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        self.logger.info(f"Running module {module_name}...")
        handler2 = logging.FileHandler(f"{logger_path()}{module_name}.log", mode=fm, encoding='utf-8')
        handler2.setFormatter(formater)
        self.logger.addHandler(handler2)

    def log(self,message):
        self.logger.setLevel(logging.DEBUG)
        self.logger.info(message)

    def err(self, err):
        self.logger.setLevel(logging.ERROR)
        self.logger.exception(err)



def logger_path():
    year, month, day = datetime.now().year, datetime.now().month, datetime.now().day
    logger_path = f"C:/Report-Logs/logs/{year}/{month}/{day}/"
    if not os.path.exists(logger_path):
        os.makedirs(logger_path)
    return logger_path
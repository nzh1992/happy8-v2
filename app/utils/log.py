import os

from loguru import logger

log_fp = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), "logs","log_{time:YYYY-MM-DD}.log")
print(log_fp)
logger.add(log_fp, rotation="1 days", compression="zip")
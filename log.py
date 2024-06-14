from config import log_type
from const import LOG_TYPE_TRACE, LOG_TYPE_ERROR, LOG_TYPE_INFO
from datetime import datetime, timezone
import logging

def printLog(logType, message):

    if log_type == LOG_TYPE_ERROR and logType != LOG_TYPE_ERROR:
        return

    if log_type == LOG_TYPE_INFO and logType == LOG_TYPE_TRACE:
        return

    dt = datetime.now(timezone.utc)

    logging.info(f"{dt} [{logType}] {message}")

    print(f"{dt} [{logType}] {message}")

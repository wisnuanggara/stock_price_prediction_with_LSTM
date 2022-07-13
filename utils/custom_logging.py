import logging
import sys
import os
import datetime
import config

today = datetime.datetime.today()
log_level = config.LOGLEVEL
log_dir = config.LOGDIRECTORY
log_filename = config.LOGFILENAME

def set_logging(level, message):
    """ Set logging configuration level, format & handler"""
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(log_dir, log_filename)),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger('kompas_log')

    level_log = ['DEBUG','INFO','WARNING','CRITICAL','ERROR']

    if level in level_log and type(level) is str:
        if level == 'DEBUG':
            return logger.debug(message)
        elif level == 'INFO':
            return logger.info(message)
        elif level == 'WARNING':
            return logger.warning(message)
        elif level == 'CRITICAL':
            return logger.critical(message)
        else:
            return logger.error(message)

    raise ValueError("Logging Level Not Found !")
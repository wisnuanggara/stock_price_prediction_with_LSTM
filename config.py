import os
import datetime as dt
import logging

today = dt.datetime.today()
_basedir_ = os.path.abspath(os.path.dirname(__file__))

""" LOGGING CONFIG """
LOGLEVEL = logging.DEBUG
LOGDIRECTORY = os.getenv("LOGDIRECTORY", _basedir_+"\logs")
LOGFILENAME = os.getenv("LOGFILENAME", f"{today.year}-{today.month:02d}-{today.day:02d}.log")
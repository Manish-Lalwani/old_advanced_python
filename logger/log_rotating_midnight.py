
"""
WAS GETTING FILENAME ISSUE AS THE DEFAULT TIMELOGGER WAS CREATING NEW FILE BUT WITH OLD(YESTERDAY'S DATE)
REF LINK: https://stackoverflow.com/questions/24649789/how-to-force-a-rotating-name-with-pythons-timedrotatingfilehandler
"""
import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import time
import os
import re


class ParallelTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, postfix = ".log",atTime=None):
        super().__init__(filename=filename, when=when, interval=interval, backupCount=backupCount, encoding=encoding, delay=delay, utc=utc)

        self.origFileName = filename
        self.when = when.upper()
        self.interval = interval
        self.backupCount = backupCount
        self.utc = utc
        self.postfix = postfix

        if self.when == 'S':
            self.interval = 1 # one second
            self.suffix = "%Y-%m-%d_%H-%M-%S"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$"
        elif self.when == 'M':
            self.interval = 60 # one minute
            self.suffix = "%Y-%m-%d_%H-%M"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}$"
        elif self.when == 'H':
            self.interval = 60 * 60 # one hour
            self.suffix = "%Y-%m-%d_%H"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}$"
        elif self.when == 'D' or self.when == 'MIDNIGHT':
            self.interval = 60 * 60 * 24 # one day
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        elif self.when.startswith('W'):
            self.interval = 60 * 60 * 24 * 7 # one week
            if len(self.when) != 2:
                raise ValueError("You must specify a day for weekly rollover from 0 to 6 (0 is Monday): %s" % self.when)
            if self.when[1] < '0' or self.when[1] > '6':
                 raise ValueError("Invalid day specified for weekly rollover: %s" % self.when)
            self.dayOfWeek = int(self.when[1])
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        else:
            raise ValueError("Invalid rollover interval specified: %s" % self.when)

        currenttime = int(time.time())
        logging.handlers.BaseRotatingHandler.__init__(self, self.calculateFileName(currenttime), 'a', encoding, delay)

        self.extMatch = re.compile(self.extMatch)
        self.interval = self.interval * interval # multiply by units requested

        self.rolloverAt = self.computeRollover(currenttime)

    def calculateFileName(self, currenttime):
        if self.utc:
             timeTuple = time.gmtime(currenttime)
        else:
             timeTuple = time.localtime(currenttime)

        return self.origFileName + time.strftime(self.suffix, timeTuple) + self.postfix

    def getFilesToDelete(self, newFileName):
        dirName, fName = os.path.split(self.origFileName)
        dName, newFileName = os.path.split(newFileName)

        fileNames = os.listdir(dirName)
        result = []
        prefix = fName + "."
        postfix = self.postfix
        prelen = len(prefix)
        postlen = len(postfix)
        for fileName in fileNames:
            if fileName[:prelen] == prefix and fileName[-postlen:] == postfix and len(fileName)-postlen > prelen and fileName != newFileName:
                 suffix = fileName[prelen:len(fileName)-postlen]
                 if self.extMatch.match(suffix):
                     result.append(os.path.join(dirName, fileName))
        result.sort()
        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def doRollover(self):
         if self.stream:
            self.stream.close()
            self.stream = None

         currentTime = self.rolloverAt
         newFileName = self.calculateFileName(currentTime)
         newBaseFileName = os.path.abspath(newFileName)
         self.baseFilename = newBaseFileName
         self.mode = 'a'
         self.stream = self._open()

         if self.backupCount > 0:
             for s in self.getFilesToDelete(newFileName):
                 try:
                     os.remove(s)
                 except:
                     pass

         newRolloverAt = self.computeRollover(currentTime)
         while newRolloverAt <= currentTime:
             newRolloverAt = newRolloverAt + self.interval

         #If DST changes and midnight or weekly rollover, adjust for this.
         if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
             dstNow = time.localtime(currentTime)[-1]
             dstAtRollover = time.localtime(newRolloverAt)[-1]
             if dstNow != dstAtRollover:
                 if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                     newRolloverAt = newRolloverAt - 3600
                 else:           # DST bows out before next rollover, so we need to add an hour
                     newRolloverAt = newRolloverAt + 3600
         self.rolloverAt = newRolloverAt


class Logger:
    def __init__(self, file_handler_level = logging.DEBUG,stream_handler_level = logging.INFO,
                 filename="log",filemode="a",logger_user = __name__,
                 console_output_flag =1,file_output_flag =1,
                 format="""%(asctime)s %(levelname)s %(lineno)s %(message)s """, datefmt="""%d %b %y %H:%M:%S"""):

        self.logger = logging.getLogger(logger_user)
        self.logger.setLevel(logging.DEBUG)
        #self.filename = './logs'+'/{}_{}.log'.format(filename,datetime.now().strftime("%d-%m-%Y"))
        self.filename = './logs/log_'
        self.stream_handler_level = stream_handler_level
        self.file_handler_level = file_handler_level
        self.format = format
        self.datefmt = datefmt
        self.console_output_flag = console_output_flag  # if console_output_flag set to 1 will print to console also
        self.file_output_flag = file_output_flag
        self.create_handler()

    def create_handler(self):
        # Create handlers
        c_handler = logging.StreamHandler() #stream handler writes to console
        f_handler = ParallelTimedRotatingFileHandler(self.filename,when="midnight",backupCount=1)
        c_handler.setLevel(self.stream_handler_level)
        f_handler.setLevel(self.file_handler_level)

        # Create formatters and add it to handlers
        c_format = self.format
        f_format = self.format
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        if self.console_output_flag == 1:
            self.logger.addHandler(f_handler)
        if self.console_output_flag ==1:
            self.logger.addHandler(c_handler)


    def get_logger(self):
        return self.logger



class CustomizeLogFormatter(logging.Formatter):
    def format(self, record):
        try:
            record.project_id = '01'
            record.technical_module_name = '-'
            record.sub_module_id = '-'
            record.unique_value = '-'
            record.host = '2'
            record.port = '3'
            record.type = '-'
            record.tag = '-'

            if (record.args):
                record.project_id = '01'
                record.technical_module_name = record.args.get("technical_module_name", "Python")  # default Python
                record.sub_module_id = record.args.get("sub_module_id", "sub_module_id")  # default sub_module_id
                record.unique_value = record.args.get("unique_value", "000")  # default 000
                record.host = record.args.get("host",'2')  # default properties.HOST_IP
                record.port = record.args.get("port", '4')  # default properties.PORT
                record.type = record.args.get("type", "AppLog")  # default AppLog
                record.tag = record.args.get("tag", "tag")  # default tag
                return super().format(record)
        except Exception as e:
            print(e)


l1 = Logger(format=CustomizeLogFormatter("""%(asctime)s | %(project_id)s | %(technical_module_name)s | %(sub_module_id)s | %(unique_value)s | %(host)s | %(port)s | %(type)s | %(tag)s | %(levelname)s | %(message)s""", datefmt="%d/%b/%y %H:%M:%S %Z"), logger_user='optivity_logger')
log = l1.get_logger() #use this object for logging.

if __name__ == "__main__":
    while True:
        log.error("This is a error message ",{'sub_module_id': '@'})
        time.sleep(2)
    
import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

class  EnhancedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler, logging.handlers.RotatingFileHandler):
    '''
        cf http://stackoverflow.com/questions/29602352/how-to-mix-logging-handlers-file-timed-and-compress-log-in-the-same-config-f

         Spec:
         Log files limited in size & date. I.E. when the size or date is overtaken, there is a file rollover
     '''

    ########################################


    def __init__(self, filename, mode = 'a', maxBytes = 0, backupCount = 0, encoding = None,
             delay = 0, when = 'h', interval = 1, utc = False):

        logging.handlers.TimedRotatingFileHandler.__init__(
        self, filename, when, interval, backupCount, encoding, delay, utc)

        logging.handlers.RotatingFileHandler.__init__(self, filename, mode, maxBytes, backupCount, encoding, delay)

     ########################################

    def computeRollover(self, currentTime):
         return logging.handlers.TimedRotatingFileHandler.computeRollover(self, currentTime)

    ########################################

    def getFilesToDelete(self):
        return logging.handlers.TimedRotatingFileHandler.getFilesToDelete(self)

    ########################################

    def doRollover(self):
        return logging.handlers.TimedRotatingFileHandler.doRollover(self)

    ########################################

    def shouldRollover(self, record):
         """ Determine if rollover should occur. """
         return (logging.handlers.TimedRotatingFileHandler.shouldRollover(self, record) or logging.handlers.RotatingFileHandler.shouldRollover(self, record))

class Logger:
    def __init__(self, file_handler_level = logging.DEBUG,stream_handler_level = logging.INFO,
                 filename="log",filemode="a",logger_user = __name__,
                 console_output_flag =1,file_output_flag =1,
                 format="""%(asctime)s %(levelname)s %(lineno)s %(message)s """, datefmt="""%d %b %y %H:%M:%S"""):

        self.logger = logging.getLogger(logger_user)
        self.logger.setLevel(logging.DEBUG)
        self.filename = './logs/{}_{}.log'.format(filename,datetime.now().strftime("%d-%m-%Y"))
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
        # f_handler = logging.FileHandler(self.filename) #file handler writes to file #original
        #f_handler = RotatingFileHandler(self.filename, maxBytes=20,backupCount=5)  #based on mb's
        #f_handler = TimedRotatingFileHandler(self.filename,when="s",interval=10,backupCount=5)
        f_handler = EnhancedRotatingFileHandler(self.filename,maxBytes=200,backupCount=5,when='m',interval=1)
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


if __name__ == "__main__":
    l1 = Logger(filename="temp",logger_user='1')
    log = l1.get_logger()
    l2 = Logger(filename="temp2",logger_user='2')
    log2 = l2.get_logger()
    # log.debug("This is a debug message ")
    # log.info("This is a info message ")
    # log.warning("This is a warning message ")
    # log.error("This is a error message ")
    # log2.error("Writing in temp2 file")

    for i in range(0,100):
        log2.error("Writing in temp2 file")


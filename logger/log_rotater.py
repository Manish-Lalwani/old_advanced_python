import os
import gzip
import logging.handlers

class NewRotatingFileHandler(logging.handlers.RotatingFileHandler):
    def __init__(self, filename, **kws):
        backupCount = kws.get('backupCount', 0)
        self.backup_count = backupCount
        logging.handlers.RotatingFileHandler.__init__(self, filename, **kws)

    def doArchive(self, old_log):
        with open(old_log) as log:
            with gzip.open(old_log + '.gz', 'wb') as comp_log:
                comp_log.writelines(log)
        os.remove(old_log)
    def namer(self,name):
        return name + ".gz"

    # def rotator(self,source, dest):
    #     print("*****************************************")
    #     with open(source, "rb") as sf:
    #         data = sf.read()
    #         compressed = zlib.compress(data, 9)
    #         with open(dest, "wb") as df:
    #             df.write(compressed)
    #     os.remove(source)

    def doRollover(self):
      print("##############################")
      print(self.namer)
      print(self.rotator)
      if self.stream:
          self.stream.close()
          self.stream = None
      if self.backup_count > 0:
          for i in range(self.backup_count - 1, 0, -1):
              sfn = "%s.%d.gz" % (self.baseFilename, i)
              dfn = "%s.%d.gz" % (self.baseFilename, i + 1)
              if os.path.exists(sfn):
                  if os.path.exists(dfn):
                      os.remove(dfn)
                  os.rename(sfn, dfn)
      dfn = self.baseFilename + ".1"
      if os.path.exists(dfn):
          os.remove(dfn)
      if os.path.exists(self.baseFilename):
          os.rename(self.baseFilename, dfn)
          print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
          self.doArchive(dfn)
          #self.rotator(dfn,dfn+".gz")
      if not self.delay:
          self.stream = self._open()



import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime



class Logger:
    def __init__(self, file_handler_level = logging.DEBUG,stream_handler_level = logging.INFO,
                 filename="log",filemode="a",logger_user = __name__,
                 console_output_flag =1,file_output_flag =1,
                 format="""%(asctime)s %(levelname)s %(lineno)s %(message)s """, datefmt="""%d %b %y %H:%M:%S"""):

        self.logger = logging.getLogger(logger_user)
        self.logger.setLevel(logging.DEBUG)
        self.filename = './{}_{}.log'.format(filename,datetime.now().strftime("%d-%m-%Y"))
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
        # f_handler = logging.FileHandler(self.filename) #file handler writes to file
        f_handler = NewRotatingFileHandler(self.filename, maxBytes=20,backupCount=5)
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


def methods(cls):
  z = [x for x, y in cls.__dict__.items()]
  print(z)
    #return [x for x, y in cls.__dict__.items() if type(y) == FunctionType]


if __name__ == "__main__":
    l1 = Logger(filename="temp",logger_user='1')
    log = l1.get_logger()
    l2 = Logger(filename="temp2",logger_user='2')
    log2 = l2.get_logger()

    res = methods(NewRotatingFileHandler)
    print("------------------------------result is",res)
    # log.debug("This is a debug message ")
    # log.info("This is a info message ")
    # log.warning("This is a warning message ")
    # log.error("This is a error message ")
    log2.error("Writing in temp2 file")


    for i in range(0,1000):
      log2.error("Writing in temp2 file")


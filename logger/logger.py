import logging
from datetime import datetime


class Logger:
    def __init__(self, file_handler_level = logging.DEBUG,stream_handler_level = logging.WARNING,
                 filename="log",filemode="a",logger_user = __name__,
                 console_output_flag =1,file_output_flag =1,
                 format="""%(asctime)s %(levelname)s %(lineno)s %(message)s """, datefmt="""%d %b %y %H:%M:%S """):


        self.logger = logging.getLogger(logger_user)
        self.logger.setLevel(logging.DEBUG)
        self.filename = '{}_{}.log'.format(filename,datetime.now().strftime("%d-%m-%Y"))
        self.stream_handler_level = stream_handler_level
        self.file_handler_level = file_handler_level
        self.format = format
        self.datefmt = datefmt
        self.console_output_flag = console_output_flag  # if console_output_flag set to 1 will print to console also
        self.file_output_flag = file_output_flag
        print("Temp: Log Handler: {} Log Level {}".format(self.logger.handlers, self.logger.level))
        self.create_handler()
        print("Temp: After adding handler Log Handler: {} Log Level {}".format(self.logger.handlers, self.logger.level))

        #logging.basicConfig(level=level,filename=filename,filemode=filemode,format=format)


    def create_handler(self):
        # Create handlers
        c_handler = logging.StreamHandler() #stream handler writes to console
        f_handler = logging.FileHandler(self.filename) #file handler writes to file
        print("TEMP before setting level C_HANDLER LEVEL {} F_HANDLER LEVEL {}".format(c_handler.level, f_handler.level))
        # c_handler.setLevel(self.stream_handler_level)
        # f_handler.setLevel(self.file_handler_level)
        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.DEBUG)
        print("TEMP C_HANDLER LEVEL {} F_HANDLER LEVEL {}".format(c_handler.level,f_handler.level))
        # Create formatters and add it to handlers
        c_format = logging.Formatter(self.format,self.datefmt)
        f_format = logging.Formatter(self.format,self.datefmt)
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        if self.file_output_flag == 1:
            self.logger.addHandler(f_handler)
        if self.console_output_flag ==1:
            self.logger.addHandler(c_handler)

        self.logger.info("Temp: Inside create handler: This is a debug message")
    def get_logger(self):
        return self.logger


if __name__ == "__main__":
    l1 = Logger()
    log = l1.get_logger()
    log.error("This is a error message ")
    log.warning("This is a warning message")
    log.info("THis is a info message")
    log.info("This is a debug message")

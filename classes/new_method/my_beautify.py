'''
Own module for formatting and other stuff

ref : link for implementiing class in own module : https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
#escape character issue : ref link 2 : https://stackoverflow.com/questions/25146960/python-convert-back-slashes-to-forward-slashes/25147093

for getting name of the object passed please refer to following link : https://docs.python.org/3.3/library/inspect.html
and create it using inspect module i guess
''' 
import os
import inspect
import logger

l1 = logger.Logger(format ="""%(asctime)s: %(message)s""",datefmt="""%d %b %y %H:%M:%S """)
log = l1.get_logger()
#log.error("Website Initializing.........")

#
#  #prints start of execution of function
# def fname_print(message):  # function name print
#     print("===============================================")
#     print("Executing {}:".format(message))


#
#  #prints start of execution of function v 2.0
# def fname_print(message,caller_file_name=None,function_caller=None):  # function name print
#   if caller_file_name ==None and function_caller==None:
#       print("===============================================")
#       print("Executing {}:".format(message,caller_file_name,function_caller))
#   elif function_caller==None and caller_file_name != None:
#       print("===============================================")
#       print("Executing: {} | Caller_filename: {}".format(message, caller_file_name, function_caller))
#   else:
#       print("===============================================")
#       print("Executing {} Caller_filename: {} Function_caller: {}".format(message, caller_file_name, function_caller))

def fname_print(message,caller_file_name=None,function_caller=None):
    pass


def details(stack,on_flag=1):
    if on_flag ==1:
        stack = stack
        current_func = stack[0].function #stack[0][0].f_code.co_name
        if "self" in stack[0][0].f_locals: #checking if function in class or direct
            current_class = stack[0][0].f_locals["self"].__class__.__name__
        else:
            current_class = "None"

        current_func_lineno = stack[0].lineno

        head, tail = os.path.split(stack[0].filename) # as was getting ful path spliting the file name
        current_filename = tail


        caller_func = stack[1][0].f_code.co_name

        if "self" in stack[1][0].f_locals:
            caller_class = stack[1][0].f_locals["self"].__class__.__name__
        else:
            caller_class = "None"
        caller_func_lineno = stack[1].lineno
        head, tail =os.path.split(stack[1].filename)
        caller_filename = tail
        print("_____________________________________________________________________________________________")
        #print("---------------------------------------------------------------------------------------------")
        #print("=============================================================================================")
        #print("Executing {}() {} - {} {}-->Caller {}() {} - {} {} ".format(current_func,current_func_lineno,current_class,current_filename, caller_func,caller_func_lineno,caller_class,caller_filename))
        str1 = "Executing [{}() {} - {} {}]".format(current_func,current_func_lineno,current_class,current_filename)
        str2 = "Caller [{}() {} - {} {}] ".format(caller_func,caller_func_lineno,caller_class,caller_filename)

        #print('%-65s | %-65s' % (str1, str2)) # '-' for left align, 65 total space given, 's for string'

        str3 = '%-65s | %-65s' % (str1, str2)
        log.error("_____________________________________________________________________________________________")
        log.error(str3)

        ######print("{}-->{}".format(str2,str1))
        #len(str1)
        #print("{} {}".format(str1,str2.rjust(100-len(str1),'-')))
        #print("length is :",len(str1))
        ###print('%-50s%-12s' % (str1, str2)
        # print("L {:^20} R".format(str1))
        # # Example 1
        # print('L {:<20} R'.format('x'))
        # # Example 2
        # print('L {:^20} R'.format('x'))
        # # Example 3
        # print('L {:>20} R'.format('x'))


    #print(str1.rjust(40,'+'))
def log_print(message=None,variable_name=None,variable=None,log_flag=1,variable_type=1):  # log print
    if log_flag ==1: #Function print switch default yes
        if message ==None:
            if variable_type==1: #Type switch default yes
                print("log: Variable output for {0}: {1}            Type is : {2}".format(variable_name,variable,type(variable)))
            else:
                print("log: Variable output for {0}: {1}".format(variable_name,variable))

        elif variable_name == None:
            print("log: {0}".format(message))
        else:
            print("log: {0}: Variable output for {1}: {2}".format(message,variable_name,variable))


def windows_path_convertor(dir):    #note path should be passed as a raw string for now

    log_print("Before conversion","dir",dir)
    dir = dir.replace(os.sep,"/")
    log_print("Before conversion","dir",dir)

    return dir
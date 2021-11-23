"""
Connecting to database using context manager

"""
#
# class DatabaseConnect():
#     def __init__(self,file_name): #file_name = database fie
#         print("DatabaseConnect class Init method Called")
#         self.file_name = file_name
#
#     def __enter__(self):
#         print("DatabaseConnect class enter method called")
#
#
#     def __exit__(self,type,value,traceback):
#         print("DatabaseConnect Exit Method called")
#
#
#
#
# with DatabaseConnect(file_name="demo.txt") as conn:
#     print("---")
#
#
#
# #output:
# # DatabaseConnect class Init method Called
# # DatabaseConnect class enter method called
# # ---
# # DatabaseConnect Exit Method called


class DatabaseConnect():
    def __init__(self,file_name):
        print("DatabaseConnect class Init method Called")
        self.file_name = file_name

    def __enter__(self):
        print("DatabaseConnect class enter method called")


    def __exit__(self,type,value,traceback):
        print("DatabaseConnect Exit Method called")




with DatabaseConnect(file_name="demo.txt") as conn:
    print("---")




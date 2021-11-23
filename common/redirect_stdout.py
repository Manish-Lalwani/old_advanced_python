"""
Redirecting Stdout (uses we can get the print statement on console to a variable like in case)

ref link: https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement
"""


import io,sys

old_stdout = sys.stdout # saving the original stdout to the variable
new_stdout = io.StringIO() # new stdout
sys.stdout = new_stdout # assigning the original stdout to new stdout so that we can get the output in an variable instead of console

str1 = "print('This is a test')"
exec(str1) # executing the string as an python statement with the help of exec command
exec_output = sys.stdout.getvalue().strip() # getting the exec command output which is stored and not printed to console as we have reassigned the stdout to new stdout
sys.stdout = old_stdout #setting stdout as the original so that the next print statement is printed on console
print(f"exec_output is {exec_output}")





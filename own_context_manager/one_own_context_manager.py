"""
context manager are used for manageing resources in python like database and file

ref : https://www.geeksforgeeks.org/context-manager-in-python/#:~:text=Python%20provides%20an%20easy%20way,or%20functions(with%20decorators).

ref : https://book.pythontips.com/en/latest/context_managers.html
"""


#open() example

data = "this is a string"
with open("example.txt","w") as fp:
	fp.write(data)
with open("example.txt") as fp:
	data = fp.read()

print(data)


#for a class to be a context manager at least 2 method enter and exit should be there
class FileOpen:
	def __init__(self,file_name,write_method):
		self.file_obj = open(file_name,write_method)

	def __enter__(self):
		print("Executing Enter Method")
		return self.file_obj

	def __exit__(self,type,value,traceback):
		print("Executing Exit Method")
		print(f"type is:{type},value is:{value},traceback is:{traceback}")
		self.file_obj.close()


print("Writing to file using context manager")
with FileOpen(file_name='demo.txt',write_method='w') as fp:
	fp.write("Have written this string using own context manager")


print("Reading to a file using context manager")
with FileOpen(file_name='demo.txt',write_method='r') as fp:
	data = fp.read()


print(data)



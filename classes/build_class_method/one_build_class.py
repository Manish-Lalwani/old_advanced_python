"""
__build_class__ is a dunder method which is executed while a class is created
"""



class Demo:
	def __new__(cls):
		print("new method executed")

	def __init__(self):
		print("init method executed")

	def __call__(self):
		print("call method called")


"""
James Powell: So you want to be a Python expert? | PyData Seattle 2017

ref link: 	https://www.youtube.com/watch?v=cKPlPJyQrt4&ab_channel=PyData

Generators

ALso : difference between generator and iterator
"""

#generator


#for creating a generator ,iter and next method are needed(compulsory)
class GeneratorSyntax:
	def __iter__(self):
		pass
	def __next__(self):
		pass


class DemoGenerator:
	def __init__(self):
		print("init method called")
	
	def __iter__(self):
		print("iter method called")
		self.value = 0

	def __next__(self):
		print("iter method called")
		current_val = self.value

		if self.value > 10:
			raise StopIteration()

		self.value +=1
		sleep(0.5)
		return current_val



if __name__ == '__main__':
	for x in DemoGenerator():
		print(x)
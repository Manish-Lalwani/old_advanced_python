"""
Printing class details using exec function()
ref link for exec: https://www.geeksforgeeks.org/execute-string-code-python/
"""

import io,sys
import time





class A:
	def __init__(self,num1):
		self.num1 = num1


	def print_class_details(self):
			print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			results = [] 
			old_stdout = sys.stdout # saving the original stdout to the variable
			new_stdout = io.StringIO() # new stdout
			sys.stdout = new_stdout # assigning the original stdout to new stdout so that we can get the output in an variable instead of console
			#print("Class details are as follows")
			dunder_function_list = dir(self) # getting all dunder function names
			i = 0
			for x in dunder_function_list:
				try:
					i +=1
					sys.stdout.write("None")
					exec_output = None
					time.sleep(2)
					sys.stdout = old_stdout
					print(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% New  Iteration {i}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
					str1 ="print(self." + str(x) + ")" #getting self.x as string representation as if we directly print self.x it directly searches for attribute x and gives error that attribute x not found
					sys.stdout = old_stdout
					print(str1[6:-1]) #printing converting string representation just for understanding (have excluded the print function)
					sys.stdout = new_stdout
					exec(str1) #executing string the string will get executed as normal python statement
					exec_output = sys.stdout.getvalue().strip() # getting the exec command output which is stored and not printed to console as we have reassigned the stdout to new stdout
					sys.stdout = old_stdout #setting stdout as the original so that the next print statement is printed on console
					print("@@@@@" + exec_output+ "@@@@@")
					#print(str1)
					#sys.stdout = new_stdout
					if "method" in exec_output:
						print("********************************")
						print("inside method if")
						str1 = str1[:-1] + '()' + ')'
						print("#####",str1)
						sys.stdout = old_stdout
						exec(str1)
						exec_output = sys.stdout.getvalue().strip()
						sys.stdout = old_stdout
						print("222")
						print(exec_output)
						#exec_output = sys.stdout.getvalue().strip()
					else:
						print("inside else method")
					results.append(exec_output)
					print("---------------------------------------------------------")
					sys.stdout = new_stdout
					sys.stdout.write("\n\n\n")
					exec_output = None
					time.sleep(5)
				except Exception as e:
					print("^^^^^^^^^^^^^^^^^^^^",e)
					continue




if __name__ == "__main__":
	obj1 = A(num1=5)
	obj1.print_class_details()

# THIS IS A TEST FILE.
# THESE COMMENTS, AS WELL AS ALL UNUSED FUNCTIONS/CLASSES SHOULD BE REMOVED.

def func(x):
	"""This function is kinda useless."""
	return x

def func2(x):
	'''DOCSTRING, YEAH'''
	return 5

# func2 should be removed, as it won't be used.

class Real:
	isReal = True
	# func2 = 5
	# ^ For extra challenge later.

	def __init__(self,x,y):
		self.x = x
		self.y = func(y)

	def remove_this_method(self):
		print("This method does nothing of significance.")

class Fake:
	isReal = False
	# func2 = 5

	def __init__(self,x,y):
		self.x = x
		self.y = func(y)

	def remove_this_method(self):
		print("This method does nothing of significance.")


print( func(6) , func(6),func(6))
x = Real(0,5)
print( x.isReal )
class Parent():
	""" This is inheritance example """

	def __init__(self,l_neme,eye):
		print('Parent Constructor Called')
		self.last_name = l_neme
		self.eye_color = eye 

class Child(Parent): # here was my error 
	""" This is the class whom inheritance from its Parent"""
	def __init__(self,l_neme,eye,num):
		print ('Child Constructor Called')
		Parent.__init__(self,l_neme,eye)
		self.num = num

rash = Child('Kh','gray',7)
print(rash.last_name)
print(rash.num)


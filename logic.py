class logic():
	def __init__(self,v, a, b):
		self.value=v
		self.mean=a
		self.range=b

	def getFuzz(self,z,index):
		# Last equation
		a=self.mean
		b=self.range
		if index == -1:
			if 	a-b <= z <= a:
				return 1 - (a-z)/b
			elif z < a-b:
				return 0
			else :
				return 1

		elif index == 0:
			if z <= a:
				return 1
			elif z >= a+b:
				return 0
			else:
				return 1-(a+b-z)/a

		else:
			if a-b <= z <= a:
				return 1-(a-z)/b
			elif a <= z <= a+b:
				return 1 - (z-a)/b
			else:
				return 0
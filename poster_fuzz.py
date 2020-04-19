import numpy as np
import logic

class fuzzy_logic():
	def __init__(self):
		self.logics=[]

	def getLogicValueList(self):
		return np.array([self.logics[i].value for i in np.arange(0,len(self.logics))]).astype("uint8")

	def addLogic(self,value,a,b):
		self.logics.append(logic.logic(value,a,b))

	def classify(self,value):
		v_logic=[]
		value_list=self.getLogicValueList()
		length=len(self.logics)

		for i in xrange(0,length-1):
			v_logic.append(self.logics[i].getFuzz(value,i))
		v_logic.append(self.logics[-1].getFuzz(value,-1))

		den=0
		num=0
		for i in xrange(0,length):
			num+=(v_logic[i]*value_list[i])
			den+=v_logic[i]

		#perform Classification
		expected_value=num/den;
		return value_list[min(range(len(value_list)), key = lambda i: abs(value_list[i]-expected_value))]
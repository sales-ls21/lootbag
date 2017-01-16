class Bag(object):

	def __init__(self):
		self.toys = dict()

	def addToy(self, name, toy):
		self.toys.update({name: toy})
		return self.toys

	def getToys(self):
		return self.toys

	def removeToy(self, name, toy):
		self.toys[name].remove(toy)

	def listKidsWhoGetToys(self):
		kidsName = list()
		for (k,v) in self.toys.items():
			kidsName.append(k)
		return kidsName

	def getAllToysForChild(self, name):
		return self.toys[name]

	def isDelivered(self, name, status):
		self.toys[name].update({status})
		return self.toys
			


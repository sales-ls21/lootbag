import sys
import sqlite3

class Bag(object):

	def __init__(self):
		self.toys = dict()

	def addToy(self, name, toy, delivered):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

			try: 
				c.execute("INSERT INTO CHILD VALUES (?,?,?)", (None, name, delivered))
			except sqlite3.OperationalError:
				pass

			c.execute("SELECT ChildId FROM Child WHERE Name='{}'".format(name))
			ID = c.fetchall()[0][0]
			print(ID)
			try:
				c.execute("INSERT INTO TOY VALUES(?, ?, ?)", (None, toy, ID))
			except sqlite3.OperationalError:
				pass

	def getToys(self):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

			try:
				c.execute("SELECT Name FROM Toy")
				names = c.fetchall()
				print(names)

	def removeToy(self, toy, name):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

			c.execute("SELECT ChildId FROM Child WHERE Name='{}'".format(name))
			child = c.fetchall()[0][0]

			try: 
				c.execute("DELETE FROM TOY WHERE CHILDID = {} AND NAME = '{}'".format(child, toy))
			except sqlite3.OperationalError:
				pass

	def listKidsWhoGetToys(self):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

			try:
				c.execute("SELECT Name FROM Child")
				names = c.fetchall()
				print(names)
		
	def getAllToysForChild(self, name):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

		c.execute("""SELECT t.Name FROM Toy t, Child c WHERE c.Name='{}' AND c.ChildId = t.Child""".format(name))
		toys = c.fetchall()
		print(toys)

	def isDelivered(self, name):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()
		c.execute("SELECT c.delivered from child c where c.name = '{}'".format(name))
		toys_delivered = c.fetchall()
		print(toys_delivered)
			

if __name__ == '__main__':
	lootbag = Bag()
	if sys.argv[1] == "add":
		lootbag.addToy(sys.argv[2], sys.argv[3], sys.argv[4])
	elif sys.argv[1] == "remove":
		lootbag.removeToy(sys.argv[2], sys.argv[3])
	elif sys.argv[1] == "ls":
		lootbag.getAllToysForChild(sys.argv[2])
	elif sys.argv[1] == "delivered":
		lootbag.isDelivered(sys.argv[2])
	elif sys.argv[1] == "show":
		lootbag.listKidsWhoGetToys()
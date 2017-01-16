import unittest
from bag import *


class testLootbag(unittest.TestCase):

	def test_isInstanceOfBag(self):
		lootbag = Bag()
		self.assertIsInstance(lootbag, Bag)

	def test_itemInBag(self):
		lootbag = Bag()
		lootbag.addToy("bryce", {"yo-yo", "bike", "water gun"})
		self.assertIn("yo-yo", lootbag.toys["bryce"])

	def test_removeItemFromBag(self):
		lootbag = Bag()
		lootbag.addToy("bryce", {"yo-yo", "bike", "water gun"})
		lootbag.removeToy("bryce", "bike")
		self.assertNotIn("bryce", lootbag.toys["bryce"])

	def test_listAllKids(self):
		lootbag = Bag()
		lootbag.addToy("tanya", {"bike", "pony", "book"})
		lootbag.addToy("mike", {"basketball", "shoes", "socks"})
		lootbag.addToy("rachel", {"pogo stick", "puppy", "video game"})
		lootbag.listKidsWhoGetToys()
		self.assertIn("mike", lootbag.listKidsWhoGetToys())

	def test_listAllSpecificChildToys(self):
		lootbag = Bag()
		lootbag.addToy("tanya", {"bike", "pony", "book"})
		lootbag.addToy("mike", {"basketball", "shoes", "socks"})
		lootbag.addToy("rachel", {"pogo stick", "puppy", "video game"})
		lootbag.getAllToysForChild("tanya")
		self.assertGreater(len(lootbag.getAllToysForChild("rachel")), 0)
		

	def test_addDeliveredProperty(self):
		lootbag = Bag()
		lootbag.addToy("tanya", {"bike", "pony", "book"})
		lootbag.addToy("mike", {"basketball", "shoes", "socks"})
		lootbag.addToy("rachel", {"pogo stick", "puppy", "video game"})		
		lootbag.isDelivered("tanya", "delivered")
		self.assertIn("delivered", lootbag.getAllToysForChild("tanya"))
		
if __name__ == '__main__':
    unittest.main()
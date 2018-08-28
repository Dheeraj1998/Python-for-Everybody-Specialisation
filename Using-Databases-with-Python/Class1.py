class PartyAnimal:
	x = 0
	
	def party(self):
		self.x = self.x + 1
		print("Value of x : ",self.x)
	

Human = PartyAnimal()
Human.party()
Human.party()
Human.party()

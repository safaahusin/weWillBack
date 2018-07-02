import pygame
class Car:
	def __init__(self ,DIS,photo,width,height,x,y,step):
		pygame.init()
		self.photo = pygame.image.load(photo)
		self.x = x
		self.y = y
		self.step = step
		self.DIS = DIS
		self.screenx = width
		self.screeny = height
	
	def getX(self):
		return self.x
		
	
	def getY(self):
		return self.y
		
	
	def getPhoto(self):
		return self.photo
		
	def carRun(self):
		self.carHitBound()
		self.x +=self.step
	
	def carHitBound(self):
		if self.x >= self.screenx - 50:
			self.x = 0
		if self.x < 0:
			self.x = self.screenx-200

	def manHitcar(self,man):
		return set(range(man.getX(),man.getX()+86)) & set(range(self.getX(),self.getX()+160))  and  set(range(man.getY(),man.getY()+94)) & set(range(self.getY(),self.getY()+84))

import pygame
step = 60
class Man: 
	def __init__(self,width,height,photo):
		pygame.init()
		self.flag = True
		self.width = width
		self.height = height
		self.x = width/2-100
		self.y = height - 150
		self.photo = pygame.image.load(photo)
		
	def closeManRun(self):
		self.flag = False
		
	def getPhoto(self):
		return self.photo
		
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	def changeX(self ,step):
		self.x +=step
		print 'manx',self.x	
	def changeY(self,step):
		self.y +=step
		print 'many',self.y		
	def IsHitBoundLeft(self ,x ):
		return x == 0
		
	def IsHitBoundRight(self ):
		return self.x == 1000 + (width-1000)/2
			
	def IsHitBoundBottom(self):
		return self.y >= height/2+100
		
	def Reset(self):
		self.y =self.height - 150
		self.x =self.width/2-100
			
	def manHitLeft(self):
		return self.x <= 0
	
	def manHitRight(self):
		return self.x >= self.width	-100	
			
	def manHitbottom(self):
		return self.y >=self.height-200
		
	def manHitTop(self):
		return self.y <=0
		
	def manPass (self):
		return set(range(self.getX(),self.getX()+86)) & set(range(700,820))  and  set(range(self.getY(),self.getY()+94)) & set(range(-30,90))
	def manRun(self):
		while self.flag:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.flag = False
					break
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						if not self.manHitbottom():
							self.changeY(step)
						

					if event.key == pygame.K_UP:
						if not self.manHitTop():
							self.changeY(-1*step)
						
					if event.key == pygame.K_RIGHT:
						if not self.manHitRight():	
							self.changeX(step)
						

					if event.key == pygame.K_LEFT:
						if not self.manHitLeft():
							self.changeX(-1*step)
						

import pygame,time

class Congratulation():
	def __init__(self,Heart,w,h):
		self.Score = Heart*100
		pygame.init()
		pygame.font.init()
		self.x = w
		self.y = h
		global Text
		Text = pygame.font.SysFont("None",70)
		Text2 = pygame.font.SysFont("None",45)
		print 'yes1'
		self.DIS = pygame.display.set_mode((1600,900),pygame.RESIZABLE,32)
		print 'yes2'
		self.DIS.blit(pygame.image.load("Road.png"),(0,0))
		print 'yes3'
		self.DIS.blit(Text.render("CONGRATULATION" , True,(255,255,255)), (self.x/2-200,self.y/2))
		print 'yes4'
		self.DIS.blit(Text2.render("Score : " + str(self.Score) , True, (255,255,255)), (self.x/2-100,self.y/2+100))
		print 'yes5'
		pygame.display.update()


#c = Congratulation(10,1600,900)

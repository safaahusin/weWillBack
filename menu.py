import pygame , sys ,mainFrame,time ,random,high_score,AboutUs

import story,option,saveName


menuList = ["     Start",
			"High Score",
			"  Options",
			"    Story",
			"    About",
			"     Exit"]
class Menu (mainFrame.MainFrame):
	global Text
	pygame.font.init()
	Text = pygame.font.SysFont("None",60)
	def __init__(self):
		self.mm = mainFrame.MainFrame()
		mainFrame.MainFrame.check=False
		
	def writeMenuList(self):
		k=0
		for i in menuList:
			self.mm.DIS.blit(Text.render(i, True, (0,0,0)), (500,100+100*k))#positions (700,100) (700,200)...
			k+=1
			pygame.display.update()
	def start(self):
		s=saveName.saveName()
	def high_Score(self):
		 high=high_score.HighScore()
		 high.Run()
	def options(self):
		op=option.Scale_Test()
	 
	def fun_story(slef):
		s=story.story()
	def about(self):
		ab=AboutUs.About_Design()
		ab.Run()
	def exitt(self):
		sys.exit()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def menuRun(self):
		self.writeMenuList()
		bg = pygame.image.load('haba.jpg')
			#pygame.draw.rect(m.mm.DIS,(0,0,0),(690,90,140,60),4)
		i=-1
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						i-=1
						if i > 5 or i < 0:
							i=0
						self.mm.DIS.blit(bg,(0,0))
						self.writeMenuList()
						pygame.draw.rect(self.mm.DIS,(255,255,255),(490,90+100*i,270,60),4)
							#print i , 90+100*i
					if event.key == pygame.K_DOWN:
						i+=1
						if i > 5 or i < 0:
							i=0
						self.mm.DIS.blit(bg,(0,0))
						self.writeMenuList()
						pygame.draw.rect(self.mm.DIS,(255,255,255),(490,90+100*i,270,60),4)
							#print i , 90+100*i
					if event.key == pygame.K_RETURN:
						if i == 0:
							self.start()
						elif i == 1:
							self.high_Score()
						elif i == 2:
							self.options()
						elif i == 3:
							self.fun_story()
						elif i == 4:
							self.about()
						elif i == 5:
							self.exitt()
						
					pygame.display.update()
			

"""if __name__ == '__main__':
	obj = Menu()
	obj.menuRun()
"""

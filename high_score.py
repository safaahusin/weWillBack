import mainFrame ,pygame ,sys , menu
import file_module
pygame.font.init()

class HighScore (mainFrame.MainFrame):
	global Text
	Text = pygame.font.SysFont("None",50)
	pygame.init()
	#DIS = pygame.display.set_mode((1400,900),pygame.RESIZABLE,32)
	def __init__ (self):
		self.frame = mainFrame.MainFrame()
	def write(self):
		myfile=file_module.MyFile()
		l=myfile.readhighScore()
		k=2 #238,232,190
		self.frame.DIS.blit(Text.render("High  * *  Score" , True,(0,0,128)), (500,60))	
		self.frame.DIS.blit(Text.render("__________________" , True, (238,232,190)), (450,80))
		self.frame.DIS.blit(Text.render("Name :-" , True, (178,34,34)), (100,150))#positions (700,100) (700,200)...
		self.frame.DIS.blit(Text.render("Score *" , True, (178,34,34)), (550,150))
		self.frame.DIS.blit(Text.render("LeveL *", True,(178,34,34)), (900,150))
		if(len(l)!=0):
			for i in l:
				i[2] = i[2][:-1]
				self.frame.DIS.blit(Text.render(i[0] , True, (0,0,0)), (100,110+60*k))#positions (700,100) (700,200)...
				self.frame.DIS.blit(Text.render(i[1]+" $", True, (0,0,0)), (550,110+60*k))
				self.frame.DIS.blit(Text.render(i[2] , True, (0,0,0)), (900,110+60*k))
				k+=1
				pygame.display.update()
		else:
			self.frame.DIS.blit(Text.render("__" , True, (0,0,0)), (100,110+60*2))#positions (700,100) (700,200)...
			self.frame.DIS.blit(Text.render("__", True, (0,0,0)), (550,110+60*2))
			self.frame.DIS.blit(Text.render("__" , True, (0,0,0)), (900,100+60*2))
			
		pygame.draw.rect(self.frame.DIS,(0,0,0),(100,590,140,60),4)
		self.frame.DIS.blit(Text.render("Back" , True, (0,0,0)), (120,600))
		
	def Run(self):
		self.write()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
						new = menu.Menu()
						new.menuRun()
			pygame.display.update()

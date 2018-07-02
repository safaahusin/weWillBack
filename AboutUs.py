import mainFrame ,pygame ,sys , menu 
#pygame.font.init()

class About_Design (mainFrame.MainFrame):
	global Text
	Text = pygame.font.SysFont("None",45)
	pygame.init()
	DIS = pygame.display.set_mode((1600,900),pygame.RESIZABLE,32)
	def __init__ (self):
		self.frame = mainFrame.MainFrame()
	def about(self):
		self.frame.DIS.blit(Text.render("About  * *  US" , True,(210,105,30)), (500,60))
		self.frame.DIS.blit(Text.render("_________________" , True, (238,232,190)), (450,80))
		self.frame.DIS.blit(Text.render("Programmer By :-" , True, (178,34,34)), (100,200))#positions (700,100) (700,200)...
		self.frame.DIS.blit(Text.render("* Safaa El-Shafe'y" , True, (0,0,0)), (150,260))
		self.frame.DIS.blit(Text.render("* Heba Mostafa ", True,(0,0,0)), (150,320))
		self.frame.DIS.blit(Text.render("* Esraa Mohammed ", True, (0,0,0)), (150,380))
		self.frame.DIS.blit(Text.render("- Faculty of Computer Science , Helwan Uni ...", True, 	(0,0,128)), (100,440))
		self.frame.DIS.blit(Text.render("- Using Python Language ^__^", True, (0,0,128)), (100,500))
		#self.frame.DIS.blit(Text.render("Wait Our Next Game ^__^ ", True, (	188,143,143)), (420,560))
		pygame.draw.rect(self.frame.DIS,(0,0,0),(100,590,140,60),4)
		self.frame.DIS.blit(Text.render("Back" , True, (0,0,0)), (120,600))

	def Run(self):
		self.about()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
						new = menu.Menu()
						new.menuRun()
			pygame.display.update()
	
"""
ab=About_Design()
ab.Run()

"""

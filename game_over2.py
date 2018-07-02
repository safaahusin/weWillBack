import pygame,thread,music,menu,sys,time
import mainFrame

class gameOver():
	
	Text = pygame.font.SysFont("None",45)
	
	def __init__(self):
		
		pygame.init()
		
		self.bg = pygame.image.load('game-over.jpg')
		self.sizeScreenX=1300
		self.sizeScreenY=900
		self.screen=pygame.display.set_mode((self.sizeScreenX,self.sizeScreenY))
		#music.stop()
		#thread.start_new_thread(music.playSong,('Resident Evil 4 Soundtrack - Game Over.mp3',))
		#title_arabic=u'\uFEB3\uFEE8\uFECC\uFEEE\uFEA9'.encode('utf8')
		#pygame.display.set_caption(title_arabic)
		
		
		while(True):
			self.screen.fill((0,0,0))
			
			self.screen.blit(self.bg,(100,80))
			
			#pygame.draw.rect(self.screen,(255,255,255),(100,590,140,60),4)
			#self.screen.blit(self.Text.render("Back" , True, (255,255,255)), (120,600))
			pygame.display.update()
			self.Action()
			

		
	def Action(self):
		time.sleep(5)
		new = menu.Menu()
		new.menuRun()
		mainFrame.MainFrame.check=False
		pygame.display.update()
		'''for event in pygame.event.get():
			print 'Action'
			if(event.type==pygame.QUIT):
				sys.exit()
				pygame.quit()
				#music.stop()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
					new = menu.Menu()
					new.menuRun()
					mainFrame.MainFrame.check=False'''
				
				
		
g=gameOver()

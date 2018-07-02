import pygame,sys ,music,thread


class theEnd():
	
	pygame.font.init()
	Text = pygame.font.SysFont("None",60)
	sizeScreenX=1300
	sizeScreenY=900
	screen=pygame.display.set_mode((sizeScreenX,sizeScreenY))
	
	def __init__(self):
		#if(level=="Phalsten         "):
		music.stop()
		thread.start_new_thread(music.playSong,('fin.mp3',))
		title_arabic=u'\uFEB3\uFEE8\uFECC\uFEEE\uFEA9'.encode('utf8')
		pygame.display.set_caption(title_arabic)
		bg1 = pygame.image.load('980arbe7.jpg')
		bg2 = pygame.image.load('980arbe7.jpg')
		"""bg3 = pygame.image.load('ff9860f7a7de5c47b1b097c3584b5556.jpg')
		bg4 = pygame.image.load('980arbe7.jpg') """
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				"""if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
						if(level=="Phalsten         "):
							p=phalsten.phlasten(inp)
						elif(level=="Egypt        "):
							c=CrossTheRoad.CrossTheRoad(inp)	
			if(level=="Phalsten         "):"""
			#self.screen.blit(bg1,(0,0))
			self.screen.fill((0,0,0))
			self.screen.blit(pygame.transform.scale(bg1, (1250, 650)),(20,25))
			#self.screen.blit(bg2,(200,50))
			#self.screen.blit(self.Text.render("", True, (255,255,255)), (150,150))
			#self.screen.blit(self.Text.render("Phalsten " , True, (0,0,0)), (150,400))
			pygame.display.update()
			
#theEnd()		
			
	
			



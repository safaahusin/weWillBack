import pygame,sys ,music,thread,phalsten,option,CrossTheRoad
import file_module

class intro_level():
	
	pygame.font.init()
	Text = pygame.font.SysFont("None",60)
	sizeScreenX=1300
	sizeScreenY=900
	screen=pygame.display.set_mode((sizeScreenX,sizeScreenY))
	
	def __init__(self,level,inp):
		#if(level=="Phalsten         "):
			#music.stop()
			#thread.start_new_thread(music.playSong,('Call of Duty 4 Modern Warfare OST - Game Over.mp3',))
		title_arabic=u'\uFEB3\uFEE8\uFECC\uFEEE\uFEA9'.encode('utf8')
		pygame.display.set_caption(title_arabic)
		bg = pygame.image.load('artsfon.com-28665.jpg')
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
					
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
						if(level=="Phalsten         "):
							p=phalsten.phlasten(inp)
						elif(level=="Egypt        "):
							c=CrossTheRoad.CrossTheRoad(inp)
							
							
			if(level=="Phalsten         "):
				self.screen.blit(bg,(0,0))
				self.screen.blit(self.Text.render("Last LeveL ... " , True, (255,255,255)), (150,150))
				self.screen.blit(self.Text.render("Phalsten " , True, (0,0,0)), (150,400))
			
			pygame.display.update()
			
			
#i=intro_level("Phalsten         ","safaa")		
			
	
			


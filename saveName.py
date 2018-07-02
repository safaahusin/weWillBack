import pygame,sys ,music,thread,inputbox,option
import file_module,intro_level,fun

class saveName():
	
	pygame.font.init()
	Text = pygame.font.SysFont("None",35)
	sizeScreenX=1300
	sizeScreenY=900
	screen=pygame.display.set_mode((sizeScreenX,sizeScreenY))
	inp=""
	def __init__(self):
		#music.stop()
		#thread.start_new_thread(music.playSong,('Call of Duty 4 Modern Warfare OST - Game Over.mp3',))
		title_arabic=u'\uFEB3\uFEE8\uFECC\uFEEE\uFEA9'.encode('utf8')
		pygame.display.set_caption(title_arabic)
		bg = pygame.image.load('haba.jpg')
		
		while True:			
			pygame.display.update()
			self.screen.blit(bg,(0,0))
			self.screen.blit(self.Text.render("Enter Your Name ... " , True, (0,0,0)), (200,300)) 
			self.screen.blit(self.Text.render("Welcome ^___^ " , True, (0,0,128)), (150,150))
			inp = str(inputbox.ask(self.screen, ''))
			if(not (inp =="")):
				f=file_module.MyFile()
				f.writeName(inp)
				option.Scale_Test.level
				fun.puzzle(option.Scale_Test.level,inp)
				#intro_level.intro_level(option.Scale_Test.level,inp)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()	
			
#save=saveName()	
			

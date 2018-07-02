import sys, pygame,music ,thread,menu,mainFrame
class story():	
	def __init__(self):
		pygame.init()
		size = width, height = 1600,900
		speed = [15,15]
		black = 0, 0, 0
		#thread.start_new_thread(music.playSong,('Dragon Lands.mp3',))
		screen = pygame.display.set_mode(size,0,8)
		pygame.display.set_caption("Story")#title
		bg = pygame.image.load('YourFastComputer_html_m43cccdaa.png')
		screen.blit(bg,(400,200))
		"""path="/home/mts2/Desktop/back_connect/image2/"
		image_list=['51413.jpg','Screenshot from 2016-08-29 14:52:12.png','a4233737338_10.jpg','Screenshot from 2016-08-29 14:39:10.png','Screenshot from 2016-08-29 14:37:16.png'
		,'indzex.jpeg','couple-under-night-sky-star-anime-love-art-desktop.jpg',
		'Screenshot from 2016-08-29 14:43:11.png','anime-background-scenery-school-anime-scenery-wallpaper-tumblr.jpg',
		'Screenshot from 2016-08-29 15:09:16.png','Screenshot from 2016-08-29 14:59:28.png',
		]
		ball = pygame.image.load(path+image_list[0])#to load image 
		ballrect = ball.get_rect()
		
		red=(255,0,0)
		screen.fill(black)
		i=0
		j=0"""
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
						#music.stop()
						new = menu.Menu()
						new.menuRun()
						#mainFrame.MainFrame.check=True
				"""ballrect = ballrect.move(speed)
				if ballrect.left < 0 or ballrect.right > width-10:
					speed[0] = -speed[0]
				if ballrect.top < 0 or ballrect.bottom > height-10:
					speed[1] = -speed[1]
      
				screen.fill(black)
				screen.blit(ball,ballrect)#ballrect to move
				if(j<20):
					j+=1
				else:
					j=0
					if(i<10):
						i+=1
					else:
						i=0
					ball = pygame.image.load(path+image_list[i])"""
				pygame.display.update()
				pygame.display.flip()
				""""if(i==9):
					sys.exit()
					new = menu.Menu()
					new.menuRun()"""

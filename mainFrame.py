import pygame , sys ,music ,thread
from Tkinter import *

class MainFrame:
	check=True
	def __init__(self):
		pygame.init()
		self.DIS = pygame.display.set_mode((1600,900),pygame.RESIZABLE,32) 
		bg = pygame.image.load('haba.jpg')#haba.jpg
		#img = pygame.image.load('running-man-xxl.png') 
		pygame.display.set_icon(bg)
		title_arabic=u'\uFEB3\uFEE8\uFECC\uFEEE\uFEA9'.encode('utf8')
		pygame.display.set_caption(title_arabic)
		#pygame.display.set_icon(img)
		if(self.check):
			self.call_music()
		self.DIS = pygame.display.set_mode((1600,900),pygame.RESIZABLE,32)
		self.DIS.blit(bg,(0,0))
		
	def call_music(self):
		
		thread.start_new_thread(music.playSong,('Call of Duty 4 Modern Warfare OST - Game Over.mp3',))
		#di-evantile_savage-law.mp3
		
	
		

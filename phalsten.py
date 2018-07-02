import pygame,sys,thread,time,random,music,game_over,file_module
import theEnd

class phlasten():
	
	pygame.init()
	Text = pygame.font.SysFont("None",70)
	sizeScreenX=1300
	sizeScreenY=900
	screen=pygame.display.set_mode((sizeScreenX,sizeScreenY))
	endSizeScreenX=sizeScreenX-350
	startSizeScreenX=40
	Text = pygame.font.SysFont("None",30)
	player_x=550
	player_y=550
	dirction_player="R"
	
	clock=pygame.time.Clock()
	
	bombRandX=[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
	flowerRandX=[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
	bombRandYChange=10
	flowerRandYChange=[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]
	Monsty=[1,1,1]
	MonstyY=15
	NumFollower=15
	NumBomb=3
	NumMonsty=3
	NumEvil=2
	NumTree=8
	
	move=30
	stepBomb=20
	stepFlower=25
	stepEvil=10
	stepMonsty=15
	
	level=10
	score=0
	total_score=0
	
	lastXbomb=0
	lastYbomb=0
	lastXflower=0
	lastYflower=0
	lastXEvil=0
	
	evilY=player_y
	evilX=[50,1100,1000]
	evilDirction=["R","L","L"]
	
	
	treeRandXChange=[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,
	15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]
	TreeYposition=360
	photoTree1=[1,2,3,4,0,5,6,4,0,1,2,3,4,6,5,2,3,4,0]
	photoTree2=[1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0]
	
	tree_design=[
	'icon-olive-tree-black.png',
	'ulSeelS.png',
	'07-512.png',
	'black-oak-tree-md.png',
	'tree-9-xxl.png',
	'173-200.png',
	'oak-tree-icon-png-30.png',
	'tree-10-xxl.png'
	]
	
	
	def draw_hero(self):
		man=pygame.image.load('b27c7c889e9256a844bcf282b98cedd7.gif')
		if(self.dirction_player=="R"):
			man=pygame.image.load('ken_masters_by_fjamesfernandez-d2nypbd.png')
			self.screen.blit(pygame.transform.scale(man, (100, 100)),(self.player_x,self.player_y))
		elif(self.dirction_player=="L"):
			man=pygame.image.load('b27c7c889e9256a844bcf282b98cedd7.gif')
			self.screen.blit(pygame.transform.scale(man, (120, 120)),(self.player_x,self.player_y))
			
	def turn_draw_dirc(self):
		if(self.player_x<self.startSizeScreenX):
			self.player_x=self.endSizeScreenX
		if(self.player_x>self.endSizeScreenX):
			self.player_x=self.startSizeScreenX
	
	
	def move_hero(self):
		for event in pygame.event.get():
			if(event.type==pygame.QUIT):
				music.stop()
				sys.exit()
				pygame.quit()
				
			if(event.type==pygame.KEYDOWN):
				if(event.key==pygame.K_LEFT):
					self.dirction_player="L"
					self.player_x-=self.move
					for i in range(self.NumTree):
						self.treeRandXChange[i]+=self.move
				if(event.key==pygame.K_RIGHT):
					self.dirction_player="R"
					self.player_x+=self.move
					for i in range(self.NumTree):
						self.treeRandXChange[i]-=self.move
				if (event.key==pygame.K_SPACE):
					self.kill_evil()
				"""if(event.key==pygame.K_UP):
					self.player_y-=self.move
				if(event.key==pygame.K_DOWN):
					self.player_y+=self.move
				if event.key == pygame.K_ESCAPE:
					print "escape"
				"""
	def generate_Monsty(self):
		for i in range(self.NumMonsty):
			self.Monsty[i]=random.randrange(20,self.sizeScreenX-100)
			self.MonstyY=self.stepMonsty
			
	def draw_Monsty(self):
		mon=pygame.image.load('h11-512.png')
		for i in range(self.NumMonsty):
			self.screen.blit(pygame.transform.scale(mon, (60, 60)), (self.Monsty[i],self.MonstyY))
				
	def generate_bomb(self):
		value=random.randrange(20,self.sizeScreenX-100)
		self.bombRandYChange=self.stepBomb
		return value
			
	
	def draw_bomb(self,value):
		self.screen.blit(pygame.transform.scale(self.bomb, (60, 60)), (value,self.bombRandYChange))
		
	def draw_group_bomb(self):
		for i in range(self.NumBomb):
			self.bombRandX[i]=self.generate_bomb()
			self.draw_bomb(self.bombRandX[i])
			
	def kill_bomb(self):
		for i in range(self.NumBomb):
			fire=pygame.image.load('6ipL5MdbT.png')
			if(self.bombRandX[i]>=self.player_x-20 and self.bombRandX[i]<=self.player_x+120):
				if(self.bombRandYChange>=self.player_y and self.bombRandYChange<=self.player_y+120):
					if(not (self.bombRandYChange==self.lastYbomb and self.bombRandX[i]==self.lastXbomb)):
						#self.screen.blit(pygame.transform.scale(fire, (500,500)),(self.bombRandX[i],self.bombRandYChange))
						self.screen.blit(pygame.transform.scale(fire,(500,500)),(300,200))
						self.lastYbomb=self.bombRandYChange+self.stepBomb
						self.lastXbomb=self.bombRandX[i]
						self.level-=1
						#pygame.time.wait(700)
						break
					else:
						self.lastYbomb+=self.stepBomb
						
	def draw_follower(self,value,index):
		if(index==0):
			self.screen.blit(pygame.transform.scale(self.flower_eat3, (50, 50)), (value,self.flowerRandYChange[index]))
		elif(index==1):
			self.screen.blit(pygame.transform.scale(self.flower_eat2, (50, 50)), (value,self.flowerRandYChange[index]))
		elif(index==2):
			self.screen.blit(pygame.transform.scale(self.flower_eat4, (50, 50)), (value,self.flowerRandYChange[index]))
		else:
			self.screen.blit(pygame.transform.scale(self.flower_eat1, (50, 50)), (value,self.flowerRandYChange[index]))
		
	def eat_follower(self):
		for i in range(self.NumBomb):
			if(self.flowerRandX[i]>=self.player_x-20 and self.flowerRandX[i]<=self.player_x+120):
				if(self.flowerRandYChange[i]>=self.player_y and self.flowerRandYChange[i]<=self.player_y+120):
					if(not(self.lastXflower==self.flowerRandX[i]and self.lastYflower==self.flowerRandYChange[i])):
						self.flowerRandX[i]=self.generate_follower(i)
						self.score+=1
						self.total_score+=1
						self.lastXflower=self.flowerRandX[i]
						self.lastYflower=self.flowerRandYChange[i]+self.stepFlower
						break
					else:
						self.lastYflower=self.flowerRandYChange[i]+self.stepFlower
					
	
	def draw_group_follower(self):
		for i in range(self.NumFollower):
			self.flowerRandX[i]=self.generate_follower(i)
			self.draw_follower(self.flowerRandX[i],i)
				
	def generate_follower(self,index):
		value=random.randrange(20,self.sizeScreenX-100)
		self.flowerRandYChange[index]=self.stepFlower
		return value
		
	def check_score(self):
		if(self.score+1%10==0):
			self.score=0
			self.level+=1
					
	def draw_heart(self):
		for i in range(self.level):
			self.screen.blit(self.heart,(30+(i*50),20))
			#print "heart"
			
	def draw_score(self):
		self.screen.blit(pygame.transform.scale(self.flower_score, (50, 50)), (1200,20))
		self.screen.blit(self.Text.render(str(self.score), True, (255,255,255)), (1150,30))
		
	def sucess(self):
		if(self.total_score==10):
			theEnd.theEnd()
				
	def generate_tree(self,index,dirc):
		#value=random.randrange(20,self.sizeScreenX-100)
		if(dirc==1):#right
			self.treeRandXChange[index]=350
		else:
			self.treeRandXChange[index]=1200
		self.photoTree1[index]=random.randrange(0,8)
		self.photoTree2[index]=random.randrange(0,8)
		"""
		else:
			if(dirc==1):#right
				self.treeRandXChange2[index]=1200
			else:
				self.treeRandXChange2[index]=20
			self.photoTree2[index]=random.randrange(0,5)
		"""
		#self.treeRandXChange2[index]=random.randrange(20,self.sizeScreenX-100)
			
	def draw_tree(self,index):
		tree=pygame.image.load(self.tree_design[self.photoTree1[index]])
		self.screen.blit(pygame.transform.scale(tree, (170, 170)),(self.treeRandXChange[index],self.TreeYposition))
		#tree=pygame.image.load(self.tree_design[self.photoTree2[index]])
		#self.screen.blit(pygame.transform.scale(tree, (170, 170)),(self.treeRandXChange[index],self.TreeYposition-130))
		
	def draw_first_tree(self):
		for i in range(self.NumTree):
			tree=pygame.image.load(self.tree_design[self.photoTree1[i]])
			self.treeRandXChange[i]=300+(i*130)
			self.screen.blit(pygame.transform.scale(tree, (170, 170)),(self.treeRandXChange[i],self.TreeYposition))
				
	def draw_evil(self,index):
		evil=pygame.image.load('4a6b77ae99a98d0d3a0a68a6b5491305.png')
		if(self.evilX[index]>self.player_x):
			evil=pygame.image.load('4a6b77ae99a98d0d3a0a68a6b5491305.png')	
		else:
			evil=pygame.image.load('Devil.png')			
		self.screen.blit(pygame.transform.scale(evil,(80,80)),(self.evilX[index],self.evilY))
		
	def draw_group_evil(self):
		for i in range(self.NumEvil):
			self.draw_evil(i)
			
	def generate_evil(self,index):
		value=random.randrange(20,self.sizeScreenX-100)
		if(value>self.player_x):
			if(self.dirction_player=="R"):
				self.evilDirction[index]="L"
			else:
				self.evilDirction[index]="R"				
		else:
			self.evilDirction[index]=self.dirction_player
		self.evilX[index]=value
			
	def kill_evil(self):
		#d18b063b4feba533c82bdb16ebd2e4fc_006608600 1331679479.jpeg
		flag=pygame.image.load('israel-flag-burn-fire-770x400.jpg')
		self.screen.blit(pygame.transform.scale(flag,(500,500)),(300,200))
		for i in range(self.NumEvil):
			if(self.evilDirction[i]==self.dirction_player):
				self.generate_evil(i)
				break
				
	def die_evil(self):
		for i in range(self.NumEvil):
			if(self.evilX[i]>=self.player_x-20 and self.evilX[i]<=self.player_x+120):
				if(not (self.evilX[i]==self.lastXEvil)):
					self.lastXEvil=self.evilX[i]+self.stepEvil
					self.level-=1
					self.generate_evil(i)
					break
				else:
					self.lastXEvil+=self.stepEvil

	def move_evil(self,index):
		if(self.evilX[index]>self.player_x):
			self.evilX[index]-=self.stepEvil
			if(self.dirction_player=="R"):
				self.evilDirction[index]="L"
			else:
				self.evilDirction[index]="R"				
		else:
			self.evilX[index]+=self.stepEvil
			self.evilDirction[index]=self.dirction_player
			

			
	def __init__(self,inp):
		
		#music.stop()
		#thread.start_new_thread(music.playSong,('Call of Duty 4 Modern Warfare OST - Game Over.mp3',))
		
		title_arabic=u'\uFEB3\uFEE8\uFECC\uFEEE\uFEA9'.encode('utf8')
		pygame.display.set_caption(title_arabic)
		bg = pygame.image.load('Sun-rising-good-morning.jpg')
		self.heart=pygame.image.load('life.png')
		self.bomb=pygame.image.load('clan-bomber-icon.png')
		self.flower_score=pygame.image.load('blooming-rose-flower-icon-1295.png')
		self.flower_eat1=pygame.image.load('rose.png')
		self.flower_eat2=pygame.image.load('description-textmateicon-png-31.png')
		self.flower_eat3=pygame.image.load('pvir78.png')
		self.flower_eat4=pygame.image.load('050251-blue-jelly-icon-natural-wonders-flower26-sc44.png')
		gameOver=True
		gameExit=True
		value=[1,2,3]
		self.draw_group_bomb()
		self.draw_group_follower()
		self.draw_first_tree()
		self.draw_group_evil()
		self.generate_Monsty()
		while gameExit:
			while gameOver==True:
				self.screen.fill((0,0,0))
				self.screen.blit(bg,(10,0))
				self.draw_heart()
				self.move_hero()
				self.draw_score()
				self.draw_Monsty()
				
				for i in range(self.NumTree):
					self.draw_tree(i)
					
				for i in range (self.NumBomb):
					self.draw_bomb(self.bombRandX[i])
					
				for i in range(self.NumFollower):
					self.flowerRandYChange[i]+=self.stepFlower
					
				for i in range (self.NumFollower):
					self.draw_follower(self.flowerRandX[i],i)
					
				self.draw_hero()
				self.draw_group_evil()
				for i in range(self.NumEvil):
					self.move_evil(i)
					
				self.turn_draw_dirc()
				
				self.kill_bomb()
				
				print self.level
				
				print self.score

				if(self.level==0):
					f=file_module.MyFile()
					f.writeScoreLevel(inp,self.score,"phalstenn")
					g=game_over.gameOver()
					
				self.eat_follower()
				
				self.bombRandYChange+=self.stepBomb
				self.MonstyY+=self.stepMonsty
				
				self.check_score()
				self.sucess()
				if(self.bombRandYChange>800):
					self.draw_group_bomb()
					
				if(self.MonstyY>800):
					self.generate_Monsty()
					
				for i in range(self.NumFollower):
					if(self.flowerRandYChange[i]>800):
						self.flowerRandX[i]=self.generate_follower(i)
						
				for i in range(self.NumTree):
					if(self.treeRandXChange[i]>1200): 
						self.generate_tree(i,1)
					if(self.treeRandXChange[i]<350 ):
						self.generate_tree(i,2)
				self.die_evil()	
				"""
				for i in range(self.NumEvil):
					if(self.NumEvil>=1):
						self.draw_evil("L",i)
					else:
						self.draw_evil("R",i)
				"""
					
				#self.clock.tick(0)#control time for change frame per second			
				pygame.display.update()
				
				
			
#p=phlasten("safaa")


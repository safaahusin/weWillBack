import random, pygame, sys,intro_level		
from pygame.locals import *	
from color import *
class puzzle:	
	FPS = 10 
	WINDOWWIDTH = 1340 
	WINDOWHEIGHT = 780 
	REVEALSPEED = 8 
	BOXSIZE = 90 
	GAPSIZE = 10 
	BOARDWIDTH = 4
	BOARDHEIGHT = 4 
	XMARGIN = (WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2		
	YMARGIN = (WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2
	check=False
	########################################################################
	def score(self):
		self.DISPLAYSURF.fill(BGCOLOR)
		emotion=pygame.image.load('clipart-thumbs-up-happy-smiley-emoticon-256x256-8595.png')
		self.DISPLAYSURF.blit(pygame.transform.scale(emotion, (100, 100)),(200,200))		
		self.DISPLAYSURF.blit(self.Text.render("Go Ahead Now" , True, (255,255,255)), (100,100))
		return True
		
	#########################################################################
	def getRandomizedBoard(self):	
		icons = []
		for color in ALLCOLORS:
			for shape in ALLSHAPES:
				icons.append( (shape, color) )
				
		random.shuffle(icons) 
		numIconsUsed = int(self.BOARDWIDTH * self.BOARDHEIGHT / 2) 
		icons = icons[:numIconsUsed] * 2 
		random.shuffle(icons)
		board = []
		
		for x in range(self.BOARDWIDTH):
			column = []	
			for y in range(self.BOARDHEIGHT):
				
				column.append(icons[0])
				del icons[0] 
			board.append(column)
		
		return board
	####################################################	
	def generateRevealedBoxesData(self,val):	
		revealedBoxes = []
		for i in range(self.BOARDWIDTH):
			revealedBoxes.append([val] * self.BOARDHEIGHT)
			
		return revealedBoxes	
	##################################################
	def splitIntoGroupsOf(self,groupSize, theList):
		result = []
		for i in range(0, len(theList), groupSize):
			result.append(theList[i:i + groupSize])
		return result	
	##################################################
	def leftTopCoordsOfBox(self,boxx, boxy):	
		left = boxx * (self.BOXSIZE + self.GAPSIZE) + self.XMARGIN	
		top = boxy * (self.BOXSIZE + self.GAPSIZE) + self.YMARGIN
		return (left, top)
    ##################################################
	
	def startGameAnimation(self,board):
		coveredBoxes = self.generateRevealedBoxesData(False)
		boxes = []
		for x in range(self.BOARDWIDTH):
			for y in range(self.BOARDHEIGHT):
				boxes.append( (x, y) )
		random.shuffle(boxes)
		boxGroups = self.splitIntoGroupsOf(7, boxes)
		self.drawBoard(board, coveredBoxes)
		#######################################
	def drawBoxCovers(self,board, boxes, coverage):
			for box in boxes:
				left, top = self.leftTopCoordsOfBox(box[0], box[1])
				pygame.draw.rect(self.DISPLAYSURF, BGCOLOR, (left, top, self.BOXSIZE, self.BOXSIZE))
				shape, color = self.getShapeAndColor(board, box[0], box[1])
				self.drawIcon(shape, color, box[0], box[1])
				if coverage > 0: 
					pygame.draw.rect(self.DISPLAYSURF,WHITE, (left, top, coverage, self.BOXSIZE))
			emotion=pygame.image.load('funny-icon-11.png')
			self.DISPLAYSURF.blit(pygame.transform.scale(emotion, (100, 100)),(200,200))		
			self.DISPLAYSURF.blit(self.Text.render("Play This At First" , True, (255,255,255)), (100,100))		
			pygame.display.update()
			

			self.FPSCLOCK.tick(self.FPS)
		##############################################
	def drawIcon(self,shape, color, boxx, boxy):	
		quarter = int(self.BOXSIZE * 0.25) 
		half = int(self.BOXSIZE * 0.5) 
		left, top = self.leftTopCoordsOfBox(boxx, boxy)
		if shape == DONUT:
			pygame.draw.circle(self.DISPLAYSURF, color, (left + half, top + half),half)
			
		elif shape == SQUARE:
			pygame.draw.rect(self.DISPLAYSURF, color, (left + quarter, top + quarter, self.BOXSIZE - half, self.BOXSIZE - half))
		elif shape == DIAMOND:
			pygame.draw.polygon(self.DISPLAYSURF, color, ((left + half, top), (left + self.BOXSIZE - 1, top + half), (left + half, top + self.BOXSIZE - 1), (left, top + half)))
		elif shape == LINES:
			pygame.draw.rect(self.DISPLAYSURF, color, (left, top, self.BOXSIZE, self.BOXSIZE ))
		elif shape == OVAL:
			pygame.draw.ellipse(self.DISPLAYSURF, color, (left, top + quarter, self.BOXSIZE, half))
		
		################################################
	def getShapeAndColor(self,board, boxx, boxy):
		return board[boxx][boxy][0], board[boxx][boxy][1]
		################################################
	def drawBoard(self,board, revealed):	
		for boxx in range(self.BOARDWIDTH):
			for boxy in range(self.BOARDHEIGHT):
				left, top = self.leftTopCoordsOfBox(boxx, boxy)
				if not revealed[boxx][boxy]:
					pygame.draw.rect(self.DISPLAYSURF,WHITE, (left, top, self.BOXSIZE, self.BOXSIZE))
				else:
					shape, color = self.getShapeAndColor(board, boxx, boxy)
					self.drawIcon(shape, color, boxx, boxy)		
	#################################################################
	def getBoxAtPixel(self,x, y):
		for boxx in range(self.BOARDWIDTH):
			for boxy in range(self.BOARDHEIGHT):
				left, top = self.leftTopCoordsOfBox(boxx, boxy)
				boxRect = pygame.Rect(left, top, self.BOXSIZE,self.BOXSIZE)
				if boxRect.collidepoint(x, y):
					return (boxx, boxy)
		return (None, None)
	
	#################################################################
	def drawHighlightBox(self,boxx, boxy):
		left, top = self.leftTopCoordsOfBox(boxx, boxy)
		pygame.draw.rect(self.DISPLAYSURF,RED, (left - 5, top - 5, self.BOXSIZE + 10, self.BOXSIZE + 10), 4)
	#################################################################
	def gameWonAnimation(self,board):
		coveredBoxes = self.generateRevealedBoxesData(True)
		color1 = LIGHTBGCOLOR
		color2 = BGCOLOR
		for i in range(13):
			color1, color2 = color2, color1 # swap colors
			self.DISPLAYSURF.fill(color1)
			self.drawBoard(board, coveredBoxes)
			pygame.display.update()
			emotion=pygame.image.load('funny-icon-11.png')
			self.DISPLAYSURF.blit(pygame.transform.scale(emotion, (100, 100)),(200,200))		
			self.DISPLAYSURF.blit(self.Text.render("Play This At First" , True, (255,255,255)), (100,100))
			pygame.time.wait(300)	
	##################################################################
	def hasWon(self,revealedBoxes):
		for i in revealedBoxes:
			if False in i:
				return False
		return True		
	
	##################################################################
	Text = pygame.font.SysFont("None",50)		
	def __init__(self,level,inp):
		self.level=level
		self.inp=inp
		pygame.init()
		self.FPSCLOCK = pygame.time.Clock()
		self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH,self. WINDOWHEIGHT))
		mousex = 0
		mousey = 0 
		pygame.display.set_caption('funy ^_^')
		mainBoard=self.getRandomizedBoard()
		revealedBoxes = self.generateRevealedBoxesData(False)
		firstSelection = None
		self.DISPLAYSURF.fill(BGCOLOR)
		self.startGameAnimation(mainBoard)
		
		while True: 
			
			mouseClicked = False
			self.DISPLAYSURF.fill(BGCOLOR)
			self.drawBoard(mainBoard, revealedBoxes)
			
			for event in pygame.event.get():
				if event.type == QUIT:
				 pygame.quit()
				 sys.exit()
				elif event.type == MOUSEMOTION:
					 mousex, mousey = event.pos
				elif event.type == MOUSEBUTTONUP:
					mousex, mousey = event.pos
					mouseClicked = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
						intro_level.intro_level(self.level,self.inp)
						 
				
			boxx, boxy = self.getBoxAtPixel(mousex, mousey)	
			if boxx != None and boxy != None:
				if not revealedBoxes[boxx][boxy]:
					self.drawHighlightBox(boxx, boxy)
				if not revealedBoxes[boxx][boxy] and mouseClicked:
					self.drawBoxCovers(mainBoard, [(boxx, boxy)],0)
					revealedBoxes[boxx][boxy] = True 	
					if firstSelection == None:
						firstSelection = (boxx, boxy)
					else:
						
						icon1shape, icon1color = self.getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
						icon2shape, icon2color = self.getShapeAndColor(mainBoard, boxx, boxy)		
						if icon1shape != icon2shape or icon1color != icon2color:
							pygame.time.wait(1000)
							self.drawBoxCovers(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)],self.BOXSIZE)
							revealedBoxes[firstSelection[0]][firstSelection[1]] = False
							revealedBoxes[boxx][boxy] = False
								
						elif self.hasWon(revealedBoxes):
							self.gameWonAnimation(mainBoard)
							pygame.time.wait(2000)
							mainBoard = self.getRandomizedBoard()
							revealedBoxes = self.generateRevealedBoxesData(False)
							self.check=self.score()#################################this score
							pygame.display.update()
							pygame.time.wait(1000)	
						firstSelection = None
			if(self.check==False):
				emotion=pygame.image.load('funny-icon-11.png')
				self.DISPLAYSURF.blit(pygame.transform.scale(emotion, (100, 100)),(200,200))		
				self.DISPLAYSURF.blit(self.Text.render("Play This At First" , True, (255,255,255)), (100,100))
				pygame.display.update()	
#m=puzzle("safaa","phalsten")

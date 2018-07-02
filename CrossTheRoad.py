import  pygame ,thread,time,sys,Car,Man,threading

#root = Tkinter.Tk()

width = 1366 
height = 768

Heart = 3

class CrossTheRoad:
	
	def __init__(self,inp):
		self.inp=inp
		pygame.init()
		self.DIS = pygame.display.set_mode((width,height),pygame.RESIZABLE,32) 
		self.car = self.initialCars()
		self.man = Man.Man(width ,height ,"man.png")
		self.backGround()
		time.sleep(1)
		self.t = thread.start_new_thread(self.Run,())
		#thread.start_new_thread(self.manRun,())
		self.man.manRun()
		
				
				
					
	def Run(self):
		f = True
		while f:
			for c in self.car:
				c.carRun()
			self.backGround()
			pygame.display.update()
			
				
			

			
		
	def initialCars(self):
		car = []
		car.append(Car.Car(self.DIS,"Red.png",width,height,width/2-50,130,60))
		car.append(Car.Car(self.DIS,"Blue.png",width,height,width/2,330,90))
		car.append(Car.Car(self.DIS,"Orange.png",width,height,width/2+100,530,80))
		car.append(Car.Car(self.DIS,"Green.png",width,height,width-200-300,230,-80))
		car.append(Car.Car(self.DIS,"Yellow.png",width,height,width-200,430,-90))
		car.append(Car.Car(self.DIS,"Gray.png",width,height,width-200-100,630,-60))
		return car
		
		
	
	def backGround(self):
		self.DIS.blit(pygame.image.load("Road.png"),(0,0))
		self.DIS.blit(pygame.image.load(str(Heart) + ".png"),(100,10))
		if not self.man.manPass():
			self.DIS.blit(self.man.getPhoto(),(self.man.getX(),self.man.getY()))
		else:
			import Congaratulaion
			c = Congaratulaion.Congratulation(Heart,width,height)
		for c in self.car:
			self.DIS.blit(c.getPhoto(),(c.getX(),c.getY()))
			if c.manHitcar(self.man) :
				global Heart
				print Heart
				if Heart >= 0:
					self.man.Reset()
					Heart -=1
				if Heart == -1:
					print 'here'
					import game_over2
					g = game_over2.gameOver()
					print 'import'
					self.man.closeManRun()
					
			

#c = CrossTheRoad("safaa")

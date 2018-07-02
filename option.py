from Tkinter import *
import pygame,menu , music,thread

class Scale_Test:
    level="Phalsten         "
    def __init__(self):
        self.root = Tk()
        self.var=StringVar(self.root)
        #thread.start_new_thread(music.playSong,('Adele.One and Only.mp3',))
        img = PhotoImage(file='heba.gif')
        self.root.call('wm', 'iconphoto', self.root._w, img)
        self.root.geometry("1600x1600")
        title_arabic=u'\uFEB3\uFEE8\uFECC\uFEEE\uFEA9'
        self.root.title(title_arabic)
        self.root.geometry("1600x1600")		
        """self.game = IntVar()#variable can get & set 
        self.game.set(100)#inilization"""
        self.stroy=IntVar()
        self.stroy.set(100)
        background_image =PhotoImage(file="heba.gif")
        w = background_image.width()
        h = background_image.height()
        
        Label(self.root,image=background_image,height=h,width=w).place(x=0,y=0,relwidth=1, relheight=1)
        Label(text="Options ",fg="Medium Blue",font=("Times New Roman",20, "bold italic")).place(x=600,y=50)
        
        Label(text="SOUND",fg="Medium Blue",bg="lightgray",font=("Times New Roman",20, "bold italic")).place(x=330,y=200)
        Scale(self.root, from_=100, to=0, length=300, width=40,bd=5,showvalue=0,
                       variable=self.stroy, command=self.scale_cmd).place(x=340,y=300)
                       
        Label(text="LEVEL",fg="Medium Blue",bg="lightgray",font=("Times New Roman",20, "bold italic")).place(x=830,y=200)              
        #self.s = Scale(self.root, from_=100, to=0, length=300, width=40,bd=5,showvalue=0,
                      # variable=self.game, command=self.scale_game).place(x=840,y=300)
                  
        
        
        self.var.set("Phalsten         ") # initial value
        

        option = OptionMenu(self.root, self.var,"Egypt        ", "Phalsten         ")
        option.place(x=840,y=300)
                   
        back=Button(self.root,text="Save",height=1,width=6,font=("Times", "23", "bold italic"),command=self.quit)
        back.pack(side=BOTTOM,pady=40) 
        
        self.root.mainloop()
        

		
    def scale_cmd(self, event=None):
		music.change_volume(self.stroy.get())
        #print "story is ",self.stroy.get()
     
    """def scale_game(self,event=None):
		music.change_volume(self.game.get())
		#print "game is ",self.game.get() """
		 
    def quit(self):
		Scale_Test.level=self.var.get()
		self.root.destroy()

#m = Scale_Test()

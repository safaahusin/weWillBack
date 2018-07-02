import Tkinter
import Tkinter,time
import tkFont

class frame1:
	def __init__(self):
		
		window=Tkinter.Tk()
		title_arabic=u'\uFEB3\uFEE8\uFECC\uFEEE\uFEA9'
		window.title(title_arabic)
		img = Tkinter.PhotoImage(file = 'maxresdefault.gif')
		window.call('wm', 'iconphoto', window._w, img)
		window.geometry("1330x710")
		window.resizable(width=False, height=False) 
		#window.title("we will come")
		m=tkFont.Font(family="Times New Roman", size=18)
		mylabel=Tkinter.Label(text="Loading  . . .",fg="#ff1a75",bg="black",font=m)
		mylabel.place(x=665,y=300)
		mylabel3=Tkinter.Text()
		mylabel3.place(x=550,y=395)
		mylabel3['width']='50'
		mylabel3['height']=0.6
		mylabel3.configure(state='disabled')
		self.load()
		window.configure(background='black')
		window.mainloop()
		
	def load(self):
		mylabel2=Tkinter.Text()
		mylabel2['bd']=0
		mylabel2['bg']="#ff99ff"
		mylabel2['height']=0.5
		mylabel2['width']='0'
		mylabel2.place(x=550,y=395)
		mylabel2.after(200, lambda: mylabel2.config(bg='#ff99ff',width ='6'))
		mylabel2.after(250, lambda: mylabel2.config(bg='#ff99ff',width ='7'))
		mylabel2.after(300, lambda: mylabel2.config(bg='#ff99ff',width ='8'))
		mylabel2.after(350, lambda: mylabel2.config(bg='#ff99ff',width ='9'))
		mylabel2.after(400, lambda: mylabel2.config(bg='#ff99ff',width ='10'))
		mylabel2.after(450, lambda: mylabel2.config(bg='#ff99ff',width ='11'))
		mylabel2.after(500, lambda: mylabel2.config(bg='#ff99ff',width ='12'))
		mylabel2.after(550, lambda: mylabel2.config(bg='#ff99ff',width ='13'))
		mylabel2.after(600, lambda: mylabel2.config(bg='#ff99ff',width ='14'))
		mylabel2.after(650, lambda: mylabel2.config(bg='#ff99ff',width ='15'))
		mylabel2.after(700, lambda: mylabel2.config(bg='#ff99ff',width ='16'))
		mylabel2.after(750, lambda: mylabel2.config(bg='#ff99ff',width ='17'))
		mylabel2.after(800, lambda: mylabel2.config(bg='#ff99ff',width ='18'))
		mylabel2.after(850, lambda: mylabel2.config(bg='#ff99ff',width ='19'))
		mylabel2.after(900, lambda: mylabel2.config(bg='#ff99ff',width ='20'))
		mylabel2.after(950, lambda: mylabel2.config(bg='#ff99ff',width ='21'))
		mylabel2.after(1000, lambda: mylabel2.config(bg='#ff99ff',width ='22'))
		mylabel2.after(1050, lambda: mylabel2.config(bg='#ff99ff',width ='23'))
		mylabel2.after(1100, lambda: mylabel2.config(bg='#ff99ff',width ='24'))
		mylabel2.after(1150, lambda: mylabel2.config(bg='#ff99ff',width ='25'))
		mylabel2.after(1200, lambda: mylabel2.config(bg='#ff99ff',width ='26'))
		mylabel2.after(1250, lambda: mylabel2.config(bg='#ff99ff',width ='27'))
		mylabel2.after(1300, lambda: mylabel2.config(bg='#ff99ff',width ='28'))
		mylabel2.after(1350, lambda: mylabel2.config(bg='#ff99ff',width ='29'))
		mylabel2.after(1400, lambda: mylabel2.config(bg='#ff99ff',width ='30'))
		mylabel2.after(1450, lambda: mylabel2.config(bg='#ff99ff',width ='31'))
		mylabel2.after(1500, lambda: mylabel2.config(bg='#ff99ff',width ='32'))
		mylabel2.after(1550, lambda: mylabel2.config(bg='#ff99ff',width ='33'))
		mylabel2.after(1600, lambda: mylabel2.config(bg='#ff99ff',width ='34'))
		mylabel2.after(1650, lambda: mylabel2.config(bg='#ff99ff',width ='35'))
		mylabel2.after(1700, lambda: mylabel2.config(bg='#ff99ff',width ='36'))
		mylabel2.after(1750, lambda: mylabel2.config(bg='#ff99ff',width ='37'))
		mylabel2.after(1800, lambda: mylabel2.config(bg='#ff99ff',width ='40'))
		mylabel2.after(1850, lambda: mylabel2.config(bg='#ff99ff',width ='41'))
		mylabel2.after(1900, lambda: mylabel2.config(bg='#ff99ff',width ='42'))
		mylabel2.after(1950, lambda: mylabel2.config(bg='#ff99ff',width ='43'))
		mylabel2.after(2000, lambda: mylabel2.config(bg='#ff99ff',width ='44'))
		mylabel2.after(2050, lambda: mylabel2.config(bg='#ff99ff',width ='45'))
		mylabel2.after(2100, lambda: mylabel2.config(bg='#ff99ff',width ='46'))
		mylabel2.after(2150, lambda: mylabel2.config(bg='#ff99ff',width ='47'))
		mylabel2.after(2200, lambda: mylabel2.config(bg='#ff99ff',width ='48'))
		mylabel2.after(2250, lambda: mylabel2.config(bg='#ff99ff',width ='49'))
		mylabel2.after(2300, lambda: mylabel2.config(bg='#ff99ff',width ='50'))
		mylabel2.configure(state='disabled')
			
e=frame1()

#------------------Author Info----------------------#
#		Maintenance Downtime SQL upload GUI
# Designed and developed by: Ing Jorge Alberto Morales, MBA
# Controls Engineer for Mubea Coil Springs Mexico
# JorgeAlberto.Morales@mubea.com
#---------------------------------------------------#


#----------------------import area
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import sys
import os
from datetime import *
import datetime
import tkinter as tk
import os
import time, threading
from tkinter import *
from tkinter import messagebox
from functools import partial
import tkinter as tk
import sys
from datetime import datetime
import csv
#--------------------------------------

#---------------------------------------Auxiliary Functions-------------------------#
def convert(date_time):
	new_datetime = date_time.replace("/"," ")
	format = '%d %m %Y'  # The format
	datetime_str = datetime.datetime.strptime(new_datetime, format).isocalendar()[1]
 
	return datetime_str

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


#/////----------------------------Reading and Writing Files--------------------------#

with open(resource_path("resources/basic_btn_data.csv")) as file:
	type(file)
	csvreader = csv.reader(file)
	header = []
	header = next(csvreader)
	header
	rows = []
	for row in csvreader:
		rows.append(row)


with open(resource_path("resources/label_data.csv")) as file:
	type(file)
	csvreader = csv.reader(file)
	header = []
	header = next(csvreader)
	header
	etiqs = []
	for etiq in csvreader:
		etiqs.append(etiq)



####### machine loader CSV

#Original data 
machines = pd.read_csv(resource_path('resources/machines.csv'))
df1 = machines['Linea'].unique()

#a text file output that will serve as a receipt for the upload



#--------------------SQL Management------------------------
engine = create_engine('mssql+pyodbc://scadamex:scadamex@SAL-W12E-SQL\MSSQLMEX/scadadata?driver=SQL+Server+Native+Client+11.0', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


#-----------------------------Start of tkinter classes-----------------------------#

#This class PasswordChecker stores the necessary data to run a tkinter gui.
class Passwordchecker(tk.Frame):
	#needs info
	def __init__(self, parent):
	#tk.frame starts and calls the initialize user interface
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.initialize_user_interface()

	#first function inside the class: GUI initializing
	#this is where GUI initial configuration takes place.
	def initialize_user_interface(self):
		#define the GUI size in px (depends on end-user screen size)
		self.parent.geometry("1920x1080")
		#protocol to correctly close GUI
		self.parent.protocol("WM_DELETE_WINDOW", self.quit)
		self.parent.title("Mubea Mexico - Maintenance Reporting Tool.")
		# a label that contains the background image
		self.background_image = PhotoImage(file = resource_path("resources/UI2.png"))
		#self.parent.attributes('-fullscreen', True)
		self.parent.attributes('-fullscreen', True)
		label1 = Label(self.parent, image = self.background_image)
		label1.place(x = 0,y = 0)
		#general parameters for the buttons.
		h_offset = 2
		w_offset = 4
		self.fg_offset = "white"
		self.bg_offset = '#314a94'
######Button declaration area
		for i in range(len(rows)):
		#process the first button
			a_temp = rows[i-1][1]
			globals()[a_temp] = Button(self.parent, width = w_offset, height = h_offset)
			globals()[a_temp].configure(width = int(rows[i-1][6]))
			globals()[a_temp].configure(height = int(rows[i-1][7]))
			globals()[a_temp].place(x =int(rows[i-1][2]),y=int(rows[i-1][3]))
			globals()[a_temp].configure(bg = self.bg_offset)
			globals()[a_temp].configure(fg = self.fg_offset)
			globals()[a_temp].configure(font=("Helvetica", 12, "bold"))
			globals()[a_temp].configure(text = rows[i-1][4])
			#self.selector is the function inside the main class
			globals()[a_temp].configure(command=partial(self.Selector, int(rows[i-1][5])))

#########label declaration area
		for i in range(len(etiqs)):
		#process the first button
			a_temp = etiqs[i-1][1]
			globals()[a_temp] = Label(self.parent, width = w_offset, height = h_offset)
			globals()[a_temp].configure(width = int(etiqs[i-1][6]))
			globals()[a_temp].configure(height = int(etiqs[i-1][7]))
			globals()[a_temp].place(x =int(etiqs[i-1][2]),y=int(etiqs[i-1][3]))
			globals()[a_temp].configure(bg = self.bg_offset)
			globals()[a_temp].configure(fg = self.fg_offset)
			globals()[a_temp].configure(font=("Helvetica", int(etiqs[i-1][8]), "bold"))
			globals()[a_temp].configure(text = etiqs[i-1][4])



			self.console = Label(self.parent,width = w_offset*10, height = h_offset)
			self.console.place(x=350,y=410)
			self.console.configure(text = "HI")
			self.console.configure(fg="white", bg="black", font=("Console",10))
######### Create Dropdown menus for COM options 
		#ComPort.
		dropwidth = 20
		dropfront = "white"
		dropbg = '#314a94'
		dropfont = ("Helvetica",14)
		dropx = 300
		dropy = 122

		#list area
		#machines
		self.D_Linea = StringVar()
		self.D_Linea.set("Linea")
		self.dropdown2 = OptionMenu(self.parent,self.D_Linea,*df1)
		self.dropdown2.place(x=int(dropx),y=int(dropy)+35)
		self.dropdown2.configure(fg=dropfront, bg=dropbg, width=dropwidth, font=dropfont,highlightthickness=0)
		
		self.D_Linea.trace("w",self.machine_selector)

		self.D_Machine = StringVar()
		self.D_Machine.set("Maquina")
		self.dropdown3 = OptionMenu(self.parent,self.D_Machine, ' ')
		self.dropdown3.place(x=int(dropx),y=int(dropy)+85)
		self.dropdown3.configure(fg=dropfront, bg=dropbg, width=dropwidth, font=dropfont,highlightthickness=0)		

		self.D_Machine.trace("w",self.component_selector)

		self.D_Component = StringVar()
		self.D_Component.set("Componente")
		self.dropdown4 = OptionMenu(self.parent,self.D_Component, ' ')
		self.dropdown4.place(x=int(dropx),y=int(dropy)+135)
		self.dropdown4.configure(fg=dropfront, bg=dropbg, width=dropwidth, font=dropfont,highlightthickness=0)		

		Falla = tk.Text(self.parent, width=40, height=3,font=("Helvetica", 12),borderwidth=2).place(x=int(dropx)+800,y=int(dropy)+115)
		Root_C = tk.Text(self.parent, width=30, height=3,font=("Helvetica", 12),borderwidth=2).place(x=int(dropx)+850,y=int(dropy)+115)
		Descr = tk.Text(self.parent, width=30, height=3,font=("Helvetica", 12),borderwidth=2).place(x=int(dropx)+800,y=int(dropy)+200)

##########Selector is the function that commands buttons actions
	def Selector(self,num):
		global ComPort
		#go to def run() in thread 2 and config it to pass these variables to the method1 second thread.	
		#### area to check if the info coming from the optionmenu is valid and all the option menus were opened and selected.
			
		#button to Open COM
		if num == 10:
			print('10')
			ComPort = self.D_Linea.get()
			print(ComPort)
			SecondThread.start()
		#button to close COM
		if num == 20:
			print('20')
		if num == 30:
			print('30')


	def quit(self):
		if messagebox.askyesno('Salida','¿Seguro que quiere salir?'):
            #In order to use quit function, mainWindow MUST BE an attribute of Interface. 
			self.parent.destroy()
			self.parent.quit()
			SecondThread.stop()


	def method1(self,ComPort): 
		#This is the area where the second thread lives.
		while finish is not True:
			print(f"second thread: {ComPort}")
			time.sleep(5)
	
	def machine_selector(self,*args):
		global df3
		#pandas dataframe is already loaded
		#single column dataframe with lines
		valor = self.D_Linea.get()
		#print(valor)
		df2=machines.query("Linea == @valor")
		#print(df2)
		df3 = df2['MAQUINA'].unique()
		df3.sort()
		menu = self.dropdown3['menu']
		menu.delete(0, 'end')
		for maquinas in df3:
			menu.add_command(label=maquinas, command=lambda data=maquinas: self.D_Machine.set(data))

	def component_selector(self,*args):
		global df6
		#pandas dataframe is already loaded
		#single column dataframe with lines
		valor1 = self.D_Linea.get()
		valor2 = self.D_Machine.get()
		#print(valor)
		df2=machines.query("Linea == @valor1")
		df5=df2.query("MAQUINA == @valor2")
		df6 = df5['COMPONENTE'].unique()
		#WE SORT THIS
		#print(df6)
		df6.sort()
		menu = self.dropdown4['menu']
		menu.delete(0, 'end')
		for components in df6:
			menu.add_command(label=components, command=lambda data=components: self.D_Component.set(data))	





		
#################Threading area 
class Process(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.attrib2 = "Attrib from Process1 class"

class Process(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.attrib2 = "Attrib from Process2 class"
		self._stop_event = threading.Event()

	def run(self):
		global finish
		#while not finish:
			#do not start serial until com info is selected.
		run1.method1(ComPort)
		#run1.console.configure(text = f"Proceso Terminado")

	
	def stop(self):
		self._stop_event.set()
		print("Thread Stopped")

#stuff that 
if __name__ == '__main__':
	finish = False
	root = tk.Tk()
	SecondThread = Process()
	run1 = Passwordchecker(root)
	root.mainloop() #GUI.start()
	#print("Exiting....")
	finish = True

#main thread is not in main loop error was raising because i was trying to run the next GUI command
	#run1.console.configure(text = f"Proceso Terminado")
#after i executed root.destroy() and root.quit().
# i finished the process then i tried to execute a GUI command. What an error.


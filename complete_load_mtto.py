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

####### machine loader CSV

#Original data 
machines = pd.read_csv(resource_path('resources/machines.csv'))


#single column dataframe with lines
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
		self.parent.geometry("979x480")
		#protocol to correctly close GUI
		self.parent.protocol("WM_DELETE_WINDOW", self.quit)
		self.parent.title("Mubea de Mexico - Reporte de Mantenimiento.")
		# a label that contains the background image
		self.background_image = PhotoImage(file = resource_path("resources/UI1.png"))
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

			self.console = Label(self.parent,width = w_offset*10, height = h_offset)
			self.console.place(x=350,y=410)
			self.console.configure(text = "HI")
			self.console.configure(fg="white", bg="black", font=("Console",10))
######### Create Dropdown menus for COM options 
		#ComPort.
		dropwidth = 18
		dropfront = "white"
		dropbg = '#314a94'
		dropfont = ("Sans-serif",10)
		dropx = 229
		dropy = 30

		#list area

		#machines
		self.baudRate1 = StringVar()
		self.baudRate1.set("Linea")
		dropdown2 = OptionMenu(self.parent,self.baudRate1,*df1)
		dropdown2.place(x=int(dropx),y=int(dropy)+30)
		dropdown2.configure(fg=dropfront, bg=dropbg, width=dropwidth, font=dropfont)












##########Selector is the function that commands buttons actions
	def Selector(self,num):

		#go to def run() in thread 2 and config it to pass these variables to the method1 second thread.	
		#### area to check if the info coming from the optionmenu is valid and all the option menus were opened and selected.
			
		#button to Open COM
		if num == 10:
			print('10')
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

	def method1(self,ComPort,baudRate,Parity_data,stop_bits,byte_size): 
		#This is the area where the second thread lives.
		while finish is not True:
			print("second thread")
			time.sleep(5)

		
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
		run1.method1()
		run1.console.configure(text = f"Proceso Terminado")
	
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
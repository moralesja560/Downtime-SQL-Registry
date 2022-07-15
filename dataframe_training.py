import pandas as pd
import csv
import sys,os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


#MACHINES IS THE ORIGINAL DATAFRAME
machines = pd.read_csv(resource_path('resources/machines.csv'))

#DF1 CONTAINS THE LINES
df1 = machines['Linea'].unique()

value=input(f"Please input line:  ")
#DF2 IS TO FILTER THE ORIGINAL DATAFRAME TO GET THE MACHINES AND COMPONENTS FROM SELECTED LINE
df2=machines.query("Linea == @value")

#df3 STORES THE UNIQUE MACHINE VALUES TO FILL THE COMBOBOX
df3 = df2['MAQUINA'].unique()



value=input(f"Please input machine:  ")
#AGAIN, WE FILTER DF2 TO GET THE SELECTED MACHINE
df5=df2.query("MAQUINA == @value")
#RETRIEVE ONLY THE UNIQUE VALUES TO FORM A SINGLE-COLUMN DATAFRAME
df6 = df5['COMPONENTE'].unique()
#WE SORT THIS
df6.sort()
print(df5)
print(df6)

L



import pandas as pd
import csv
import sys,os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#Original data 
machines = pd.read_csv(resource_path('resources/machines.csv'))


#single column dataframe with lines
df1 = machines['Linea'].unique()

value=input(f"Please input filter:  ")
df2=machines.query("Linea == @value")

print(df1)


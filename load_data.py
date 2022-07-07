#This procedure will upload user-input data into the designated SQL table

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import sys
import os
from datetime import *



engine = create_engine('mssql+pyodbc://scadamex:scadamex@SAL-W12E-SQL\MSSQLMEX/scadadata?driver=SQL+Server+Native+Client+11.0', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


sql = "SELECT NUM FROM Temp3_Mtto_Log"
df = pd.read_sql_query(sql, engine)
df.to_string()

max_number = df["NUM"].iloc[-1]

columns = ["NUM","LINEA","COMPONENTE","CONDICION","ACCION","CODIGO_MAQUINA","CAUSA","MINUTOS","FECHA","SEMANA","RESPONSABLE","TURNO","APLICA"]

dicc = {'NUM': max_number+1, 
		'LINEA': 'linea',
		"COMPONENTE": 'compo',
		"CONDICION": 'condi',
		"ACCION": 'accion',
		"CODIGO_MAQUINA": 'maq',
		"CAUSA": 'causa',
		"MINUTOS": 100,
		"FECHA": '10-05-2006',
		"SEMANA": '5',
		"RESPONSABLE": 'JAM',
		"TURNO": '1',
		"APLICA": 'SI'
		}


#Step 1: ask for user input and store in a python list.
for i in range(0,12):
	if i == 8:
		weeknum =  datetime.date(dicc['FECHA'])
		val = weeknum.strftime("%U")
	else:
		val = input(f"Please input {columns[i+1]}:  ")
		
	print(f"el ciclo {i} va con la columna {columns[i+1]} ")
	dicc.update({columns[i+1]:val})

mtto_df = pd.DataFrame([dicc])
print(mtto_df)
#mtto_df.to_sql('Temp3_Mtto_Log', con=engine, if_exists='append',index=False)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pyodbc
import pandas as pd


engine = create_engine('mssql+pyodbc://scadamex:scadamex@SAL-W12E-SQL\MSSQLMEX/scadadata?driver=SQL+Server+Native+Client+11.0', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

sql = "SELECT * FROM Empleados_Mtto"
df = pd.read_sql_query(sql, engine)
df.head()

print(df)

mydict = {562: "Erik Gaytan",
		568: "Jorge Perez",
		986: "Alejandro Lopez", 
		1471: "Omar Hernandez",
		1476: "Pablo Garcia",
		1881: "Eduardo Rodriguez",
		2693: "Francisco Perez",
		2786: "Carlos Darley",
		3939: "Rodrigo Gutierrez",
		4025: "Enrique Munoz",
		4045: "Jose Salazar",
		4281: "Osvaldo Gutierrez",
		4383: "Diego Hernandez",
		1830: "Jorge Morales",
		734:  "Angel Irigoyen",
		3840: "Ernesto Barron",
		4146: "Bryan Monroy"
		}

nueva_info = pd.DataFrame(mydict.items(), columns=['Empl_Number', 'Empl_Name'])

print(nueva_info)

#nueva_info.to_sql('Empleados_Mtto', con=engine, if_exists='append')
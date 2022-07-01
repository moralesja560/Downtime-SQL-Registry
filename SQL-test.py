from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pyodbc
import pandas as pd

#engine = create_engine("dialect[SQL Server]://scadamex:scadamex@SAL-W12E-SQL//MSSQLMEX/scadadata")

#"dialect[+driver]://+ dsn_uid + ':' + dsn_pwd + '@'+dsn_hostname+':'+dsn_port+'/' + dsn_database"

#"dialect[SQL Server]://scadamex:scadamex@SAL-W12E-SQL\MSSQLMEX\scadadata"

#engine = create_engine(r'mssql+pyodbc://scadamex:scadamex@SAL-W12E-SQL\MSSQLMEX\scadadata')

engine = create_engine('mssql+pyodbc://scadamex:scadamex@SAL-W12E-SQL\MSSQLMEX/scadadata?driver=SQL+Server+Native+Client+11.0', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

sql = "SELECT * FROM Empleados_Mtto"
df = pd.read_sql_query(sql, engine)
df.head()

print(df)

mydict = {'1830':'Jorge Morales',
		'1831':'Ernesto Barron',
		'2756':'Bryan Monroy'
		}

nueva_info = pd.DataFrame(mydict.items(), columns=['Empl_Number', 'Empl_Name'])

print(nueva_info)

nueva_info.to_sql('Empleados_Mtto', con=engine, if_exists='replace')
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import sys
import os

engine = create_engine('mssql+pyodbc://scadamex:scadamex@SAL-W12E-SQL\MSSQLMEX/scadadata?driver=SQL+Server+Native+Client+11.0', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

mtto_df = pd.read_csv(resource_path(r"resources/mtto_data.csv"),header=0,usecols=['NUM','LINEA','MAQUINA','COMPONENTE','CONDICION_FALLA','ACCION_INMEDIATA','MAQUINA_1','CAUSA','Minutos_TM','FECHA','SEMANA','RESPONSABLE','TURNO','Aplica'])


#nueva_info = pd.DataFrame(mtto_df, columns=['NUM','LINEA','MAQUINA','COMPONENTE','CONDICION_FALLA','ACCION_INMEDIATA','MAQUINA_1','CAUSA','Minutos_TM','FECHA','SEMANA','RESPONSABLE','TURNO','Aplica'])

print(mtto_df)
mtto_df.to_sql('Test2_MTTO_History', con=engine, if_exists='append')
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import obtener_conexion_db
from sqlalchemy import text

def cargar_tabla(df: pd.DataFrame, nombre: str) -> None:
    engine = obtener_conexion_db()
    with engine.connect() as conn:
        conn.execute(text(f'DROP TABLE IF EXISTS {nombre} CASCADE'))
        conn.commit()
    df.to_sql(nombre, con=engine, if_exists='replace', index=False)
    print(f'[LOAD] Tabla "{nombre}" cargada: {len(df)} filas.')

from sqlalchemy import create_engine

def obtener_conexion_db():
    url_conexion = 'postgresql+psycopg2://postgres:abeja@localhost:5432/educacion'
    return create_engine(url_conexion)
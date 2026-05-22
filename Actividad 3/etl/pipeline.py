from extract import extraer_datos
from transform import (
    crear_dimension_ubicacion, 
    crear_dimension_institucion, 
    crear_tabla_hechos_matricula
)
from load import cargar_tabla

RUTA_FUENTE = 'C:/Users/biaro/OneDrive/Desktop/registro-administrativo-historico_2009-2024-inicio.xlsx'

def ejecutar_pipeline():
    # 1. EXTRACT
    df_raw = extraer_datos(RUTA_FUENTE)

    # 2. TRANSFORM
    dim_ub   = crear_dimension_ubicacion(df_raw)
    dim_inst = crear_dimension_institucion(df_raw, dim_ub)
    fact_mat = crear_tabla_hechos_matricula(df_raw)

    # 3. LOAD
    cargar_tabla(dim_ub,   'dim_ubicacion')
    cargar_tabla(dim_inst, 'dim_institucion')
    cargar_tabla(fact_mat, 'fact_matricula')
    print('[PIPELINE] Completado exitosamente.')

if __name__ == '__main__':
    ejecutar_pipeline()

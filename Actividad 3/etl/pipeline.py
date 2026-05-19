from etl.extract import extraer_datos
from etl.transform import (
    crear_dimension_ubicacion    as construir_dim_ubicacion,
    crear_dimension_institucion  as construir_dim_institucion,
    crear_tabla_hechos_matricula as construir_fact_matricula
)
from etl.load import cargar_tabla

RUTA_FUENTE = 'C:/Users/biaro/OneDrive/Desktop/Pr-cticum-2.2/Actividad 3/registro-administrativo-historico_2009-2024-inicio.xlsx'

def ejecutar_pipeline():
    # 1. EXTRACT
    df_raw = extraer_datos(RUTA_FUENTE)

    # 2. TRANSFORM
    dim_ub   = construir_dim_ubicacion(df_raw)
    dim_inst = construir_dim_institucion(df_raw, dim_ub)
    fact_mat = construir_fact_matricula(df_raw)

    # 3. LOAD
    cargar_tabla(dim_ub,   'dim_ubicacion')
    cargar_tabla(dim_inst, 'dim_institucion')
    cargar_tabla(fact_mat, 'fact_matricula')
    print('[PIPELINE] Completado exitosamente.')

if __name__ == '__main__':
    ejecutar_pipeline()

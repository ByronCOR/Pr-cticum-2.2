import pandas as pd

def extraer_datos(ruta_archivo: str) -> pd.DataFrame:
    # Soporte para Excel y CSV
    if ruta_archivo.endswith('.xlsx'):
        datos_crudos = pd.read_excel(ruta_archivo)
    else:
        datos_crudos = pd.read_csv(ruta_archivo, encoding='utf-8')
    
    # Normalización: minúsculas y quitar espacios en blanco
    datos_crudos.columns = datos_crudos.columns.str.lower().str.strip()
    
    for columna in datos_crudos.select_dtypes(include='object').columns:
        datos_crudos[columna] = datos_crudos[columna].str.strip()
        
    print(f"[EXTRACT] Filas: {datos_crudos.shape[0]}, Columnas: {datos_crudos.shape[1]}")
    return datos_crudos

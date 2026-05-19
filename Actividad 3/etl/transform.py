import pandas as pd

def crear_dimension_ubicacion(datos: pd.DataFrame) -> pd.DataFrame:
    columnas_geo = [
        'provincia', 'cod_provincia', 'canton', 'cod_canton',
        'parroquia', 'cod_parroquia', 'zona', 'regimen_escolar'
    ]
    tabla_ubicacion = datos[columnas_geo].drop_duplicates().reset_index(drop=True)
    tabla_ubicacion.insert(0, 'id_ubicacion', range(1, len(tabla_ubicacion) + 1))
    return tabla_ubicacion


def crear_dimension_institucion(datos: pd.DataFrame, tabla_geo: pd.DataFrame) -> pd.DataFrame:
    columnas_inst = [
        'codigo_institucion', 'nombre_institucion', 'sostenimiento',
        'modallidad', 'jornada', 'area', 'nivel_educativo'
    ]
    columnas_geo = [
        'provincia', 'cod_provincia', 'canton', 'cod_canton',
        'parroquia', 'cod_parroquia', 'zona', 'regimen_escolar'
    ]
    merge_instituciones = (
        datos[columnas_inst + columnas_geo]
        .drop_duplicates(subset=['codigo_institucion'])
        .merge(tabla_geo[columnas_geo + ['id_ubicacion']], on=columnas_geo, how='left')
    )
    tabla_final = merge_instituciones.drop(columns=columnas_geo)
    return tabla_final.rename(columns={
        'codigo_institucion': 'cod_amie',
        'modallidad': 'modalidad',
        'nivel_educativo': 'nivel_educacion'
    })


def crear_tabla_hechos_matricula(datos: pd.DataFrame) -> pd.DataFrame:
    columnas_hechos = [
        'codigo_institucion',
        'periodo',
        'total_estudiantes',
        'estudiantes_femenino',
        'estudiantes_masculino',
        'total_docentes',
        'docentes_femenino',
        'docentes_masculino'
    ]
    hechos = datos[columnas_hechos].copy()
    hechos = hechos.rename(columns={
        'codigo_institucion':    'cod_amie',
        'periodo':               'anio_lectivo',
        'estudiantes_femenino':  'estudiantes_f',
        'estudiantes_masculino': 'estudiantes_m',
        'docentes_femenino':     'docentes_f',
        'docentes_masculino':    'docentes_m'
    })
    hechos['ratio_est_docente'] = (
        hechos['total_estudiantes'] / hechos['total_docentes'].replace(0,float('nan'))
    ).round(1)
    hechos.insert(0, 'id_matricula', range(1, len(hechos) + 1))
    return hechos

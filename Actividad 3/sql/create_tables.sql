-- Dimensión Ubicación
CREATE TABLE IF NOT EXISTS dim_ubicacion (
    id_ubicacion    SERIAL PRIMARY KEY,
    provincia       VARCHAR(80) NOT NULL,
    cod_provincia   CHAR(2) NOT NULL,
    canton          VARCHAR(80) NOT NULL,
    cod_canton      CHAR(4) NOT NULL,
    parroquia       VARCHAR(80) NOT NULL,
    cod_parroquia   CHAR(6),
    zona            VARCHAR(20),
    regimen_escolar VARCHAR(20)
);

-- Dimensión Institución
CREATE TABLE IF NOT EXISTS dim_institucion (
    cod_amie            VARCHAR(8) PRIMARY KEY,
    nombre_institucion  TEXT NOT NULL,
    sostenimiento       VARCHAR(30),
    modalidad           VARCHAR(30),
    jornada             VARCHAR(30),
    area                VARCHAR(20),
    nivel_educacion     VARCHAR(50),
    id_ubicacion        INTEGER REFERENCES dim_ubicacion(id_ubicacion) ON DELETE SET NULL
);

-- Tabla de Hechos Matrícula
CREATE TABLE IF NOT EXISTS fact_matricula (
    id_matricula        SERIAL PRIMARY KEY,
    cod_amie            VARCHAR(8) NOT NULL REFERENCES dim_institucion(cod_amie),
    anio_lectivo        VARCHAR(9) NOT NULL,
    total_estudiantes   INTEGER,
    estudiantes_f       INTEGER,
    estudiantes_m       INTEGER,
    total_docentes      INTEGER,
    docentes_f          INTEGER,
    docentes_m          INTEGER,
    ratio_est_docente   NUMERIC(6,1)
);

-- Índices para optimizar el Dashboard
CREATE INDEX idx_fm_cod_amie ON fact_matricula(cod_amie);
CREATE INDEX idx_fm_anio ON fact_matricula(anio_lectivo);
¿En qué provincias hay mayor carga docente (estudiantes por docente)? 
SELECT u.provincia, 
ROUND(SUM(f.total_estudiantes)::numeric / 
NULLIF(SUM(f.total_docentes),0),1) AS ratio 
FROM fact_matricula f 
JOIN dim_institucion i USING (cod_amie) 
JOIN dim_ubicacion u USING (id_ubicacion) 
WHERE f.anio_lectivo LIKE '2022-2023%'
GROUP BY u.provincia 
ORDER BY ratio DESC 

¿En qué nivel educativo hay mayor brecha de género en la matrícula? 
SELECT i.nivel_educacion, SUM(estudiantes_f) AS mujeres,
 SUM(estudiantes_m) AS hombres,
ROUND(100.0*SUM(estudiantes_f)/NULLIF(SUM(total_estudiantes),0),1) AS pct_mujeres FROM fact_matricula f JOIN dim_institucion i USING (cod_amie) 
WHERE anio_lectivo LIKE '2022-2023%' 
GROUP BY nivel_educacion 
ORDER BY pct_mujeres 

¿Cómo evolucionó la matrícula en Loja entre 2015 y 2024? 

SELECT f.anio_lectivo, 
COUNT(DISTINCT f.cod_amie) AS instituciones, 
SUM(f.total_estudiantes) AS estudiantes 
FROM fact_matricula f 
JOIN dim_institucion i USING (cod_amie) 
JOIN dim_ubicacion u USING (id_ubicacion) 
WHERE u.provincia='LOJA' AND f.anio_lectivo>='2015-2016' 
GROUP BY f.anio_lectivo ORDER BY 1 
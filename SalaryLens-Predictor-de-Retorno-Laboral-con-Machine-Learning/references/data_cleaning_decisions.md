# Registro de Decisiones de Limpieza y Transformacion de Datos (Data Cleaning Decisions)

Este documento detalla las intervenciones realizadas sobre el dataset original ``job_salary_prediction_dataset.csv`` para garantizar la integridad de los datos y optimizar el rendimiento de los futuros modelos de Machine learning.

## 1. Transformacion de la variable objetivo (``salary``)
- **Problema detectado:** Tras un analisis estadistico inicial, se observo que la variable ``salary`` presentaba una asimetria positiva (sesgo hacia la derecha) de nivel leve/moderado.
Los valores de salarios altos despazaban la media, alejandola de la mediana.

- **Decision:** Aplicar una transformacion de **raiz cuadrada** ($\sqrt{x}$).
- **Justificacion:** 
    - Se evaluo la transformacion logaritmica, pero se descarto por ser demasiado agresiva para el nivel de sesgo presente (no se trata de una Power Law).
    - La raiz cuadrada penalia moderadamente los valores altos, logrando que la distribucion se aproxime a una **Distribucion Gaussiana (Normal)**.
    - Esto mejora la converfencia de algoritmos que asumen normalidad y facilita un escalado posterior mas equilibrado.
- **Nota tecnica:** Las metricas de error y predicciones finales del modelo estaran en esta escala. Se requiere aplicar la operacion inversa ($x^2$) para la interpretacion de resultados finales.

## 2. Tratamientos de Valores Atipicos (Outliers) en Features.

- **Estado:** Las variables independientes como ``experience_years``, ``skills_count`` y ``certifications`` fueron analizadas mediante diagramas de caja (boxplots).
- **Decision:** No se aplicaron recortes (clipping) ni eliminaciones.

## 3. Estado de Limpieza del Dataset.

- **Calidad:** El dataset se encuentra completamente limpio.
- **Nulos:** No existe presencia de valores nulos.
- **Outliers:** No hay presencia de outliers en las variables predictoras.
- **Resultado:** El conjunto de datos esta listo para ser analizado univariadamente.

## 4. Decisiones sobre Categirias y Escalamiento.

- **Variables categoricas:** Se mantienen las columnas categoricas en su formato original. No se han aplicado codificadores (encoders) en esta etapa para permitir el analisis en los notebooks posteriores.
- **Escalamiento:** No se ha realizado el escalado de las variables aun, a pesar de la diferencia de magnitudes entra las features y el salario transformado.

## 5. Archivos Generados.

- **Dataset procesado:** ``data/interim/cleaned_data.csv``
- **Registro de decisiones:** ``references/data_cleaning_decisions.md``

# Salary Lens Predictor
Este proyecto nace para abordar una de las decisiones mas criticas en la vida de un joven: **la eleccion de carrera**. Mas alla de la vocacion, existe una necesidad latente de entender el retorno de inversion en educacion y el panorama laboral real.

## 1. Resumen del proyecto
Desarrollar un modelo de **Machine Learning** capaz de predecir el salario anual de un profesional basandose en multiples dimensiones socio-laborales. El fin ultimo es proporcionar una herramienta objetiva que ayude a los estudiantes a establecer expectativas realistas sobre su futuro financiero segun el camino academico y profesional que decidan tomar.

### Pregunta de negocio central
Que variables tienen mayor impacto en el salario y cual es el rango esperado dado un perfil especifico?

### Criterios de exito del EDA
- Identificar las **3 features mas predictivas** del salario (salary)
- Documentar todas las decisiones de limpieza en ```references/```
- Producir un dataset procesado reproducible en ```data/processed/```

## 2. Hallazgos del EDA
### Hallazgos principales
- Años de experiencia: Identificado como la variable con **mayor correlacion positiva** con el salario. Es el predictor principal de este dataset.
- **Tamanio de empresa:** Segunda variable mas influyente; el crecimiento en la estructura organizacional impacta positivamente en la remuneracion
- **Ubicacion (``location``):** Factor determinante en la variable salarial, destacando como el tercer predictor mas fuerte.
- **Paradoja Educativa:** Los datos sugieren que el **nivel de educacion y certificaciones** no son factores determinantes para una mayor remuneracion en este dataset tecnico, priorizando la experiencia comprobable.
  
### Distribucion del target
- **Variable ``salary``:** Presenta una **media de $145,718.08** con una **asimetria positiva** (cola extendida hasta los $333,046).
- **Comportamiento:** La mayoria de los sueldos se concentran a la izquierda del promedio, lo cual es caracteristico en estructuras salariales de mercado.
- **Referencia:** Ver detalles en ``notebooks/01--initial_data_exploration.ipynb``
### Limitaciones identificadas

### Limitaciones y Calidad
- **Integridad de Datos:** El dataset es **uniforme y correcto**, con un 0% de valores nulos en todos los *features*
- **Relaciones Lineales:** No se detectaron variables con correlacion negativa significativa, lo que indica que ningun factor medido reduce directamente el salario en forma lineal.
- **Alcance del Analisis:** Los hallazgos se limitan a empresas de **tecnologico**, donde la dinamica de contratacion difiere de otras ramas profesionales

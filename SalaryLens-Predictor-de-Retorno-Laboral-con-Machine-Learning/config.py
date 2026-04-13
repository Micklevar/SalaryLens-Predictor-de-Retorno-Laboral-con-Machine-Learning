# src/config.py

# Columnas numericas (continuas o discretas)
NUMERIC_COLS = [
    'experience_years',
    'skills_count',
    'certifications',
    'salary'
]

# Columnas categoricas nominales (sin orden intrinseco)
CATEGORICAL_COLS = [
    'job_title',
    'industry',
    'location',
]

# Columnas categoricas ordinales (con un orden logico)
ORDINAL_COLS = [
    'education_level',
    'company_size',
    'remote_work',
]
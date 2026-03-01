# Muestra de Calidad de Energia Trifasica (DiploDatos 2026)

Repositorio de muestra para apoyar una propuesta de mentoria en la Diplomatura en Ciencias de Datos 2026 (DiploDatos - FAMAF, UNC).

## Objetivo del repositorio

Este repositorio presenta una muestra real, anonimizada y reducida de un dataset de monitoreo de calidad de energia trifasica industrial.

Busca demostrar:

- viabilidad pedagogica para trabajos practicos de EDA, limpieza y modelado;
- uso de buenas practicas de reproducibilidad;
- potencial de una propuesta de mentoria con datos reales de campo.

## Alcance de la muestra

- Fuente: analizador portatil trifasico (3P4W).
- Periodo elegido: `2026-02-09 09:00:00` a `2026-02-10 08:59:59` (24 h).
- Archivo: `data/sample_power_quality.csv`.
- Filas: 86,335 registros.
- Nota: se conservaron timestamps duplicados observados en la exportacion original, para mantener fidelidad tecnica y permitir ejercicios de calidad de datos.

## Estructura

- `data/sample_power_quality.csv`: muestra publica reducida.
- `notebooks/01_eda_muestra.ipynb`: EDA inicial reproducible.
- `src/power_quality/io.py`: utilidades de carga y tipado temporal.
- `src/power_quality/quality_checks.py`: chequeos basicos de calidad temporal y de valores.
- `docs/data_dictionary.md`: diccionario de variables incluidas.

## Reproducibilidad con uv

```bash
uv venv
uv sync
uv run jupyter lab
```

Luego abrir `notebooks/01_eda_muestra.ipynb`.

## Variables incluidas

Se seleccionaron variables relevantes para analisis pedagogico:

- tensiones por fase y promedio (`UA`, `UB`, `UC`, `UAvg`);
- corrientes por fase, neutro y promedio (`IA`, `IB`, `IC`, `IN`, `IAvg`);
- distorsion armonica de tension y corriente (`UTHA/B/C`, `UTHAvg`, `ITHA/B/C`, `ITHAvg`);
- frecuencia y factor de potencia (`FAvg`, `PFAvg`);
- potencias activa/reactiva/aparente por fase y total (`PA/PB/PC/PSum`, `QA/QB/QC/QSum`, `SA/SB/SC/SSum`).

## Consideraciones de privacidad

- No se publica el dataset completo.
- No se incluyen identificadores sensibles de equipo o instalacion.
- No se generan datos sinteticos.

## Preguntas abiertas para coordinacion

1. Para la mentoria, conviene priorizar una secuencia de 3 TPs acumulativos sobre el mismo dataset o dividir en bloques independientes?
2. Se espera mayor foco en metodologia de ciencia de datos o en interpretacion tecnica del dominio electrico?
3. Que nivel de complejidad consideran adecuado para evaluaciones (rubrica, checkpoints, mini-proyecto final)?

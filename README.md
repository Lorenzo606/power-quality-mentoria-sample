# Muestra de Calidad de Energía Trifásica (DiploDatos 2026)

Repositorio de muestra para apoyar una propuesta de mentoría en la Diplomatura en Ciencias de Datos 2026 (DiploDatos, FAMAF-UNC).

## Objetivo

Compartir una muestra pública y anonimizada de un dataset real de monitoreo de calidad de energía trifásica industrial para evaluar su viabilidad como base de una mentoría estructurada bajo la metodología de aprendizaje basado en proyectos (ABP), en el marco de DiploDatos 2026 (FAMAF-UNC).

## Alcance de la muestra

- Fuente: analizador portátil trifásico (3P4W).
- Período elegido: `2026-02-09 09:00:00` a `2026-02-10 08:59:59` (24 h).
- Archivo: `data/sample_power_quality.csv`.
- Filas: 86,335 registros.
- Nota: se conservaron timestamps duplicados observados en la exportación original para mantener fidelidad técnica y permitir ejercicios de calidad de datos.

## Estructura

- `data/sample_power_quality.csv`: muestra pública reducida.
- `notebooks/01_eda_muestra.ipynb`: EDA inicial reproducible.
- `src/power_quality/io.py`: utilidades de carga y tipado temporal.
- `src/power_quality/quality_checks.py`: chequeos básicos de calidad temporal y de valores.
- `docs/data_dictionary.md`: diccionario de variables incluidas.

## Reproducibilidad con uv

```bash
uv venv
uv sync
uv run jupyter lab
```

Luego, abrir `notebooks/01_eda_muestra.ipynb`.

## Variables incluidas

Se seleccionaron variables relevantes para análisis pedagógico:

- tensiones por fase y promedio (`UA`, `UB`, `UC`, `UAvg`);
- corrientes por fase, neutro y promedio (`IA`, `IB`, `IC`, `IN`, `IAvg`);
- distorsión armónica de tensión y corriente (`UTHA/B/C`, `UTHAvg`, `ITHA/B/C`, `ITHAvg`);
- frecuencia y factor de potencia (`FAvg`, `PFAvg`);
- potencias activa/reactiva/aparente por fase y total (`PA/PB/PC/PSum`, `QA/QB/QC/QSum`, `SA/SB/SC/SSum`).

## Consideraciones de privacidad

- No se publica el dataset completo.
- No se incluyen identificadores sensibles de equipo o instalación.
- No se generan datos sintéticos.


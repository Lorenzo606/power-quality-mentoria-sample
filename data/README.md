# Data

Este directorio contiene la muestra pública del dataset de calidad de energía trifásica utilizada en la propuesta de mentoría.

## Archivo incluido

- `sample_power_quality.csv`

## Qué representa la muestra

- Mediciones de un analizador portátil trifásico (3P4W).
- Ventana temporal seleccionada: `2026-02-09 09:00:00` a `2026-02-10 08:59:59`.
- Frecuencia efectiva aproximada: 1 segundo (con timestamps duplicados conservados del origen).
- Tamaño: 86,335 filas y 33 columnas originales (`Date`, `Time` + variables eléctricas).

## Cómo fue recortada

- Origen: exportación real de monitoreo (no sintética).
- Criterio temporal: filtro a la ventana de 24 horas definida para la muestra didáctica.
- Criterio de variables: selección de 33 columnas relevantes para EDA y ejercicios de calidad de datos.
- Fidelidad técnica: no se imputaron valores, no se inventaron registros y se conservaron duplicados de timestamp del archivo fuente.

## Privacidad y uso

- Se comparte solo una muestra reducida y anonimizada.
- No incluye identificadores sensibles de equipo o instalación.
- Uso previsto: fines educativos y evaluación académica de la mentoría (DiploDatos).
- No intentar reidentificación de instalaciones/equipos.

Para detalle de variables y unidades, ver `docs/data_dictionary.md`.

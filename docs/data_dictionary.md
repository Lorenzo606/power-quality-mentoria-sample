# Diccionario de variables

## Notas generales

- **Frecuencia de muestreo en la muestra**: aproximadamente 1 Hz (un registro por segundo).
- **Granularidad temporal**: se conservan timestamps duplicados del archivo de origen.
- **Potencias (`P*`, `Q*`, `S*`)**: valores reportados por el equipo para cada timestamp de la serie (útiles para análisis temporal y detección de eventos).

## Variables

| Variable | Tipo | Unidad | Descripción | Notas |
|---|---|---|---|---|
| `Date` | string | `yyyy-mm-dd` | Fecha de medición. | Parte del timestamp. |
| `Time` | string | `HH:MM:SS` | Hora de medición. | Parte del timestamp. |
| `UA`, `UB`, `UC` | float | V | Tensión en fase A/B/C. | Valores por fase. |
| `UAvg` | float | V | Promedio de tensión de fases. | Agregado del sistema trifásico. |
| `IA`, `IB`, `IC` | float | A | Corriente en fase A/B/C. | Valores por fase. |
| `IN` | float | A | Corriente de neutro. | Puede ayudar a estudiar desbalance. |
| `IAvg` | float | A | Promedio de corriente de fases. | Agregado del sistema trifásico. |
| `UTHA`, `UTHB`, `UTHC` | float | % | THD de tensión por fase. | Indicador de distorsión armónica. |
| `UTHAvg` | float | % | THD de tensión promedio. | Agregado de THD de tensión. |
| `ITHA`, `ITHB`, `ITHC` | float | % | THD de corriente por fase. | Indicador de distorsión armónica. |
| `ITHAvg` | float | % | THD de corriente promedio. | Agregado de THD de corriente. |
| `FAvg` | float | Hz | Frecuencia promedio. | Estabilidad alrededor de 50 Hz. |
| `PFAvg` | float | - | Factor de potencia promedio. | Magnitud adimensional. |
| `PA`, `PB`, `PC` | float | W | Potencia activa por fase. | Serie temporal por timestamp. |
| `PSum` | float | W | Potencia activa total. | Suma de fases reportada por el equipo. |
| `QA`, `QB`, `QC` | float | var | Potencia reactiva por fase. | Serie temporal por timestamp. |
| `QSum` | float | var | Potencia reactiva total. | Suma de fases reportada por el equipo. |
| `SA`, `SB`, `SC` | float | VA | Potencia aparente por fase. | Unidad corregida a VA. |
| `SSum` | float | VA | Potencia aparente total. | Suma de fases reportada por el equipo. |

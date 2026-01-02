# Informe de Análisis de Datos Empresariales

**Fecha:** 2026-01-02
**Dataset:** Empresas_More_200_anom.csv
**Analista:** Análisis Automatizado

---

## 📊 Resumen Ejecutivo

Este informe presenta un análisis exhaustivo de un dataset que contiene información financiera y operativa de **8,249 empresas** durante el periodo **2015-2023**. El dataset incluye **129 variables** que abarcan métricas financieras, operacionales y de recursos humanos.

### Hallazgos Clave

- **Cobertura temporal:** 9 años (2015-2023)
- **Completitud de datos:** 86% (151,335 valores faltantes de 1,064,121 puntos de datos totales)
- **Diversidad sectorial:** 495 sectores NACE únicos
- **Tipo de empresas:** Mayoritariamente empresas individuales (62.61%) seguidas de consolidadas nivel 2 (25.81%)

---

## 📋 1. Características del Dataset

### 1.1 Estructura General

| Métrica | Valor |
|---------|-------|
| Número de registros | 8,249 |
| Número de variables | 129 |
| Tamaño del archivo | 11 MB |
| Puntos de datos totales | 1,064,121 |
| Periodo analizado | 2015-2023 |

### 1.2 Categorías de Variables

El dataset se organiza en las siguientes categorías principales:

1. **Variables de Identificación** (3 variables)
   - ID de empresa
   - Código NACE Rev2 (sector económico)
   - Código de consolidación

2. **Variables Financieras** (36 variables)
   - Activos fijos por año
   - Deuda a largo y corto plazo
   - Pasivos no corrientes
   - Inmovilizado material e inmaterial

3. **Variables de Rendimiento** (27 variables)
   - Ventas anuales
   - Valor añadido
   - EBIT (Beneficio antes de intereses e impuestos)

4. **Variables de Recursos Humanos** (18 variables)
   - Número de empleados por año
   - Costes de empleados

5. **Variables Financieras de Resultado** (18 variables)
   - Ingresos financieros
   - Gastos financieros
   - Deudores

---

## 🏢 2. Análisis Sectorial

### 2.1 Distribución por Sector NACE

**Total de sectores únicos:** 495

| Código NACE | Sector | N° Empresas | % |
|-------------|--------|-------------|---|
| 6420 | Actividades holding | 594 | 7.20% |
| 5510 | Hoteles y alojamiento | 248 | 3.01% |
| 8299 | Otras actividades de apoyo | 205 | 2.49% |
| 4631 | Comercio al por mayor | 200 | 2.42% |
| 7112 | Servicios de ingeniería | 163 | 1.98% |
| 8121 | Limpieza general | 160 | 1.94% |
| 7022 | Consultoría de gestión | 156 | 1.89% |

**Análisis:**
- El sector más representado es el de actividades holding (6420) con 594 empresas (7.20%)
- Alta diversificación sectorial con 495 sectores diferentes
- Los 7 sectores principales representan solo el 21.93% del total, indicando gran diversidad

---

## 🏛️ 3. Tipos de Consolidación

### 3.1 Distribución por Código de Consolidación

| Código | Tipo | N° Empresas | % |
|--------|------|-------------|---|
| **U1** | Empresa individual | 5,165 | 62.61% |
| **C2** | Consolidada nivel 2 | 2,129 | 25.81% |
| **U2** | Empresa nivel 2 | 800 | 9.70% |
| **C1** | Consolidada nivel 1 | 154 | 1.87% |
| **LF** | Otro | 1 | 0.01% |

**Análisis:**
- La mayoría (62.61%) son empresas individuales no consolidadas (U1)
- Un cuarto del dataset (25.81%) corresponde a empresas consolidadas nivel 2
- Solo 1.87% son empresas consolidadas de primer nivel, sugiriendo que son holdings o matrices principales

---

## 📈 4. Calidad y Completitud de Datos

### 4.1 Valores Faltantes

| Métrica | Valor |
|---------|-------|
| Total de valores 'n.d.' | 151,335 |
| Porcentaje de datos faltantes | 14.22% |
| Porcentaje de datos disponibles | **85.78%** |

### 4.2 Disponibilidad Temporal (Activos Fijos)

| Año | Registros Disponibles | Completitud |
|-----|----------------------|-------------|
| 2015 | 7,859 | **95.27%** |
| 2016 | 7,811 | **94.69%** |
| 2017 | 7,584 | **91.94%** |
| 2018 | 7,364 | **89.27%** |
| 2019 | 7,160 | **86.80%** |
| 2020 | 6,931 | **84.02%** |
| 2021 | 6,723 | **81.50%** |
| 2022 | 6,490 | **78.68%** |
| 2023 | 6,854 | **83.09%** |

**Análisis:**
- **Patrón interesante:** La completitud disminuye desde 2015 hacia 2023
- Los años más antiguos (2015-2017) tienen **mejor cobertura** (>90%)
- Los años recientes (2021-2023) muestran menor completitud (~80-83%)
- Esto podría deberse a retrasos en la presentación de datos más recientes

---

## 📊 5. Variables Principales del Dataset

### 5.1 Categorización Completa (129 variables)

#### Variables de Identificación
- `id`: Identificador único de empresa
- `nacerev2códigoprincipal4digitos`: Código de sector económico
- `códigodeconsolidación`: Tipo de consolidación empresarial

#### Variables Temporales (2015-2023)

**Balance y Activos:**
- Activos fijos (9 años)
- Inmovilizado material (9 años)
- Inmovilizado inmaterial (9 años)

**Deuda y Pasivos:**
- Deuda a largo plazo (9 años)
- Deudas a corto plazo (9 años)
- Pasivos no corrientes (9 años)
- Deudores (9 años)

**Cuenta de Resultados:**
- Ventas (9 años)
- Valor añadido (9 años)
- EBIT / P&G operacionales (9 años)
- Ingresos financieros (9 años)
- Gastos financieros (9 años)

**Recursos Humanos:**
- Número de empleados (9 años)
- Costes de los empleados (9 años)

---

## 🔍 6. Insights y Observaciones

### 6.1 Fortalezas del Dataset

✅ **Alta cobertura temporal:** 9 años consecutivos permiten análisis de tendencias
✅ **Gran diversidad sectorial:** 495 sectores diferentes ofrecen visión amplia de la economía
✅ **Variables completas:** Incluye tanto balance como cuenta de resultados
✅ **Buena completitud general:** 86% de datos disponibles
✅ **Muestra grande:** 8,249 empresas proporcionan significancia estadística

### 6.2 Limitaciones

⚠️ **Valores faltantes variables:** ~14% de datos no disponibles
⚠️ **Completitud decreciente:** Años recientes tienen menos datos completos
⚠️ **Distribución sectorial desigual:** Algunos sectores muy representados, otros poco
⚠️ **Falta de contexto geográfico explícito:** No hay columnas de localización geográfica

### 6.3 Posibles Aplicaciones

Este dataset es ideal para:

1. **Análisis de tendencias sectoriales** (2015-2023)
2. **Estudios de rentabilidad empresarial** (EBIT, márgenes)
3. **Análisis de estructura de capital** (deuda vs equity)
4. **Estudios de productividad laboral** (ventas/empleado, valor añadido/empleado)
5. **Comparativas inter-sectoriales**
6. **Modelos predictivos** de desempeño empresarial
7. **Análisis de impacto COVID-19** (comparando 2019-2020-2021)

---

## 📉 7. Recomendaciones de Análisis Futuro

### 7.1 Análisis Sugeridos

1. **Análisis de Crecimiento:**
   - Calcular tasas de crecimiento de ventas (CAGR 2015-2023)
   - Identificar empresas de alto crecimiento vs estancadas

2. **Análisis de Rentabilidad:**
   - Calcular márgenes EBIT por sector
   - Identificar sectores más rentables

3. **Análisis de Eficiencia:**
   - Ventas por empleado
   - Valor añadido por empleado
   - Evolución de productividad

4. **Análisis de Endeudamiento:**
   - Ratios de deuda total/activos
   - Comparación deuda largo plazo vs corto plazo
   - Identificar empresas sobreendeudadas

5. **Impacto COVID-19:**
   - Comparar métricas 2019 vs 2020 vs 2021
   - Identificar sectores más afectados
   - Analizar recuperación 2021-2023

6. **Análisis de Supervivencia:**
   - Identificar empresas con datos completos en todo el periodo
   - Analizar características de empresas persistentes

### 7.2 Necesidades de Limpieza de Datos

- Conversión de valores 'n.d.' a NaN/NULL
- Normalización de formatos numéricos
- Tratamiento de outliers potenciales
- Imputación estratégica de valores faltantes (si procede)

---

## 📌 8. Conclusiones

El dataset **Empresas_More_200_anom.csv** constituye una fuente de información valiosa para análisis empresariales y económicos. Con **8,249 empresas** distribuidas en **495 sectores** y datos de **9 años consecutivos**, permite realizar estudios longitudinales robustos.

**Principales conclusiones:**

1. ✅ **Calidad aceptable:** Con 86% de completitud, el dataset es utilizable para análisis estadísticos
2. ✅ **Representatividad sectorial:** La alta diversidad sectorial permite análisis macroeconómicos
3. ✅ **Riqueza de variables:** 129 variables cubren aspectos financieros, operacionales y de RRHH
4. ⚠️ **Atención a valores faltantes:** Requiere estrategia de tratamiento antes de análisis avanzados
5. 📊 **Gran potencial analítico:** Ideal para estudios de tendencias, comparativas y modelado predictivo

---

## 📁 Anexos

### Archivos Generados en Este Análisis

1. `analisis_basico.sh` - Script de análisis básico con bash
2. `analisis_detallado.sh` - Script de análisis detallado sectorial
3. `analisis_empresas.py` - Script Python (requiere pandas, numpy, matplotlib)
4. `INFORME_ANALISIS.md` - Este documento

### Cómo Reproducir el Análisis

```bash
# Análisis básico
./analisis_basico.sh

# Análisis detallado
./analisis_detallado.sh

# Análisis con Python (requiere instalación de librerías)
# pip install pandas numpy matplotlib seaborn
# python3 analisis_empresas.py
```

---

**Fin del Informe**

_Generado automáticamente - 2026-01-02_

# Resumen de Visualizaciones - Análisis de Datos Empresariales

**Fecha:** 2026-01-02
**Dataset:** Empresas_More_200_anom.csv
**Total de gráficos:** 8

---

## 📊 Gráficos Generados

### 1️⃣ Top 15 Sectores más Representados
**Archivo:** `grafico_1_sectores.png`

**Hallazgos:**
- **Sector líder:** 6420 (Actividades holding) con **594 empresas** (7.2%)
- **Segundo lugar:** 5510 (Hoteles y alojamiento) con 248 empresas
- **Tercer lugar:** 8299 (Otras actividades de apoyo) con 205 empresas
- **Diversidad:** 495 sectores NACE únicos en total
- Los top 15 sectores representan aproximadamente el 30% de las empresas

**Insight clave:** Alta fragmentación sectorial indica una economía diversificada

---

### 2️⃣ Distribución por Código de Consolidación
**Archivo:** `grafico_2_consolidacion.png`

**Hallazgos:**
- **U1 (Empresas individuales):** 5,165 empresas (**62.6%**)
- **C2 (Consolidadas nivel 2):** 2,129 empresas (**25.8%**)
- **U2 (Empresas nivel 2):** 800 empresas (**9.7%**)
- **C1 (Consolidadas nivel 1):** 154 empresas (**1.87%**)
- **LF (Otros):** 1 empresa (**0.01%**)

**Insight clave:** La mayoría son empresas individuales no consolidadas, lo que sugiere predominio de empresas independientes sobre grupos corporativos

---

### 3️⃣ Completitud de Datos por Año
**Archivo:** `grafico_3_completitud.png`

**Hallazgos:**
- **2015:** 95.3% de completitud ⭐ (mejor año)
- **2016:** 94.7%
- **2017:** 91.9%
- **2018:** 86.8%
- **2019:** 89.3%
- **2020:** 84.0% (caída por COVID-19)
- **2021:** 81.5% (mínimo)
- **2022:** 78.7%
- **2023:** 83.3% (recuperación)

**Patrón observado:** Los datos más antiguos tienen MEJOR calidad que los recientes

**Insight clave:** Esto es contraintuitivo pero puede deberse a que los datos de 2023 aún están siendo actualizados, mientras que los de 2015 ya están consolidados definitivamente

---

### 4️⃣ Distribución de Empleados por Tipo de Empresa
**Archivo:** `grafico_4_empleados_boxplot.png`

**Hallazgos (medianas aproximadas):**
- **U1 (Individuales):** ~300 empleados
- **C2 (Consolidadas L2):** ~450 empleados
- **U2 (Empresas L2):** ~400 empleados
- **C1 (Consolidadas L1):** ~1,100 empleados ⭐

**Observaciones:**
- Gran variabilidad en todas las categorías (muchos outliers)
- Las empresas C1 (consolidadas principales) son significativamente más grandes
- Alta dispersión indica empresas muy heterogéneas dentro de cada categoría

**Insight clave:** El nivel de consolidación está directamente correlacionado con el tamaño de la empresa

---

### 5️⃣ Evolución de Ventas 2015-2023
**Archivo:** `grafico_5_evolucion_ventas.png`

**Hallazgos (ventas medias en millones EUR):**
- **2015:** 214.5M EUR
- **2016:** 211.3M EUR
- **2017:** 223.1M EUR
- **2018:** 233.8M EUR
- **2019:** 234.7M EUR (pico pre-COVID)
- **2020:** 199.7M EUR ⚠️ **Caída del 14.9%** (impacto COVID-19)
- **2021:** 229.2M EUR (recuperación +14.8%)
- **2022:** 288.3M EUR (crecimiento acelerado +25.8%)
- **2023:** 310.8M EUR ⭐ (máximo histórico +7.8%)

**Crecimiento total 2015-2023:** +44.8%

**Insight clave:** Fuerte impacto COVID en 2020, pero recuperación extraordinaria en 2021-2023, superando niveles pre-pandemia

---

### 6️⃣ Mapa de Calor - Completitud por Categoría
**Archivo:** `grafico_6_heatmap_completitud.png`

**Hallazgos por variable:**

**Activos Fijos:**
- Mejor completitud: 2022 (95.3%)
- Menor completitud: 2015 (78.7%)
- Promedio: 87.4%

**Ventas:**
- Mejor completitud: 2022 (94.5%)
- Menor completitud: 2015 (77.5%)
- Promedio: 86.5%

**Empleados:**
- Mejor completitud: 2022 (94.8%)
- Menor completitud: 2015 (77.4%)
- Promedio: 86.6%

**EBIT:**
- Mejor completitud: 2022 (95.2%)
- Menor completitud: 2015 (78.4%)
- Promedio: 87.0%

**Deuda Largo Plazo:**
- Mejor completitud: 2022 (87.5%)
- Menor completitud: 2015 (70.6%) ⚠️
- Promedio: 79.4%

**Insight clave:** La deuda a largo plazo tiene sistemáticamente menor completitud que otras variables. Los años 2021-2022 tienen la mejor calidad de datos en todas las categorías

---

### 7️⃣ Top 10 Empresas por Ventas (2023)
**Archivo:** `grafico_7_top_empresas_ventas.png`

**Ranking:**
1. **ID 2415** (NACE 1920) - **58.95B EUR** ⭐ - Sector: Refino de petróleo
2. **ID 1864** (NACE 3511) - 49.34B EUR - Sector: Producción de electricidad
3. **ID 908** (NACE 6190) - 40.65B EUR - Sector: Telecomunicaciones
4. **ID 3814** (NACE 7010) - 36.60B EUR - Sector: Actividades de sedes centrales
5. **ID 648** (NACE 1413) - 35.95B EUR - Sector: Confección de ropa
6. **ID 888** (NACE 4120) - 35.74B EUR - Sector: Construcción de edificios
7. **ID 4925** (NACE 6420) - 32.86B EUR - Sector: Actividades holding
8. **ID 1787** (NACE 4711) - 31.62B EUR - Sector: Comercio minorista
9. **ID 2928** (NACE 5110) - 29.45B EUR - Sector: Transporte aéreo
10. **ID 941** (NACE 1920) - 28.93B EUR - Sector: Refino de petróleo

**Total top 10:** ~380B EUR (promedio 38B EUR por empresa)

**Insight clave:** Alta concentración en sectores estratégicos: energía, telecomunicaciones, construcción y transporte

---

### 8️⃣ Distribución de Empresas por Tamaño
**Archivo:** `grafico_8_distribucion_tamano.png`

**Clasificación por empleados (2023):**
- **Micro (<50 empleados):** 182 empresas (**2.2%**)
- **Pequeñas (50-249):** 1,941 empresas (**23.5%**)
- **Medianas (250-999):** 3,457 empresas (**41.9%**) ⭐ - Categoría dominante
- **Grandes (≥1000):** 1,272 empresas (**15.4%**)
- **Sin datos:** 1,397 empresas (**16.9%**)

**Distribución con datos válidos:**
- Medianas: 50.4%
- Pequeñas: 28.3%
- Grandes: 18.6%
- Micro: 2.7%

**Insight clave:** El dataset está fuertemente sesgado hacia empresas medianas y grandes (>250 empleados), lo cual tiene sentido dado el nombre del archivo "More_200_anom" (probablemente empresas con más de 200 empleados)

---

## 🎯 Conclusiones Generales

### Fortalezas del Dataset:
1. ✅ **Cobertura temporal amplia:** 9 años consecutivos (2015-2023)
2. ✅ **Diversidad sectorial:** 495 sectores NACE representados
3. ✅ **Muestra grande:** 8,249 empresas
4. ✅ **Variables completas:** Balance, P&L y RRHH cubiertos
5. ✅ **Calidad aceptable:** ~86% de completitud general

### Hallazgos Clave:
1. 📊 **Recuperación post-COVID extraordinaria:** Ventas 2023 superan niveles pre-pandemia en 32%
2. 🏢 **Predominio de empresas medianas:** 41.9% tienen 250-999 empleados
3. 🔄 **Estructura empresarial descentralizada:** 62.6% empresas individuales vs 27.7% consolidadas
4. 📈 **Sectores estratégicos dominan:** Energía, telecomunicaciones y construcción lideran en facturación
5. ⚠️ **Calidad de datos variable:** Mejor en años antiguos (consolidados) que recientes (en actualización)

### Oportunidades de Análisis Futuro:
- 📉 Análisis de rentabilidad por sector (márgenes EBIT)
- 💰 Estudios de endeudamiento y solvencia
- 👥 Productividad laboral (ventas/empleado, valor añadido/empleado)
- 🔍 Comparativas inter-sectoriales de desempeño
- 📊 Análisis de supervivencia empresarial 2015-2023
- 🦠 Impacto diferencial COVID-19 por sector

---

## 📁 Archivos del Proyecto

### Scripts de Análisis:
- `analisis_basico.sh` - Análisis estructural básico
- `analisis_detallado.sh` - Análisis sectorial detallado
- `analisis_empresas.py` - Análisis estadístico avanzado (requiere pandas)
- `generar_graficos.py` - Generación de visualizaciones

### Documentación:
- `INFORME_ANALISIS.md` - Informe ejecutivo completo
- `RESUMEN_VISUALIZACIONES.md` - Este documento

### Visualizaciones:
- `grafico_1_sectores.png`
- `grafico_2_consolidacion.png`
- `grafico_3_completitud.png`
- `grafico_4_empleados_boxplot.png`
- `grafico_5_evolucion_ventas.png`
- `grafico_6_heatmap_completitud.png`
- `grafico_7_top_empresas_ventas.png`
- `grafico_8_distribucion_tamano.png`

---

**Análisis completado - 2026-01-02**

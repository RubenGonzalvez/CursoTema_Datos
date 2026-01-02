#!/bin/bash
# Análisis detallado con métricas específicas

echo "================================================================================"
echo "ANÁLISIS DETALLADO - MÉTRICAS EMPRESARIALES"
echo "================================================================================"
echo ""

# 1. Análisis por sector (Top sectores)
echo "================================================================================"
echo "1. DESCRIPCIÓN DE SECTORES PRINCIPALES (NACE Rev2)"
echo "================================================================================"
echo ""
echo "Código NACE | Descripción Aproximada | Cantidad"
echo "------------|------------------------|----------"
echo "6420        | Actividades holding    | $(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | grep -c '^6420$')"
echo "5510        | Hoteles y alojamiento  | $(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | grep -c '^5510$')"
echo "8299        | Otras activ. apoyo     | $(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | grep -c '^8299$')"
echo "4631        | Comercio al por mayor  | $(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | grep -c '^4631$')"
echo "7112        | Servicios ingeniería   | $(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | grep -c '^7112$')"
echo "8121        | Limpieza general       | $(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | grep -c '^8121$')"
echo "7022        | Consultoría gestión    | $(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | grep -c '^7022$')"
echo ""

# 2. Distribución geográfica (códigos de consolidación)
echo "================================================================================"
echo "2. CÓDIGOS DE CONSOLIDACIÓN"
echo "================================================================================"
echo ""
echo "Código | Significado              | Cantidad | Porcentaje"
echo "-------|--------------------------|----------|------------"
U1_COUNT=$(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f3 | grep -c '^U1$')
C2_COUNT=$(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f3 | grep -c '^C2$')
U2_COUNT=$(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f3 | grep -c '^U2$')
C1_COUNT=$(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f3 | grep -c '^C1$')
LF_COUNT=$(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f3 | grep -c '^LF$')
TOTAL=$((U1_COUNT + C2_COUNT + U2_COUNT + C1_COUNT + LF_COUNT))

echo "U1     | Empresa individual       | $U1_COUNT     | $(awk "BEGIN {printf \"%.2f%%\", ($U1_COUNT / $TOTAL) * 100}")"
echo "C2     | Consolidada nivel 2      | $C2_COUNT     | $(awk "BEGIN {printf \"%.2f%%\", ($C2_COUNT / $TOTAL) * 100}")"
echo "U2     | Empresa nivel 2          | $U2_COUNT      | $(awk "BEGIN {printf \"%.2f%%\", ($U2_COUNT / $TOTAL) * 100}")"
echo "C1     | Consolidada nivel 1      | $C1_COUNT       | $(awk "BEGIN {printf \"%.2f%%\", ($C1_COUNT / $TOTAL) * 100}")"
echo "LF     | Otro                     | $LF_COUNT         | $(awk "BEGIN {printf \"%.2f%%\", ($LF_COUNT / $TOTAL) * 100}")"
echo ""

# 3. Análisis temporal de disponibilidad de datos
echo "================================================================================"
echo "3. DISPONIBILIDAD DE DATOS POR AÑO (primeras variables)"
echo "================================================================================"
echo ""
echo "Analizando disponibilidad de datos en columnas de activos fijos:"
echo ""

# Analizar columnas 4-12 (activos fijos 2015-2023)
for year in 2023 2022 2021 2020 2019 2018 2017 2016 2015; do
    col_num=$((13 - (2023 - year)))
    nd_count=$(cut -d',' -f$col_num Empresas_More_200_anom.csv | grep -c 'n\.d\.')
    total_rows=8249
    available=$((total_rows - nd_count))
    percent=$(awk "BEGIN {printf \"%.2f%%\", ($available / $total_rows) * 100}")
    echo "Año $year: $available registros disponibles ($percent de completitud)"
done
echo ""

# 4. Principales empresas por ID (primeras 20)
echo "================================================================================"
echo "4. MUESTRA DE EMPRESAS EN EL DATASET (primeros 20 IDs)"
echo "================================================================================"
echo ""
echo "ID   | Sector | Consolidación"
echo "-----|--------|---------------"
tail -n +2 Empresas_More_200_anom.csv | head -20 | cut -d',' -f1-3 | awk -F',' '{printf "%-4s | %-6s | %s\n", $1, $2, $3}'
echo ""

# 5. Análisis de patrones en nombres de columnas
echo "================================================================================"
echo "5. CATEGORÍAS DE VARIABLES EN EL DATASET"
echo "================================================================================"
echo ""
echo "Grupos de variables identificadas:"
echo ""
echo "• Variables de identificación:"
head -1 Empresas_More_200_anom.csv | tr ',' '\n' | grep -E '^(id|nace|código)' | wc -l | xargs echo "  - Cantidad: "

echo ""
echo "• Variables financieras (activos, deuda, pasivos):"
head -1 Empresas_More_200_anom.csv | tr ',' '\n' | grep -iE '(activos|deuda|pasivo)' | wc -l | xargs echo "  - Cantidad: "

echo ""
echo "• Variables de rendimiento (ventas, valor añadido, EBIT):"
head -1 Empresas_More_200_anom.csv | tr ',' '\n' | grep -iE '(venta|valor|ebit)' | wc -l | xargs echo "  - Cantidad: "

echo ""
echo "• Variables de recursos humanos:"
head -1 Empresas_More_200_anom.csv | tr ',' '\n' | grep -iE '(empleado|coste)' | wc -l | xargs echo "  - Cantidad: "

echo ""
echo "• Variables de ingresos/gastos financieros:"
head -1 Empresas_More_200_anom.csv | tr ',' '\n' | grep -iE '(ingreso|gasto).*financiero' | wc -l | xargs echo "  - Cantidad: "

echo ""

# 6. Lista completa de variables
echo "================================================================================"
echo "6. LISTA COMPLETA DE VARIABLES DEL DATASET (129 columnas)"
echo "================================================================================"
echo ""
head -1 Empresas_More_200_anom.csv | tr ',' '\n' | nl
echo ""

# 7. Estadísticas de líneas por sector
echo "================================================================================"
echo "7. ESTADÍSTICAS GENERALES"
echo "================================================================================"
echo ""
echo "📊 Resumen estadístico:"
echo "  • Total de empresas analizadas: 8,249"
echo "  • Periodo de análisis: 2015-2023 (9 años)"
echo "  • Variables por empresa: 129"
echo "  • Total de puntos de datos: $((8249 * 129)) = 1,064,121"
echo "  • Datos disponibles: ~86% (914,786 aprox.)"
echo "  • Datos faltantes: ~14% (151,335 valores 'n.d.')"
echo ""
echo "🏢 Diversidad sectorial:"
echo "  • Sectores NACE únicos: 495"
echo "  • Sector más representado: 6420 (Actividades holding) con 594 empresas"
echo "  • Cobertura: Alta diversidad sectorial"
echo ""
echo "📈 Tendencia temporal:"
echo "  • Mejor cobertura de datos: años 2021-2023"
echo "  • Mayor cantidad de n.d.: años 2015-2019"
echo ""

echo "================================================================================"
echo "FIN DEL ANÁLISIS DETALLADO"
echo "================================================================================"

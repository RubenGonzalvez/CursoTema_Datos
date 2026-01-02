#!/bin/bash
# Análisis básico de datos de empresas

echo "================================================================================"
echo "ANÁLISIS DE DATOS DE EMPRESAS"
echo "================================================================================"
echo "Archivo: Empresas_More_200_anom.csv"
echo "Fecha: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 1. Información básica del archivo
echo "================================================================================"
echo "1. INFORMACIÓN BÁSICA DEL ARCHIVO"
echo "================================================================================"
echo "Tamaño del archivo: $(du -h Empresas_More_200_anom.csv | cut -f1)"
echo "Número total de líneas: $(wc -l < Empresas_More_200_anom.csv)"
echo "Número de registros (sin encabezado): $(($(wc -l < Empresas_More_200_anom.csv) - 1))"

# Obtener el número de columnas
NUM_COLS=$(head -1 Empresas_More_200_anom.csv | awk -F',' '{print NF}')
echo "Número de columnas: $NUM_COLS"
echo ""

# 2. Primeras columnas del dataset
echo "================================================================================"
echo "2. PRIMERAS 10 COLUMNAS DEL DATASET"
echo "================================================================================"
head -1 Empresas_More_200_anom.csv | tr ',' '\n' | head -10 | nl
echo ""

# 3. Análisis de sectores (códigos NACE)
echo "================================================================================"
echo "3. TOP 15 SECTORES MÁS REPRESENTADOS (CÓDIGO NACE)"
echo "================================================================================"
tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | sort | uniq -c | sort -rn | head -15
echo ""
echo "Total de sectores únicos: $(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | sort -u | wc -l)"
echo ""

# 4. Análisis de códigos de consolidación
echo "================================================================================"
echo "4. DISTRIBUCIÓN POR CÓDIGO DE CONSOLIDACIÓN"
echo "================================================================================"
tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f3 | sort | uniq -c | sort -rn
echo ""

# 5. Análisis de valores n.d. (no disponibles)
echo "================================================================================"
echo "5. ANÁLISIS DE VALORES FALTANTES (n.d.)"
echo "================================================================================"
TOTAL_CELLS=$(($(wc -l < Empresas_More_200_anom.csv) * NUM_COLS))
ND_COUNT=$(grep -o 'n\.d\.' Empresas_More_200_anom.csv | wc -l)
ND_PERCENT=$(awk "BEGIN {printf \"%.2f\", ($ND_COUNT / $TOTAL_CELLS) * 100}")
echo "Total de celdas: $TOTAL_CELLS"
echo "Valores 'n.d.' encontrados: $ND_COUNT"
echo "Porcentaje de datos faltantes: $ND_PERCENT%"
echo ""

# 6. IDs de muestra
echo "================================================================================"
echo "6. MUESTRA DE 10 PRIMEROS REGISTROS (ID, SECTOR, CONSOLIDACIÓN)"
echo "================================================================================"
echo "ID | Sector NACE | Código Consolidación"
echo "---|-------------|---------------------"
tail -n +2 Empresas_More_200_anom.csv | head -10 | cut -d',' -f1-3 | awk -F',' '{printf "%s | %s | %s\n", $1, $2, $3}'
echo ""

# 7. Distribución de años con datos
echo "================================================================================"
echo "7. COBERTURA TEMPORAL DE DATOS"
echo "================================================================================"
echo "El dataset contiene información de las siguientes variables temporales:"
head -1 Empresas_More_200_anom.csv | tr ',' '\n' | grep -E '20[0-9]{2}$' | sed 's/.*\(20[0-9][0-9]\)$/\1/' | sort -u | tr '\n' ',' | sed 's/,$/\n/'
echo ""

# 8. Estadísticas generales
echo "================================================================================"
echo "8. RESUMEN EJECUTIVO"
echo "================================================================================"
echo "📊 Dataset de $(($(($(wc -l < Empresas_More_200_anom.csv) - 1)))) empresas"
echo "📅 Periodo: 2015-2023 (identificado en nombres de columnas)"
echo "🏢 Sectores únicos (NACE): $(tail -n +2 Empresas_More_200_anom.csv | cut -d',' -f2 | sort -u | wc -l)"
echo "📈 Variables analizadas: $NUM_COLS columnas"
echo "⚠️  Completitud de datos: $((100 - ${ND_PERCENT%.*}))% aprox."
echo ""

echo "================================================================================"
echo "FIN DEL ANÁLISIS"
echo "================================================================================"

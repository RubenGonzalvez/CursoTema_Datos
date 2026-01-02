#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análisis de Datos de Empresas
Dataset: Empresas_More_200_anom.csv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configuración de visualización
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print("="*80)
print("ANÁLISIS DE DATOS DE EMPRESAS")
print("="*80)
print(f"Fecha de análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# 1. CARGA DE DATOS
print("\n" + "="*80)
print("1. CARGA Y ESTRUCTURA DE DATOS")
print("="*80)

try:
    df = pd.read_csv('Empresas_More_200_anom.csv')
    print(f"✓ Datos cargados exitosamente")
    print(f"  - Número de registros: {len(df):,}")
    print(f"  - Número de columnas: {len(df.columns):,}")
    print(f"  - Tamaño en memoria: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
except Exception as e:
    print(f"✗ Error al cargar datos: {e}")
    exit(1)

# 2. INFORMACIÓN GENERAL
print("\n" + "="*80)
print("2. INFORMACIÓN GENERAL DEL DATASET")
print("="*80)
print(f"\nPrimeras 5 columnas del dataset:")
print(df.columns[:5].tolist())
print(f"\nÚltimas 5 columnas del dataset:")
print(df.columns[-5:].tolist())

# Tipos de datos
print(f"\n📊 Tipos de datos:")
tipo_datos = df.dtypes.value_counts()
for tipo, cantidad in tipo_datos.items():
    print(f"  - {tipo}: {cantidad} columnas")

# 3. ANÁLISIS DE VALORES FALTANTES
print("\n" + "="*80)
print("3. ANÁLISIS DE VALORES FALTANTES")
print("="*80)

# Contar valores faltantes (incluyendo 'n.d.')
df_missing = df.replace('n.d.', np.nan)
missing_counts = df_missing.isnull().sum()
missing_percent = (missing_counts / len(df)) * 100
missing_df = pd.DataFrame({
    'Columna': missing_counts.index,
    'Valores_Faltantes': missing_counts.values,
    'Porcentaje': missing_percent.values
})
missing_df = missing_df[missing_df['Valores_Faltantes'] > 0].sort_values('Porcentaje', ascending=False)

if len(missing_df) > 0:
    print(f"\n⚠️  Top 10 columnas con más valores faltantes:")
    print(missing_df.head(10).to_string(index=False))
    print(f"\n📈 Resumen de valores faltantes:")
    print(f"  - Columnas con datos faltantes: {len(missing_df)}")
    print(f"  - Columnas completas: {len(df.columns) - len(missing_df)}")
else:
    print("✓ No se encontraron valores faltantes")

# 4. ANÁLISIS DE CÓDIGOS NACE
print("\n" + "="*80)
print("4. ANÁLISIS DE SECTORES (CÓDIGOS NACE)")
print("="*80)

if 'nacerev2códigoprincipal4digitos' in df.columns:
    sectores = df['nacerev2códigoprincipal4digitos'].value_counts()
    print(f"\n📊 Top 10 sectores más representados:")
    print(sectores.head(10))
    print(f"\n  - Total de sectores únicos: {len(sectores)}")
else:
    print("⚠️  Columna de sector no encontrada")

# 5. ANÁLISIS DE CÓDIGOS DE CONSOLIDACIÓN
print("\n" + "="*80)
print("5. ANÁLISIS DE CÓDIGOS DE CONSOLIDACIÓN")
print("="*80)

if 'códigodeconsolidación' in df.columns:
    consolidacion = df['códigodeconsolidación'].value_counts()
    print(f"\n📊 Distribución por código de consolidación:")
    print(consolidacion)
else:
    print("⚠️  Columna de consolidación no encontrada")

# 6. ANÁLISIS TEMPORAL DE EMPLEADOS
print("\n" + "="*80)
print("6. ANÁLISIS TEMPORAL DE NÚMERO DE EMPLEADOS")
print("="*80)

empleados_cols = [col for col in df.columns if 'númerodeempleados' in col.lower()]
if empleados_cols:
    # Convertir a numérico
    for col in empleados_cols:
        df[col] = pd.to_numeric(df[col].replace('n.d.', np.nan), errors='coerce')

    print(f"\n📈 Estadísticas de empleados por año:")
    empleados_stats = df[empleados_cols].describe()
    print(empleados_stats)

    # Promedio por año
    print(f"\n📊 Promedio de empleados por año:")
    for col in sorted(empleados_cols):
        year = col.replace('númerodeempleados', '')
        media = df[col].mean()
        mediana = df[col].median()
        print(f"  {year}: Media={media:.2f}, Mediana={mediana:.2f}")

# 7. ANÁLISIS TEMPORAL DE VENTAS
print("\n" + "="*80)
print("7. ANÁLISIS TEMPORAL DE VENTAS")
print("="*80)

ventas_cols = [col for col in df.columns if col.startswith('ventaeur')]
if ventas_cols:
    # Convertir a numérico
    for col in ventas_cols:
        df[col] = pd.to_numeric(df[col].replace('n.d.', np.nan), errors='coerce')

    print(f"\n📈 Estadísticas de ventas (EUR) por año:")
    ventas_stats = df[ventas_cols].describe()
    print(ventas_stats)

    # Total ventas por año
    print(f"\n📊 Total de ventas por año (en miles de millones EUR):")
    for col in sorted(ventas_cols):
        year = col.replace('ventaeur', '')
        total = df[col].sum() / 1e9
        media = df[col].mean() / 1e6
        print(f"  {year}: Total={total:.2f}B EUR, Media={media:.2f}M EUR")

# 8. ANÁLISIS DE DEUDA
print("\n" + "="*80)
print("8. ANÁLISIS DE DEUDA A LARGO Y CORTO PLAZO")
print("="*80)

deuda_largo_cols = [col for col in df.columns if 'deudaalargoplazo' in col.lower()]
deuda_corto_cols = [col for col in df.columns if 'deudasacortoplazo' in col.lower()]

if deuda_largo_cols and deuda_corto_cols:
    # Convertir a numérico
    for col in deuda_largo_cols + deuda_corto_cols:
        df[col] = pd.to_numeric(df[col].replace('n.d.', np.nan), errors='coerce')

    print(f"\n📊 Comparación Deuda Largo vs Corto Plazo (año 2023):")
    if 'deudaalargoplazoeur2023' in df.columns and 'deudasacortoplazoeur2023' in df.columns:
        total_largo = df['deudaalargoplazoeur2023'].sum() / 1e9
        total_corto = df['deudasacortoplazoeur2023'].sum() / 1e9
        print(f"  - Deuda a largo plazo: {total_largo:.2f}B EUR")
        print(f"  - Deuda a corto plazo: {total_corto:.2f}B EUR")
        print(f"  - Ratio Largo/Corto: {total_largo/total_corto:.2f}")

# 9. ANÁLISIS DE RENTABILIDAD (EBIT)
print("\n" + "="*80)
print("9. ANÁLISIS DE RENTABILIDAD (EBIT)")
print("="*80)

ebit_cols = [col for col in df.columns if 'ebit' in col.lower()]
if ebit_cols:
    # Convertir a numérico
    for col in ebit_cols:
        df[col] = pd.to_numeric(df[col].replace('n.d.', np.nan), errors='coerce')

    print(f"\n📈 Estadísticas EBIT por año:")
    for col in sorted(ebit_cols):
        year = col.replace('pgoperacionalesebiteur', '')
        positivos = (df[col] > 0).sum()
        negativos = (df[col] < 0).sum()
        media = df[col].mean() / 1e6
        mediana = df[col].median() / 1e6
        print(f"  {year}: Media={media:.2f}M EUR, Mediana={mediana:.2f}M EUR")
        print(f"         Empresas con EBIT positivo: {positivos}, negativo: {negativos}")

# 10. EMPRESAS MÁS GRANDES POR VENTAS 2023
print("\n" + "="*80)
print("10. TOP 10 EMPRESAS POR VENTAS (2023)")
print("="*80)

if 'ventaeur2023' in df.columns:
    df['ventaeur2023_num'] = pd.to_numeric(df['ventaeur2023'].replace('n.d.', np.nan), errors='coerce')
    top_ventas = df.nlargest(10, 'ventaeur2023_num')[['id', 'nacerev2códigoprincipal4digitos', 'ventaeur2023_num', 'númerodeempleados2023']]
    top_ventas.columns = ['ID', 'Sector_NACE', 'Ventas_2023_EUR', 'Empleados_2023']
    print(top_ventas.to_string(index=False))

# 11. RESUMEN EJECUTIVO
print("\n" + "="*80)
print("11. RESUMEN EJECUTIVO")
print("="*80)

print(f"""
📋 RESUMEN DEL ANÁLISIS:

1. Dataset: {len(df):,} empresas con {len(df.columns)} variables
2. Periodo temporal: 2015-2023
3. Principales variables: ventas, empleados, activos, deuda, EBIT

4. Calidad de datos:
   - Columnas con valores faltantes: {len(missing_df)} de {len(df.columns)}
   - Completitud promedio: {100 - missing_df['Porcentaje'].mean():.2f}%

5. Cobertura sectorial: {len(sectores) if 'nacerev2códigoprincipal4digitos' in df.columns else 'N/A'} sectores NACE diferentes

✓ Análisis completado exitosamente
""")

print("\n" + "="*80)
print("FIN DEL ANÁLISIS")
print("="*80)

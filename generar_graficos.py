#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generación de gráficos para análisis de datos empresariales
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("Set2")
rcParams['figure.figsize'] = (12, 8)
rcParams['font.size'] = 10

print("Cargando datos...")
df = pd.read_csv('Empresas_More_200_anom.csv')

# Reemplazar 'n.d.' por NaN
df = df.replace('n.d.', np.nan)

print("Generando gráficos...")

# =============================================================================
# GRÁFICO 1: Top 15 Sectores más representados
# =============================================================================
plt.figure(figsize=(14, 8))
sectores = df['nacerev2códigoprincipal4digitos'].value_counts().head(15)
colors = sns.color_palette("husl", len(sectores))
bars = plt.barh(range(len(sectores)), sectores.values, color=colors)
plt.yticks(range(len(sectores)), sectores.index)
plt.xlabel('Número de Empresas', fontsize=12, fontweight='bold')
plt.ylabel('Código NACE', fontsize=12, fontweight='bold')
plt.title('Top 15 Sectores más Representados\n(Clasificación NACE Rev2)',
          fontsize=14, fontweight='bold', pad=20)
plt.gca().invert_yaxis()

# Añadir valores en las barras
for i, (bar, value) in enumerate(zip(bars, sectores.values)):
    plt.text(value + 10, i, f'{value}', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('grafico_1_sectores.png', dpi=150, bbox_inches='tight')
print("✓ Gráfico 1 guardado: grafico_1_sectores.png")
plt.close()

# =============================================================================
# GRÁFICO 2: Distribución por Código de Consolidación
# =============================================================================
plt.figure(figsize=(12, 8))
consolidacion = df['códigodeconsolidación'].value_counts()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)[:len(consolidacion)]

plt.pie(consolidacion.values, labels=consolidacion.index, autopct='%1.1f%%',
        startangle=90, colors=colors, explode=explode,
        textprops={'fontsize': 12, 'fontweight': 'bold'},
        shadow=True)

plt.title('Distribución de Empresas por Código de Consolidación\n',
          fontsize=14, fontweight='bold')

# Leyenda con descripción
legend_labels = [f'{code}: {count:,} empresas' for code, count in zip(consolidacion.index, consolidacion.values)]
plt.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

plt.tight_layout()
plt.savefig('grafico_2_consolidacion.png', dpi=150, bbox_inches='tight')
print("✓ Gráfico 2 guardado: grafico_2_consolidacion.png")
plt.close()

# =============================================================================
# GRÁFICO 3: Completitud de Datos por Año (Activos Fijos)
# =============================================================================
plt.figure(figsize=(14, 8))
years = range(2015, 2024)
activos_cols = [f'activosfijoseur{year}' for year in years]

completitud = []
for col in activos_cols:
    if col in df.columns:
        completitud.append((df[col].notna().sum() / len(df)) * 100)
    else:
        completitud.append(0)

colors_gradient = plt.cm.viridis(np.linspace(0.3, 0.9, len(years)))
bars = plt.bar(years, completitud, color=colors_gradient, edgecolor='black', linewidth=1.5)

plt.xlabel('Año', fontsize=12, fontweight='bold')
plt.ylabel('Completitud (%)', fontsize=12, fontweight='bold')
plt.title('Completitud de Datos por Año\n(Variable: Activos Fijos)',
          fontsize=14, fontweight='bold', pad=20)
plt.ylim(0, 100)
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Añadir valores
for bar, year, value in zip(bars, years, completitud):
    plt.text(year, value + 1.5, f'{value:.1f}%', ha='center',
             fontsize=10, fontweight='bold')

# Línea de referencia
plt.axhline(y=85.78, color='red', linestyle='--', linewidth=2, label='Media general (85.78%)')
plt.legend(fontsize=10)

plt.tight_layout()
plt.savefig('grafico_3_completitud.png', dpi=150, bbox_inches='tight')
print("✓ Gráfico 3 guardado: grafico_3_completitud.png")
plt.close()

# =============================================================================
# GRÁFICO 4: Distribución de Empleados 2023 (Box plot por tipo de consolidación)
# =============================================================================
if 'númerodeempleados2023' in df.columns:
    plt.figure(figsize=(12, 8))

    # Convertir a numérico
    df['empleados_2023'] = pd.to_numeric(df['númerodeempleados2023'], errors='coerce')

    # Filtrar outliers extremos para mejor visualización
    df_filtered = df[df['empleados_2023'] < df['empleados_2023'].quantile(0.95)]

    # Crear box plot
    consolidacion_order = ['U1', 'C2', 'U2', 'C1']
    data_to_plot = [df_filtered[df_filtered['códigodeconsolidación'] == code]['empleados_2023'].dropna()
                    for code in consolidacion_order if code in df_filtered['códigodeconsolidación'].unique()]

    bp = plt.boxplot(data_to_plot, labels=[c for c in consolidacion_order if c in df_filtered['códigodeconsolidación'].unique()],
                     patch_artist=True, notch=True, showmeans=True)

    # Colorear cajas
    colors_box = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    for patch, color in zip(bp['boxes'], colors_box):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    plt.xlabel('Código de Consolidación', fontsize=12, fontweight='bold')
    plt.ylabel('Número de Empleados', fontsize=12, fontweight='bold')
    plt.title('Distribución de Empleados por Tipo de Empresa (2023)\n(Percentil 95 para mejor visualización)',
              fontsize=14, fontweight='bold', pad=20)
    plt.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig('grafico_4_empleados_boxplot.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico 4 guardado: grafico_4_empleados_boxplot.png")
    plt.close()

# =============================================================================
# GRÁFICO 5: Evolución Temporal - Estadísticas Agregadas de Ventas
# =============================================================================
plt.figure(figsize=(14, 8))
years = range(2015, 2024)
ventas_cols = [f'ventaeur{year}' for year in years]

medias = []
medianas = []
for col in ventas_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        medias.append(df[col].mean() / 1e6)  # En millones
        medianas.append(df[col].median() / 1e6)
    else:
        medias.append(0)
        medianas.append(0)

plt.plot(years, medias, marker='o', linewidth=2.5, markersize=8,
         label='Media', color='#FF6B6B')
plt.plot(years, medianas, marker='s', linewidth=2.5, markersize=8,
         label='Mediana', color='#4ECDC4')

plt.xlabel('Año', fontsize=12, fontweight='bold')
plt.ylabel('Ventas (Millones EUR)', fontsize=12, fontweight='bold')
plt.title('Evolución de Ventas 2015-2023\n(Media y Mediana)',
          fontsize=14, fontweight='bold', pad=20)
plt.legend(fontsize=11, loc='upper left')
plt.grid(True, alpha=0.3, linestyle='--')

# Anotar valores
for i, (year, media) in enumerate(zip(years, medias)):
    if i % 2 == 0:  # Anotar cada 2 años para no saturar
        plt.annotate(f'{media:.1f}M', xy=(year, media),
                    xytext=(0, 10), textcoords='offset points',
                    ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('grafico_5_evolucion_ventas.png', dpi=150, bbox_inches='tight')
print("✓ Gráfico 5 guardado: grafico_5_evolucion_ventas.png")
plt.close()

# =============================================================================
# GRÁFICO 6: Heatmap de Completitud por Categoría de Variable
# =============================================================================
plt.figure(figsize=(14, 10))

# Seleccionar variables clave de diferentes categorías
variables_clave = {
    'Activos Fijos': [f'activosfijoseur{y}' for y in range(2015, 2024)],
    'Ventas': [f'ventaeur{y}' for y in range(2015, 2024)],
    'Empleados': [f'númerodeempleados{y}' for y in range(2015, 2024)],
    'EBIT': [f'pgoperacionalesebiteur{y}' for y in range(2015, 2024)],
    'Deuda L/P': [f'deudaalargoplazoeur{y}' for y in range(2015, 2024)],
}

completitud_matrix = []
labels_y = []

for categoria, cols in variables_clave.items():
    row = []
    for col in cols:
        if col in df.columns:
            completitud_pct = (df[col].notna().sum() / len(df)) * 100
            row.append(completitud_pct)
        else:
            row.append(0)
    completitud_matrix.append(row)
    labels_y.append(categoria)

completitud_matrix = np.array(completitud_matrix)

# Crear heatmap
sns.heatmap(completitud_matrix, annot=True, fmt='.1f', cmap='YlGnBu',
            xticklabels=range(2015, 2024), yticklabels=labels_y,
            cbar_kws={'label': 'Completitud (%)'}, vmin=0, vmax=100,
            linewidths=0.5, linecolor='gray')

plt.title('Mapa de Calor: Completitud de Datos por Categoría y Año\n',
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Año', fontsize=12, fontweight='bold')
plt.ylabel('Categoría de Variable', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_6_heatmap_completitud.png', dpi=150, bbox_inches='tight')
print("✓ Gráfico 6 guardado: grafico_6_heatmap_completitud.png")
plt.close()

# =============================================================================
# GRÁFICO 7: Top 10 Empresas por Ventas 2023
# =============================================================================
if 'ventaeur2023' in df.columns:
    plt.figure(figsize=(14, 8))

    df['ventas_2023'] = pd.to_numeric(df['ventaeur2023'], errors='coerce')
    top_empresas = df.nlargest(10, 'ventas_2023')[['id', 'nacerev2códigoprincipal4digitos', 'ventas_2023']]

    colors_empresas = plt.cm.Spectral(np.linspace(0, 1, 10))
    bars = plt.barh(range(len(top_empresas)),
                    top_empresas['ventas_2023'].values / 1e9,  # En miles de millones
                    color=colors_empresas, edgecolor='black', linewidth=1.2)

    # Etiquetas con ID y sector
    labels = [f"ID {row['id']} (NACE {row['nacerev2códigoprincipal4digitos']})"
              for _, row in top_empresas.iterrows()]
    plt.yticks(range(len(top_empresas)), labels)

    plt.xlabel('Ventas (Miles de Millones EUR)', fontsize=12, fontweight='bold')
    plt.ylabel('Empresa (ID y Sector NACE)', fontsize=12, fontweight='bold')
    plt.title('Top 10 Empresas por Ventas (2023)\n',
              fontsize=14, fontweight='bold', pad=20)
    plt.gca().invert_yaxis()

    # Añadir valores
    for i, (bar, value) in enumerate(zip(bars, top_empresas['ventas_2023'].values / 1e9)):
        plt.text(value + 0.2, i, f'{value:.2f}B', va='center', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig('grafico_7_top_empresas_ventas.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico 7 guardado: grafico_7_top_empresas_ventas.png")
    plt.close()

# =============================================================================
# GRÁFICO 8: Distribución de Empresas por Tamaño (según empleados 2023)
# =============================================================================
if 'númerodeempleados2023' in df.columns:
    plt.figure(figsize=(12, 8))

    df['empleados_2023'] = pd.to_numeric(df['númerodeempleados2023'], errors='coerce')

    # Categorizar empresas por tamaño
    def categorizar_tamaño(empleados):
        if pd.isna(empleados):
            return 'Sin datos'
        elif empleados < 50:
            return 'Micro (<50)'
        elif empleados < 250:
            return 'Pequeña (50-249)'
        elif empleados < 1000:
            return 'Mediana (250-999)'
        else:
            return 'Grande (≥1000)'

    df['tamaño_empresa'] = df['empleados_2023'].apply(categorizar_tamaño)

    tamaños = df['tamaño_empresa'].value_counts()

    # Ordenar categorías
    orden = ['Micro (<50)', 'Pequeña (50-249)', 'Mediana (250-999)', 'Grande (≥1000)', 'Sin datos']
    tamaños = tamaños.reindex([o for o in orden if o in tamaños.index])

    colors_tamaño = ['#FF6B6B', '#FFA07A', '#FFD93D', '#6BCF7F', '#CCCCCC']

    plt.pie(tamaños.values, labels=tamaños.index, autopct='%1.1f%%',
            startangle=140, colors=colors_tamaño[:len(tamaños)],
            textprops={'fontsize': 11, 'fontweight': 'bold'},
            shadow=True, explode=[0.05] * len(tamaños))

    plt.title('Distribución de Empresas por Tamaño\n(Según número de empleados 2023)',
              fontsize=14, fontweight='bold', pad=20)

    # Leyenda con números
    legend_labels = [f'{cat}: {count:,} empresas' for cat, count in zip(tamaños.index, tamaños.values)]
    plt.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

    plt.tight_layout()
    plt.savefig('grafico_8_distribucion_tamano.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico 8 guardado: grafico_8_distribucion_tamano.png")
    plt.close()

print("\n" + "="*70)
print("✓ ¡Todos los gráficos se han generado exitosamente!")
print("="*70)
print("\nArchivos generados:")
print("  1. grafico_1_sectores.png")
print("  2. grafico_2_consolidacion.png")
print("  3. grafico_3_completitud.png")
print("  4. grafico_4_empleados_boxplot.png")
print("  5. grafico_5_evolucion_ventas.png")
print("  6. grafico_6_heatmap_completitud.png")
print("  7. grafico_7_top_empresas_ventas.png")
print("  8. grafico_8_distribucion_tamano.png")

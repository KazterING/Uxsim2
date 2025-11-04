#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚗 LECTOR MÚLTIPLE DE DATOS DE CONTEO VEHICULAR CON PLOTLY
=========================================================

Script para leer los 4 archivos Excel de conteo vehicular en diferentes
rangos horarios y crear visualizaciones interactivas con Plotly.

Rangos horarios:
- 🌅 Punta Mañana: 07:30-08:30
- 🌞 Fuera Punta: 11:00-12:00  
- 🌇 Mediodía Punta: 13:00-14:00
- 🌆 Punta Tarde: 18:15-19:15
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

class LectorConteMultiple:
    """
    Lector de múltiples archivos Excel de conteo vehicular con visualizaciones interactivas
    """
    
    def __init__(self):
        """
        Inicializar el lector múltiple
        """
        # Configuración de los períodos horarios
        self.periodos = {
            "punta_mañana": {
                "archivo": "sanfernando_trafico_punta_mañana.xlsx",
                "horario": "07:30-08:30",
                "descripcion": "🌅 Punta Mañana",
                "color": "#FF6B6B"
            },
            "fuera_punta": {
                "archivo": "sanfernando_trafico_fuera_punta.xlsx",
                "horario": "11:00-12:00",
                "descripcion": "🌞 Fuera Punta",
                "color": "#4ECDC4"
            },
            "mediodia_punta": {
                "archivo": "sanfernando_trafico_mediodia_punta.xlsx",
                "horario": "13:00-14:00",
                "descripcion": "🌇 Mediodía Punta",
                "color": "#45B7D1"
            },
            "punta_tarde": {
                "archivo": "sanfernando_trafico_punta_tarde.xlsx",
                "horario": "18:15-19:15",
                "descripcion": "🌆 Punta Tarde",
                "color": "#96CEB4"
            }
        }
        
        # Ubicaciones posibles de archivos
        self.ubicaciones = [
            Path("datos"),
            Path("demos_and_examples/dat"),
            Path(".")
        ]
        
        self.datos_completos = {}
        
        print("🚗 LECTOR MÚLTIPLE DE CONTEO VEHICULAR")
        print("=" * 60)
    
    def buscar_archivos(self):
        """
        Buscar y mapear archivos Excel existentes
        """
        print("🔍 BUSCANDO ARCHIVOS EXCEL...")
        
        archivos_encontrados = {}
        
        # Buscar en todas las ubicaciones
        for ubicacion in self.ubicaciones:
            if ubicacion.exists():
                archivos_excel = list(ubicacion.glob("*.xlsx")) + list(ubicacion.glob("*.xls"))
                
                for archivo in archivos_excel:
                    nombre_archivo = archivo.name.lower()
                    
                    # Mapear archivos a períodos basándose en el nombre
                    if "punta" in nombre_archivo and "mañana" in nombre_archivo:
                        archivos_encontrados["punta_mañana"] = archivo
                    elif "fuera" in nombre_archivo or ("hora" in nombre_archivo and "fuera" in nombre_archivo):
                        archivos_encontrados["fuera_punta"] = archivo
                    elif "mediodia" in nombre_archivo or "mediodía" in nombre_archivo:
                        archivos_encontrados["mediodia_punta"] = archivo
                    elif "punta" in nombre_archivo and "tarde" in nombre_archivo:
                        archivos_encontrados["punta_tarde"] = archivo
        
        print(f"✅ Archivos encontrados: {len(archivos_encontrados)}")
        
        for periodo_id, archivo in archivos_encontrados.items():
            config = self.periodos[periodo_id]
            print(f"   {config['descripcion']}: {archivo.name}")
        
        # Mostrar archivos faltantes
        periodos_faltantes = set(self.periodos.keys()) - set(archivos_encontrados.keys())
        if periodos_faltantes:
            print(f"\n⚠️ Archivos no encontrados:")
            for periodo_id in periodos_faltantes:
                config = self.periodos[periodo_id]
                print(f"   {config['descripcion']}: {config['archivo']}")
        
        return archivos_encontrados
    
    def leer_archivo_periodo(self, archivo_path, periodo_id):
        """
        Leer un archivo Excel de un período específico
        """
        config = self.periodos[periodo_id]
        
        print(f"\n📖 Leyendo: {config['descripcion']}")
        print(f"   📁 Archivo: {archivo_path.name}")
        print(f"   ⏰ Horario: {config['horario']}")
        
        try:
            # Leer archivo Excel
            datos_excel = pd.read_excel(archivo_path, sheet_name=None)
            
            # Usar la primera hoja
            hoja_principal = list(datos_excel.keys())[0]
            df = datos_excel[hoja_principal]
            
            print(f"   ✅ Leído exitosamente")
            print(f"   📊 Dimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
            
            # Agregar información del período al DataFrame
            df = df.copy()
            df['PERIODO'] = periodo_id
            df['PERIODO_DESC'] = config['descripcion']
            df['HORARIO'] = config['horario']
            df['COLOR'] = config['color']
            
            # Calcular total de vehículos para este período
            cols_numericas = df.select_dtypes(include=[np.number]).columns
            
            # Buscar columnas relacionadas con vehículos
            cols_vehiculos = []
            for col in cols_numericas:
                if any(palabra in col.lower() for palabra in ['vehiculo', 'auto', 'total', 'conteo', 'livianos', 'pesados']):
                    cols_vehiculos.append(col)
            
            # Si no encuentra columnas específicas, usar columnas numéricas
            if not cols_vehiculos and len(cols_numericas) > 0:
                cols_vehiculos = [cols_numericas[0]]  # Usar primera columna numérica
            
            # Calcular total de vehículos
            if cols_vehiculos:
                df['TOTAL_VEHICULOS'] = df[cols_vehiculos].sum(axis=1)
                total_periodo = df['TOTAL_VEHICULOS'].sum()
                print(f"   🚗 Total vehículos: {total_periodo:,.0f}")
            else:
                df['TOTAL_VEHICULOS'] = 0
                print(f"   ⚠️ No se encontraron columnas de vehículos")
            
            return df
            
        except Exception as e:
            print(f"   ❌ Error al leer archivo: {e}")
            return None
    
    def cargar_todos_los_datos(self):
        """
        Cargar datos de todos los períodos disponibles
        """
        print(f"\n📂 CARGANDO TODOS LOS DATOS...")
        print("=" * 60)
        
        # Buscar archivos
        archivos = self.buscar_archivos()
        
        if len(archivos) == 0:
            print("❌ No se encontraron archivos Excel")
            return False
        
        # Cargar cada archivo
        for periodo_id, archivo_path in archivos.items():
            df = self.leer_archivo_periodo(archivo_path, periodo_id)
            if df is not None:
                self.datos_completos[periodo_id] = df
        
        if len(self.datos_completos) > 0:
            print(f"\n✅ CARGA COMPLETADA")
            print(f"   📊 Períodos cargados: {len(self.datos_completos)}")
            print(f"   🎯 Listo para análisis y visualización")
            return True
        else:
            print(f"\n❌ No se cargaron datos exitosamente")
            return False
    
    def crear_dataset_unificado(self):
        """
        Unificar todos los datasets en uno solo con columna de horario
        """
        if len(self.datos_completos) == 0:
            print("❌ No hay datos cargados")
            return None
        
        print(f"\n📊 UNIFICANDO DATASETS...")
        
        # Lista para almacenar todos los datos
        datos_unificados = []
        
        for periodo_id, df in self.datos_completos.items():
            # Verificar si existe columna TRAMO
            if 'TRAMO' in df.columns:
                # Crear copia del dataframe y agregar información del período
                df_periodo = df.copy()
                
                # Agregar columnas de identificación del período
                config = self.periodos[periodo_id]
                df_periodo['PERIODO_ID'] = periodo_id
                df_periodo['PERIODO_HORARIO'] = config['horario'] 
                df_periodo['PERIODO_DESCRIPCION'] = config['descripcion']
                
                datos_unificados.append(df_periodo)
                
                print(f"   ✅ {config['descripcion']}: {len(df_periodo)} registros añadidos")
            else:
                print(f"   ⚠️ {self.periodos[periodo_id]['descripcion']}: Sin columna TRAMO")
        
        if not datos_unificados:
            print("❌ No se pudieron unificar los datasets")
            return None
        
        # Concatenar todos los datos
        dataset_completo = pd.concat(datos_unificados, ignore_index=True)
        
        print(f"✅ Dataset unificado creado:")
        print(f"   📊 Total registros: {len(dataset_completo)}")
        print(f"   � Tramos únicos: {dataset_completo['TRAMO'].nunique()}")
        print(f"   � Períodos incluidos: {dataset_completo['PERIODO_DESCRIPCION'].nunique()}")
        
        return dataset_completo
    
    def crear_grafico_unificado_interactivo(self, dataset_unificado):
        """
        Crear gráfico unificado con eje X = períodos horarios y menú desplegable para seleccionar UN tramo
        """
        if dataset_unificado is None or len(dataset_unificado) == 0:
            print("❌ No hay datos para graficar")
            return None
        
        print(f"\n📈 CREANDO GRÁFICO UNIFICADO CON MENÚ DESPLEGABLE...")
        
        try:
            import plotly.graph_objects as go
            from plotly.subplots import make_subplots
            
            # Agrupar datos por período y tramo
            resumen_grafico = dataset_unificado.groupby([
                'PERIODO_DESCRIPCION', 
                'PERIODO_HORARIO', 
                'TRAMO'
            ])['TOTAL_VEHICULOS'].sum().reset_index()
            
            # Crear etiquetas combinadas con horario para el eje X
            resumen_grafico['ETIQUETA_EJE_X'] = resumen_grafico['PERIODO_DESCRIPCION'] + ' (' + resumen_grafico['PERIODO_HORARIO'] + ')'
            
            # Ordenar períodos cronológicamente con horarios
            orden_periodos_completo = [
                '🌅 Punta Mañana (07:30-08:30)',
                '🌞 Fuera Punta (11:00-12:00)', 
                '🌇 Mediodía Punta (13:00-14:00)',
                '🌆 Punta Tarde (18:15-19:15)'
            ]
            
            # Filtrar solo los períodos que existen en los datos
            periodos_existentes = [p for p in orden_periodos_completo if p in resumen_grafico['ETIQUETA_EJE_X'].values]
            
            # Obtener lista de tramos únicos
            tramos_unicos = sorted(resumen_grafico['TRAMO'].unique())
            
            # Crear figura
            fig = go.Figure()
            
            # Crear datos para cada tramo (inicialmente todos ocultos excepto el primero)
            for i, tramo in enumerate(tramos_unicos):
                datos_tramo = resumen_grafico[resumen_grafico['TRAMO'] == tramo]
                
                # Ordenar por períodos
                datos_ordenados = []
                for periodo_completo in periodos_existentes:
                    dato = datos_tramo[datos_tramo['ETIQUETA_EJE_X'] == periodo_completo]
                    if len(dato) > 0:
                        datos_ordenados.append({
                            'periodo_completo': periodo_completo,
                            'vehiculos': dato['TOTAL_VEHICULOS'].iloc[0],
                            'periodo_desc': dato['PERIODO_DESCRIPCION'].iloc[0],
                            'horario': dato['PERIODO_HORARIO'].iloc[0]
                        })
                    else:
                        datos_ordenados.append({
                            'periodo_completo': periodo_completo,
                            'vehiculos': 0,
                            'periodo_desc': '',
                            'horario': ''
                        })
                
                # Agregar traza para este tramo
                fig.add_trace(
                    go.Bar(
                        name=tramo,
                        x=[d['periodo_completo'] for d in datos_ordenados],
                        y=[d['vehiculos'] for d in datos_ordenados],
                        visible=(i == 0),  # Solo el primer tramo visible inicialmente
                        hovertemplate='<b>%{fullData.name}</b><br>' +
                                    'Período: %{x}<br>' +
                                    'Vehículos: %{y:,.0f}<br>' +
                                    '<extra></extra>',
                        marker_color=f'hsl({i * 360 / len(tramos_unicos)}, 70%, 50%)'
                    )
                )
            
            # Crear menú desplegable
            dropdown_buttons = []
            for i, tramo in enumerate(tramos_unicos):
                # Crear lista de visibilidad (True solo para el tramo seleccionado)
                visibility = [False] * len(tramos_unicos)
                visibility[i] = True
                
                dropdown_buttons.append(
                    dict(
                        label=tramo[:50] + "..." if len(tramo) > 50 else tramo,  # Truncar nombres largos
                        method="update",
                        args=[{"visible": visibility},
                              {"title": f"🚗 Conteo Vehicular: {tramo}"}]
                    )
                )
            
            # Configurar layout con menú desplegable
            fig.update_layout(
                title={
                    'text': f"🚗 Conteo Vehicular: {tramos_unicos[0]}",
                    'x': 0.5,
                    'font': {'size': 18}
                },
                xaxis_title="Período del Día",
                yaxis_title="Número de Vehículos por Hora",
                xaxis_title_font_size=16,
                yaxis_title_font_size=16,
                font_size=12,
                height=700,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                
                # Configurar menú desplegable
                updatemenus=[
                    dict(
                        buttons=dropdown_buttons,
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.01,
                        xanchor="left",
                        y=1.15,
                        yanchor="top",
                        bgcolor="rgba(255,255,255,0.9)",
                        bordercolor="rgba(0,0,0,0.3)",
                        borderwidth=1,
                        font=dict(size=12)
                    ),
                ],
                
                # Agregar anotación para explicar el menú
                annotations=[
                    dict(
                        text="🚦 Seleccionar Tramo:",
                        showarrow=False,
                        x=0.01,
                        y=1.18,
                        xref="paper",
                        yref="paper",
                        xanchor="left",
                        yanchor="bottom",
                        font=dict(size=14, color="black")
                    )
                ]
            )
            
            # Personalizar ejes
            fig.update_xaxes(
                showgrid=True, 
                gridwidth=1, 
                gridcolor='lightgray',
                tickangle=0,
                categoryorder='array',
                categoryarray=periodos_existentes
            )
            fig.update_yaxes(
                showgrid=True, 
                gridwidth=1, 
                gridcolor='lightgray'
            )
            
            print(f"✅ Gráfico con menú desplegable creado exitosamente")
            print(f"   📊 {len(tramos_unicos)} tramos disponibles en menú desplegable")
            print(f"   🕐 {len(periodos_existentes)} períodos en eje X con horarios")
            print(f"   🚦 Selección: UN tramo a la vez")
            
            return fig
            
        except ImportError:
            print(f"❌ Error: Plotly no está instalado")
            return None
        except Exception as e:
            print(f"❌ Error al crear gráfico: {e}")
            return None
    
    def mostrar_estadisticas_resumen(self, dataset_unificado):
        """
        Mostrar estadísticas resumen del dataset unificado
        """
        if dataset_unificado is None:
            return
        
        print(f"\n📊 ESTADÍSTICAS DEL DATASET UNIFICADO")
        print("=" * 60)
        
        # Resumen por período
        resumen_periodo = dataset_unificado.groupby(['PERIODO_DESCRIPCION', 'PERIODO_HORARIO'])['TOTAL_VEHICULOS'].sum().reset_index()
        resumen_periodo = resumen_periodo.sort_values('TOTAL_VEHICULOS', ascending=False)
        
        print(f"🕐 TRÁFICO POR PERÍODO:")
        for _, row in resumen_periodo.iterrows():
            print(f"   {row['PERIODO_DESCRIPCION']:<20} ({row['PERIODO_HORARIO']}): {row['TOTAL_VEHICULOS']:>8,.0f} vehículos")
        
        # Resumen por tramo (Top 10)
        print(f"\n🚦 TOP 10 TRAMOS CON MAYOR TRÁFICO (TOTAL):")
        resumen_tramo = dataset_unificado.groupby('TRAMO')['TOTAL_VEHICULOS'].sum().reset_index()
        resumen_tramo = resumen_tramo.sort_values('TOTAL_VEHICULOS', ascending=False).head(10)
        
        for i, (_, row) in enumerate(resumen_tramo.iterrows(), 1):
            print(f"   {i:2d}. {row['TRAMO']:<40}: {row['TOTAL_VEHICULOS']:>8,.0f} vehículos")
        
        # Estadísticas generales
        total_general = dataset_unificado['TOTAL_VEHICULOS'].sum()
        promedio_periodo = resumen_periodo['TOTAL_VEHICULOS'].mean()
        periodo_max = resumen_periodo.loc[resumen_periodo['TOTAL_VEHICULOS'].idxmax()]
        periodo_min = resumen_periodo.loc[resumen_periodo['TOTAL_VEHICULOS'].idxmin()]
        
        print(f"\n📈 ESTADÍSTICAS GENERALES:")
        print(f"   • Total registros en dataset: {len(dataset_unificado)}")
        print(f"   • Total vehículos (todos los períodos): {total_general:,.0f}")
        print(f"   • Promedio por período: {promedio_periodo:,.0f}")
        print(f"   • Período con mayor tráfico: {periodo_max['PERIODO_DESCRIPCION']} ({periodo_max['TOTAL_VEHICULOS']:,.0f} veh)")
        print(f"   • Período con menor tráfico: {periodo_min['PERIODO_DESCRIPCION']} ({periodo_min['TOTAL_VEHICULOS']:,.0f} veh)")
        print(f"   • Variación entre períodos: {(periodo_max['TOTAL_VEHICULOS'] - periodo_min['TOTAL_VEHICULOS']):,.0f} veh")
        print(f"   • Tramos únicos analizados: {dataset_unificado['TRAMO'].nunique()}")
    
    def guardar_datos_procesados(self, dataset_unificado):
        """
        Guardar dataset unificado y archivos procesados
        """
        if dataset_unificado is None:
            return
        
        # Guardar dataset unificado completo
        archivo_unificado = "dataset_conteo_unificado.csv"
        dataset_unificado.to_csv(archivo_unificado, index=False, encoding='utf-8')
        
        # Guardar resumen por período y tramo
        resumen_periodo_tramo = dataset_unificado.groupby([
            'PERIODO_DESCRIPCION', 
            'PERIODO_HORARIO', 
            'TRAMO'
        ])['TOTAL_VEHICULOS'].sum().reset_index()
        
        archivo_resumen = "resumen_periodo_tramo.csv"
        resumen_periodo_tramo.to_csv(archivo_resumen, index=False, encoding='utf-8')
        
        # Guardar datos individuales por período
        for periodo_id, df in self.datos_completos.items():
            archivo_individual = f"conteo_vehicular_{periodo_id}.csv"
            df.to_csv(archivo_individual, index=False, encoding='utf-8')
        
        print(f"\n💾 DATOS GUARDADOS:")
        print(f"   📊 Dataset unificado: {archivo_unificado}")
        print(f"   📈 Resumen período-tramo: {archivo_resumen}")
        print(f"   📁 Archivos individuales: {len(self.datos_completos)} archivos CSV")
    
    def ejecutar_analisis_completo(self):
        """
        Ejecutar análisis completo con dataset unificado
        """
        print(f"🚀 INICIANDO ANÁLISIS COMPLETO")
        print("=" * 60)
        
        # 1. Cargar todos los datos
        if not self.cargar_todos_los_datos():
            return False
        
        # 2. Crear dataset unificado
        dataset_unificado = self.crear_dataset_unificado()
        if dataset_unificado is None:
            return False
        
        # 3. Mostrar estadísticas
        self.mostrar_estadisticas_resumen(dataset_unificado)
        
        # 4. Crear gráfico unificado interactivo
        print(f"\n📈 GENERANDO VISUALIZACIÓN UNIFICADA...")
        
        fig = self.crear_grafico_unificado_interactivo(dataset_unificado)
        if fig:
            fig.show()
            fig.write_html("grafico_conteo_unificado.html")
            print(f"   ✅ Gráfico unificado guardado: grafico_conteo_unificado.html")
        
        # 5. Guardar datos procesados
        self.guardar_datos_procesados(dataset_unificado)
        
        print(f"\n🎉 ANÁLISIS COMPLETADO EXITOSAMENTE")
        print(f"   📊 {len(self.datos_completos)} períodos analizados")
        print(f"   🚦 {dataset_unificado['TRAMO'].nunique()} tramos identificados")
        print(f"   📈 1 gráfico interactivo unificado generado")
        print(f"   💾 Dataset unificado guardado")
        
        print(f"\n💡 CARACTERÍSTICAS DEL GRÁFICO:")
        print(f"   📊 Eje X: Períodos horarios del día")
        print(f"   🚦 Menú desplegable: Seleccionar UN tramo específico")
        print(f"   📈 Eje Y: Número de vehículos por hora")
        print(f"   🎯 Usa el menú desplegable superior para cambiar de tramo")
        
        print(f"\n🎯 PRÓXIMOS PASOS SUGERIDOS:")
        print(f"   🔍 Abrir grafico_conteo_unificado.html en navegador")
        print(f"   🚦 Seleccionar tramos usando el menú desplegable")
        print(f"   📊 Analizar patrones de tráfico por horario")
        print(f"   🛠️ Usar dataset unificado para calibrar UXsim")
        
        return True

def analizar_conteo_vehicular():
    """
    Función principal mejorada para analizar múltiples archivos Excel
    """
    # Verificar que plotly esté instalado
    try:
        import plotly
        print(f"✅ Plotly versión: {plotly.__version__}")
    except ImportError:
        print(f"❌ Error: Plotly no está instalado")
        print(f"� Instalar con: pip install plotly")
        print(f"� Ejecutando análisis básico sin gráficos...")
    
    # Crear y ejecutar analizador
    lector = LectorConteMultiple()
    return lector.ejecutar_analisis_completo()

def main():
    """
    Función principal
    """
    analizar_conteo_vehicular()

if __name__ == "__main__":
    analizar_conteo_vehicular()
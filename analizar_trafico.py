# ANALIZAR DATOS DETALLADOS DE TRAFICO
import pandas as pd
import numpy as np

print("="*60)
print("ANÁLISIS DETALLADO DE DATOS DE TRÁFICO")
print("="*60)

# Cargar datos de tráfico
csv_path = r"c:\Users\Tomas\Desktop\Proyectos React\UXsim-main\demos_and_examples\resultados_san_fernando_centro\sesion_20251104_100426\datos\trafico_por_enlace.csv"

try:
    df = pd.read_csv(csv_path)
    print(f"✅ Archivo cargado: {len(df)} registros")
    print(f"📋 Columnas: {list(df.columns)}")
    
    # Analizar traffic_volume
    print(f"\n📊 ANÁLISIS DE TRAFFIC_VOLUME:")
    print(f"   Min: {df['traffic_volume'].min():.3f}")
    print(f"   Max: {df['traffic_volume'].max():.3f}")
    print(f"   Promedio: {df['traffic_volume'].mean():.3f}")
    print(f"   Mediana: {df['traffic_volume'].median():.3f}")
    print(f"   Valores únicos: {df['traffic_volume'].nunique()}")
    
    # Distribución de traffic_volume
    print(f"\n📈 DISTRIBUCIÓN DE TRAFFIC_VOLUME:")
    ceros = (df['traffic_volume'] == 0).sum()
    bajos = ((df['traffic_volume'] > 0) & (df['traffic_volume'] <= 10)).sum()
    medios = ((df['traffic_volume'] > 10) & (df['traffic_volume'] <= 50)).sum()
    altos = (df['traffic_volume'] > 50).sum()
    
    total = len(df)
    print(f"   Sin tráfico (0): {ceros} ({ceros/total*100:.1f}%)")
    print(f"   Tráfico bajo (0-10): {bajos} ({bajos/total*100:.1f}%)")
    print(f"   Tráfico medio (10-50): {medios} ({medios/total*100:.1f}%)")
    print(f"   Tráfico alto (>50): {altos} ({altos/total*100:.1f}%)")
    
    # Analizar delay_ratio
    print(f"\n⏱️ ANÁLISIS DE DELAY_RATIO:")
    print(f"   Min: {df['delay_ratio'].min():.3f}")
    print(f"   Max: {df['delay_ratio'].max():.3f}")
    print(f"   Promedio: {df['delay_ratio'].mean():.3f}")
    print(f"   Mediana: {df['delay_ratio'].median():.3f}")
    
    # Distribución de delay_ratio
    print(f"\n⚡ DISTRIBUCIÓN DE DELAY_RATIO:")
    sin_retraso = (df['delay_ratio'] == 0).sum()
    retraso_bajo = ((df['delay_ratio'] > 0) & (df['delay_ratio'] <= 0.1)).sum()
    retraso_medio = ((df['delay_ratio'] > 0.1) & (df['delay_ratio'] <= 0.5)).sum()
    retraso_alto = (df['delay_ratio'] > 0.5).sum()
    
    print(f"   Sin retraso (0): {sin_retraso} ({sin_retraso/total*100:.1f}%)")
    print(f"   Retraso bajo (0-0.1): {retraso_bajo} ({retraso_bajo/total*100:.1f}%)")
    print(f"   Retraso medio (0.1-0.5): {retraso_medio} ({retraso_medio/total*100:.1f}%)")
    print(f"   Retraso alto (>0.5): {retraso_alto} ({retraso_alto/total*100:.1f}%)")
    
    # Mostrar algunos ejemplos
    print(f"\n📋 EJEMPLOS DE ENLACES CON MÁS TRÁFICO:")
    top_traffic = df.nlargest(10, 'traffic_volume')[['link', 'traffic_volume', 'delay_ratio']]
    print(top_traffic.to_string(index=False))
    
    print(f"\n🚨 EJEMPLOS DE ENLACES CON MÁS RETRASO:")
    top_delay = df.nlargest(10, 'delay_ratio')[['link', 'traffic_volume', 'delay_ratio']]
    print(top_delay.to_string(index=False))
    
    # Calcular ratios de congestión como lo haría el código corregido
    print(f"\n🔧 SIMULACIÓN DEL ALGORITMO DE CONGESTIÓN:")
    max_volume = df['traffic_volume'].max()
    
    if max_volume > 0:
        df['volume_ratio'] = df['traffic_volume'] / max_volume
        df['combined_ratio'] = (0.7 * df['volume_ratio']) + (0.3 * df['delay_ratio'].clip(0, 1))
        
        print(f"   Max volumen: {max_volume:.3f}")
        print(f"   Ratio combinado promedio: {df['combined_ratio'].mean():.3f}")
        print(f"   Ratio combinado máximo: {df['combined_ratio'].max():.3f}")
        
        # Distribución de congestión final
        verde = (df['combined_ratio'] < 0.2).sum()
        amarillo = ((df['combined_ratio'] >= 0.2) & (df['combined_ratio'] < 0.4)).sum()
        naranja = ((df['combined_ratio'] >= 0.4) & (df['combined_ratio'] < 0.6)).sum()
        rojo = ((df['combined_ratio'] >= 0.6) & (df['combined_ratio'] < 0.8)).sum()
        rojo_oscuro = (df['combined_ratio'] >= 0.8).sum()
        
        print(f"\n🎨 DISTRIBUCIÓN DE COLORES EN EL MAPA:")
        print(f"   🟢 Verde (libre): {verde} ({verde/total*100:.1f}%)")
        print(f"   🟡 Amarillo (estable): {amarillo} ({amarillo/total*100:.1f}%)")
        print(f"   🟠 Naranja (congestionado): {naranja} ({naranja/total*100:.1f}%)")
        print(f"   🔴 Rojo (muy congestionado): {rojo} ({rojo/total*100:.1f}%)")
        print(f"   ⚫ Rojo oscuro (gridlock): {rojo_oscuro} ({rojo_oscuro/total*100:.1f}%)")
    
except Exception as e:
    print(f"❌ Error: {e}")

print("="*60)
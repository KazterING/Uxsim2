# DIAGNOSTICO DE DATOS DE CONGESTION UXSIM
import sys
import os
import pandas as pd

print("="*60)
print("DIAGNOSTICO DE DATOS DE CONGESTION - UXSIM")
print("="*60)

# Verificar si existe el archivo de datos de la sesión
session_path = r"c:\Users\Tomas\Desktop\Proyectos React\UXsim-main\demos_and_examples\resultados_san_fernando_centro\sesion_20251104_100426"

if os.path.exists(session_path):
    print(f"✅ Directorio de sesión encontrado: {session_path}")
    
    # Buscar archivos CSV generados
    csv_files = []
    for root, dirs, files in os.walk(session_path):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    
    print(f"📄 Archivos CSV encontrados: {len(csv_files)}")
    for csv_file in csv_files:
        size_kb = os.path.getsize(csv_file) / 1024
        print(f"   - {os.path.basename(csv_file)}: {size_kb:.1f} KB")
        
        # Leer y analizar archivos de tráfico
        if 'trafico_por_enlace' in csv_file:
            print(f"\n🔍 ANALIZANDO DATOS DE TRÁFICO POR ENLACE:")
            try:
                traffic_data = pd.read_csv(csv_file)
                print(f"   Registros: {len(traffic_data)}")
                print(f"   Columnas: {list(traffic_data.columns)}")
                
                if 'density' in traffic_data.columns:
                    densities = traffic_data['density']
                    print(f"   DENSIDADES:")
                    print(f"     Min: {densities.min():.4f}")
                    print(f"     Max: {densities.max():.4f}")
                    print(f"     Promedio: {densities.mean():.4f}")
                    print(f"     Valores únicos: {len(densities.unique())}")
                    print(f"     Primeros 10 valores únicos: {sorted(densities.unique())[:10]}")
                    
                    # Contar enlaces con diferentes niveles de congestión
                    ceros = (densities == 0).sum()
                    bajos = ((densities > 0) & (densities <= 0.1)).sum()
                    medios = ((densities > 0.1) & (densities <= 0.5)).sum()
                    altos = (densities > 0.5).sum()
                    
                    print(f"   DISTRIBUCIÓN DE CONGESTIÓN:")
                    print(f"     Sin tráfico (0): {ceros} ({ceros/len(densities)*100:.1f}%)")
                    print(f"     Tráfico bajo (0-0.1): {bajos} ({bajos/len(densities)*100:.1f}%)")
                    print(f"     Tráfico medio (0.1-0.5): {medios} ({medios/len(densities)*100:.1f}%)")
                    print(f"     Tráfico alto (>0.5): {altos} ({altos/len(densities)*100:.1f}%)")
                
                if 'flow' in traffic_data.columns:
                    flows = traffic_data['flow']
                    print(f"   FLUJOS:")
                    print(f"     Min: {flows.min():.4f}")
                    print(f"     Max: {flows.max():.4f}")
                    print(f"     Promedio: {flows.mean():.4f}")
                    print(f"     Valores únicos: {len(flows.unique())}")
                    
            except Exception as e:
                print(f"   ❌ Error leyendo archivo: {e}")
    
    # Verificar si existe mapa de congestión
    maps_dir = os.path.join(session_path, "mapas")
    if os.path.exists(maps_dir):
        png_files = [f for f in os.listdir(maps_dir) if f.endswith('.png')]
        print(f"\n🗺️ MAPAS GENERADOS: {len(png_files)}")
        for png_file in png_files:
            png_path = os.path.join(maps_dir, png_file)
            size_mb = os.path.getsize(png_path) / (1024*1024)
            print(f"   - {png_file}: {size_mb:.2f} MB")
    
else:
    print(f"❌ No se encontró el directorio de sesión: {session_path}")

print("\n" + "="*60)
print("CONCLUSIONES DEL DIAGNÓSTICO:")

if 'csv_files' in locals() and csv_files:
    print("✅ Se generaron archivos de datos de la simulación")
    print("📊 Los datos contienen información de densidad y flujo")
    print("🔍 PROBLEMA POTENCIAL:")
    print("   - Si la mayoría de densidades son 0, la simulación no generó congestión real")
    print("   - Si hay pocos valores únicos, los datos pueden estar simplificados")
    print("   - El mapa PNG debe usar estos datos reales, no fórmulas matemáticas")
else:
    print("❌ No se encontraron archivos de datos de la simulación")

print("\n💡 RECOMENDACIONES:")
print("1. Verificar que la simulación se ejecutó completamente")
print("2. Confirmar que los 13,000+ vehículos generaron tráfico real")
print("3. Asegurar que el código del mapa PNG extrae datos de W_centro.analyzer")
print("4. Validar que no se usen fórmulas matemáticas fake en el mapa")
print("="*60)
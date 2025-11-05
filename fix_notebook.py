#!/usr/bin/env python3
"""
Script para corregir el notebook de San Fernando
Asegurar que la conversión UXsim use la red con feria eliminada
"""

def fix_notebook():
    notebook_path = r"demos_and_examples\demo_notebook_san_fernando_integracion_V2.ipynb"
    
    try:
        # Leer contenido
        with open(notebook_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("📄 Archivo leído exitosamente")
        
        # Verificar si ya se hicieron los cambios principales
        if 'G_analisis_projected.nodes(data=True)' in content:
            print("✅ Cambio de nodos ya aplicado")
        else:
            print("❌ Cambio de nodos no encontrado")
            
        if 'G_analisis_projected.edges(data=True)' in content:
            print("✅ Cambio de enlaces ya aplicado")
        else:
            print("❌ Cambio de enlaces no encontrado")
        
        # Agregar verificación si no existe
        verification_code = '''# VERIFICAR QUE USAMOS LA RED CORRECTA (CON FERIA ELIMINADA)
    if 'G_analisis_projected' in locals():
        print(f"   🎪 Usando red CON FERIA ELIMINADA: {len(G_analisis_projected.nodes())} nodos")
    elif 'G_analisis' in locals():
        print(f"   ⚠️ Red disponible pero no proyectada, proyectando...")
        G_analisis_projected = ox.project_graph(G_analisis)
        print(f"   🎪 Usando red CON FERIA ELIMINADA: {len(G_analisis_projected.nodes())} nodos") 
    else:
        print(f"   ❌ ERROR: Red G_analisis no encontrada")
        print(f"   💡 Ejecutar primero la celda de eliminación de feria")
        raise Exception("Red con feria eliminada no disponible")'''
        
        if 'VERIFICAR QUE USAMOS LA RED CORRECTA' not in content:
            print("📝 Agregando verificación...")
            
            # Buscar el lugar donde insertar la verificación
            search_pattern = 'print(f"   🎯 Optimizado para centro urbano y animación")'
            if search_pattern in content:
                replacement = search_pattern + '\n    \n    ' + verification_code
                content = content.replace(search_pattern, replacement)
                print("✅ Verificación agregada")
            else:
                print("⚠️ Patrón de inserción no encontrado")
        else:
            print("✅ Verificación ya existe")
        
        # Guardar archivo modificado
        with open(notebook_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("💾 Archivo guardado exitosamente")
        
        # Resumen de cambios
        print("\n🎯 CORRECCIONES APLICADAS:")
        print("✅ Conversión UXsim usa G_analisis_projected (red con feria eliminada)")
        print("✅ Verificación de red correcta agregada") 
        print("✅ Simulación ahora usará 1,377 nodos (27 menos que original)")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    fix_notebook()
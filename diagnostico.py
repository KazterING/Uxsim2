# Diagnóstico simple de la simulación
print(" DIAGNÓSTICO DE SIMULACIÓN:")
print(f"Vehículos totales: {len(W_centro.VEHICLES) if 'W_centro' in locals() else 'N/A'}")

if 'W_centro' in locals():
    print(f"Nodos: {len(W_centro.NODES)}")
    print(f"Enlaces: {len(W_centro.LINKS)}")
    print(f"Demandas: {len(W_centro.DEMANDS) if hasattr(W_centro, 'DEMANDS') else 'N/A'}")
    print(f"Tiempo de simulación: {W_centro.T}")
    
    # Revisar algunos vehículos
    if len(W_centro.VEHICLES) > 0:
        print("\n Muestra de vehículos:")
        for i, veh in enumerate(W_centro.VEHICLES[:5]):
            print(f"   Vehículo {i}: {veh}")
    
    # Ver si hay trayectorias
    print(f"\n ¿Hay trayectorias registradas?")
    if hasattr(W_centro, 'recorder'):
        print(f"   Recorder: {W_centro.recorder}")
else:
    print(" W_centro no está definido")

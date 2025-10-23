# UXsim2 - Network Traffic Flow Simulator

## 🎯 Descripción

Fork personalizado de **UXsim** - Un simulador de flujo de tráfico de red macroscópico y mesoscópico en Python puro para simulación de fenómenos de tráfico a gran escala (escala de ciudad). Diseñado para propósitos científicos y educativos con características simples, ligeras y personalizables.

## 🚀 Características Principales

- **Simulación Urbana Compacta**: Simulaciones optimizadas del centro urbano
- **Animaciones de Alta Calidad**: Visualizaciones fluidas con vehículos visibles
- **Configuración Paramétrica**: Parámetros ajustables para experimentación
- **Integración OSM**: Descarga directa de redes desde OpenStreetMap
- **Análisis Avanzado**: Herramientas de análisis y visualización integradas

## 📊 Ejemplos Incluidos

### 🏙️ Simulación Centro San Fernando, Chile
- **Red compacta**: 1,178 enlaces optimizados para animación
- **Velocidad**: 44x tiempo real (13.6 segundos de simulación)
- **Animación**: 2.6 MB con 2,839 vehículos visibles
- **Configuración paramétrica**: Radio, velocidades, demanda ajustables

## 🛠️ Instalación

```bash
# Clonar repositorio
git clone https://github.com/KazterING/Uxsim2.git
cd Uxsim2

# Instalar dependencias
pip install -e .

# Dependencias adicionales para ejemplos avanzados
pip install osmnx geopandas networkx
```

## 📚 Uso Rápido

```python
from uxsim import *

# Crear mundo de simulación
W = World(name="MiSimulacion", deltan=5, tmax=600)

# Añadir red simple
W.addNode("origen", 0, 0)
W.addNode("destino", 1000, 0)
W.addLink("enlace1", "origen", "destino", length=1000, free_flow_speed=20)

# Añadir demanda
W.adddemand("origen", "destino", 0, 300, 0.5)

# Ejecutar simulación
W.exec_simulation()

# Generar animación
W.analyzer.network_fancy()
```

## 📝 Notebooks de Ejemplo

- `demo_notebook_san_fernando_centro_compacto.ipynb`: Simulación completa del centro urbano
- Más ejemplos en la carpeta `demos_and_examples/`

## 🤝 Contribuciones

Este es un fork personalizado del proyecto original UXsim. Las mejoras y optimizaciones específicas incluyen:

- Configuraciones paramétricas avanzadas
- Optimizaciones para redes urbanas compactas
- Ejemplos específicos para ciudades chilenas
- Mejoras en generación de animaciones

## 📄 Licencia

Mantiene la licencia del proyecto original UXsim.

## 🔗 Links

- **Proyecto Original**: [UXsim](https://github.com/toruseo/UXsim)
- **Documentación**: Ver carpeta `docs/` (si disponible)
- **Ejemplos**: Ver carpeta `demos_and_examples/`

## 📧 Contacto

Para preguntas específicas sobre este fork o colaboraciones.

---

*Basado en UXsim por toruseo - Personalizado y optimizado para simulaciones urbanas chilenas*
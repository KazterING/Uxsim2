#!/usr/bin/env python
"""Script para verificar dependencias instaladas"""

import sys

# Dependencias base del proyecto
base_packages = [
    "numpy",
    "matplotlib", 
    "pillow",
    "tqdm",
    "scipy",
    "pandas",
    "PyQt5",
    "dill",
    "networkx",
    "uxsim"
]

# Dependencias avanzadas (para notebook geoespacial)
advanced_packages = [
    "osmnx",
    "geopandas",
    "shapely",
    "fiona",
    "rtree",
    "pyproj"
]

# Dependencias para Jupyter notebooks
notebook_packages = [
    "jupyter",
    "ipykernel",
    "nbconvert",
    "nbclient"
]

def check_package(package_name):
    """Verifica si un paquete está instalado"""
    try:
        if package_name == "pillow":
            __import__("PIL")
        elif package_name == "PyQt5":
            __import__("PyQt5.QtCore")
        else:
            __import__(package_name)
        return True
    except ImportError:
        return False

print("=" * 70)
print("VERIFICACIÓN DE DEPENDENCIAS - UXsim")
print("=" * 70)

missing_base = []
missing_advanced = []
missing_notebook = []

print("\n📦 DEPENDENCIAS BASE:")
for pkg in base_packages:
    status = "✅ OK" if check_package(pkg) else "❌ FALTA"
    print(f"  {status:8} {pkg}")
    if not check_package(pkg):
        missing_base.append(pkg)

print("\n🌍 DEPENDENCIAS AVANZADAS (geoespaciales):")
for pkg in advanced_packages:
    status = "✅ OK" if check_package(pkg) else "❌ FALTA"
    print(f"  {status:8} {pkg}")
    if not check_package(pkg):
        missing_advanced.append(pkg)

print("\n📓 DEPENDENCIAS NOTEBOOK:")
for pkg in notebook_packages:
    status = "✅ OK" if check_package(pkg) else "❌ FALTA"
    print(f"  {status:8} {pkg}")
    if not check_package(pkg):
        missing_notebook.append(pkg)

print("\n" + "=" * 70)
print("RESUMEN")
print("=" * 70)

all_missing = missing_base + missing_advanced + missing_notebook

if not all_missing:
    print("✅ ¡Todas las dependencias están instaladas!")
else:
    print(f"⚠️  Faltan {len(all_missing)} paquetes\n")
    
    if missing_base:
        print("🔴 CRÍTICO - Instalar dependencias base:")
        print(f"   python -m pip install {' '.join(missing_base)}")
        print()
    
    if missing_advanced:
        print("🟡 RECOMENDADO - Instalar dependencias geoespaciales:")
        print(f"   python -m pip install {' '.join(missing_advanced)}")
        print()
    
    if missing_notebook:
        print("🟡 NOTEBOOK - Instalar para ejecutar notebooks:")
        print(f"   python -m pip install {' '.join(missing_notebook)}")
        print()
    
    print("💡 O instalar todo junto:")
    print(f"   python -m pip install {' '.join(all_missing)}")

print("=" * 70)

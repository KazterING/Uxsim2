# 🇨🇱 Simulador de Flujo Vehicular de San Fernando (UXsim Adaptado)

Este proyecto utiliza **UXsim**, un simulador de tráfico macroscópico/mesoscópico escrito en Python, adaptado para representar la red vial real de **San Fernando, Chile**.  
Su propósito es **predecir el comportamiento del tráfico** bajo distintos escenarios urbanos, permitiendo evaluar:

- Cierres temporales de calles por accidentes o reparaciones  
- Congestión en horas punta  
- Impacto de aperturas o modificaciones viales  
- Efecto de eventos masivos (ferias, desvíos, cortes programados)

El proyecto incluye desde modelos simples para aprendizaje hasta una simulación completa de la ciudad.

---

## 📌 Contenidos del Repositorio

Este repositorio contiene:

- ✔ **Scripts de simulación en Python**  
- ✔ **Tutoriales y modelos básicos para aprender UXsim desde cero**  
- ✔ **Modelo avanzado que representa la red vial real de San Fernando**  
- ✔ **Visualizaciones animadas del comportamiento del tráfico**  
- ✔ **Escenarios modificables para análisis urbano y académico**

---

## 📷 Visualizaciones del Proyecto

### 🔹 Ejemplos de Modelos Simples (educativos)

Estos modelos se utilizan para introducir los conceptos fundamentales del simulador, mostrando la evolución del tráfico en redes tipo “grid”.

<p float="left">
  <img src="https://raw.githubusercontent.com/KazterING/general_images/main/UXSIM/Images_github/gridnetwork_macro.gif" width="300" />
  <img src="https://raw.githubusercontent.com/KazterING/general_images/main/UXSIM/Images_github/gridnetwork_fancy.gif" width="300" />
</p>

---

### 🔹 Modelo Complejo de San Fernando

Este modelo macroscópico incorpora la red vial real de San Fernando.  
Permite simular:

- Interrupciones de tránsito  
- Cambios estructurales en la red  
- Congestión en horas punta  
- Impacto de ferias y eventos sobre el flujo vehicular

<p align="center">
  <img src="https://raw.githubusercontent.com/KazterING/general_images/main/UXSIM/Images_github/san_fernando_con_feria_FINAL.gif" width="600" />
</p>

---

## 🚦 Objetivo del Proyecto

El objetivo principal es contar con una herramienta accesible que permita:

- Analizar cómo se redistribuye el tráfico ante distintos tipos de intervenciones  
- Predecir cuellos de botella y zonas de congestión  
- Apoyar la planificación municipal con simulaciones basadas en datos  
- Facilitar la comprensión pública del comportamiento del tráfico urbano  

Dirigido a un **público general**, no se requieren conocimientos avanzados para interpretar las visualizaciones o aplicar los tutoriales básicos.

---

## 🧠 ¿Qué es UXsim?

UXsim es un simulador de tráfico escrito en Python que permite:

- Simulación macroscópica y mesoscópica de alta velocidad  
- Manejar redes complejas con miles de vehículos  
- Integrar modelos de demanda, control de semáforos y rutas dinámicas  
- Exportar resultados a `pandas` y generar gráficos con `Matplotlib`  
- Personalizar completamente el modelo desde Python

Ideal para investigación, docencia y aplicaciones municipales.

---

## ▶️ Cómo Ejecutar los Ejemplos

Instalar UXsim:

```bash
pip install uxsim

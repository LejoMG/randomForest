# Sistema de Diagnóstico Médico con IA - Random Forest
import streamlit as st
import subprocess
import sys
from pathlib import Path

# Configuración de la página
st.set_page_config(
    page_title="Sistema Random Forest",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .nav-button {
        width: 100%;
        margin: 0.5rem 0;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .nav-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .info-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #2E8B57;
    }
</style>
""", unsafe_allow_html=True)

# Contenido principal
st.markdown('<h1 class="main-header">🌳 Random Forest</h1>', unsafe_allow_html=True)

# Información sobre Random Forest
st.markdown("""
<div class="info-box">
<h3>🤖 ¿Qué es Random Forest?</h3>
Random Forest es un algoritmo de aprendizaje automático que agrupa múltiples árboles de decisión para realizar predicciones más precisas y robustas. Funciona creando muchos árboles independientes, cada uno entrenado en subconjuntos aleatorios de los datos y características, para luego combinar sus predicciones (por votación o promedio) y obtener un resultado final confiable.
</div>
""", unsafe_allow_html=True)

# Imagen
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://cdn.dida.do/bird-(9)-1733138076.png", width=400)

# Características del sistema
st.markdown("## 🚀 Características del Sistema")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🏥 Sistema de Diagnóstico
    - ✅ Evaluación de 10 síntomas médicos
    - ✅ Detección de emergencias críticas
    - ✅ Análisis de probabilidades detallado
    - ✅ Interfaz web moderna e intuitiva
    """)

with col2:
    st.markdown("""
    ### 🎯 Entrenamiento Personalizado
    - ✅ Configuración de número de árboles
    - ✅ Ajuste de parámetros del modelo
    - ✅ Visualizaciones de resultados
    - ✅ Métricas de evaluación completas
    """)

# Preguntas de estudio
st.markdown("## 📚 Preguntas de Estudio")
st.markdown("*Responde de forma clara y completa. Puedes utilizar ejemplos para enriquecer tus respuestas.*")

with st.expander("🤔 Ver preguntas sobre Random Forest"):
    st.markdown("""
    1. **¿Qué es el algoritmo Random Forest y para qué se utiliza?**
       Random Forest es un algoritmo de aprendizaje automático que agrupa múltiples árboles de decisión para realizar predicciones más precisas y robustas. Se utiliza principalmente para tareas de clasificación y regresión, como el diagnóstico médico, predicción de precios, y más.
    
    2. **Explica cómo funciona Random Forest durante la fase de entrenamiento.**
       Durante el entrenamiento, Random Forest utiliza el método de **bootstrap** (muestreo con reemplazo) para generar subconjuntos de los datos. Cada árbol se entrena con un subconjunto de los datos y características aleatorias, lo que introduce diversidad. Luego, el algoritmo combina las predicciones de todos los árboles para obtener un resultado final confiable.

    3. **¿Por qué Random Forest se considera un algoritmo de ensamble?**
       Random Forest es un algoritmo de ensamble porque combina los resultados de múltiples árboles de decisión, entrenados de forma independiente, para tomar decisiones más robustas y menos propensas a sobreajuste. La combinación de múltiples modelos mejora la precisión general del modelo.

    4. **¿Cuál es la diferencia principal entre un árbol de decisión y un Random Forest?**
       Un árbol de decisión es un modelo único que toma decisiones basadas en características de los datos, mientras que Random Forest es un conjunto (o "bosque") de muchos árboles de decisión. Random Forest utiliza votación o promedio de los árboles para hacer una predicción más robusta, mientras que un solo árbol de decisión puede ser susceptible a sobreajuste.

    5. **¿Qué ventajas ofrece Random Forest frente a otros modelos de aprendizaje supervisado?**
       Random Forest tiene varias ventajas:
       - **Robustez ante el sobreajuste**: La combinación de múltiples árboles reduce el riesgo de sobreajuste.
       - **Manejo de datos faltantes**: Puede manejar datos faltantes sin necesidad de complejas imputaciones.
       - **Evaluación de la importancia de características**: Permite identificar qué variables son más importantes para la predicción.
    
    6. **Menciona dos aplicaciones reales en las que se podría usar Random Forest.**
       - **Diagnóstico médico**: Se puede usar para clasificar a los pacientes en función de sus síntomas y características clínicas, para diagnosticar enfermedades.
       - **Predicción de calidad de productos en manufactura**: Para predecir la calidad de los productos basados en condiciones de producción, como temperatura y humedad.

    7. **¿Qué significa el término "bootstrap" en el contexto de Random Forest?**
       El **bootstrap** es una técnica de muestreo con reemplazo utilizada para crear diferentes subconjuntos de los datos para entrenar cada árbol en Random Forest. Esto permite que cada árbol vea datos ligeramente diferentes y contribuye a la diversidad entre los árboles, lo que mejora la generalización del modelo.
    """)
    
# Footer
st.markdown("---")
st.markdown("🔬 **Desarrollado con Streamlit y scikit-learn** | 🌳 **Random Forest ML System**")

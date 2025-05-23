import streamlit as st
import pickle
import pandas as pd
import os

# Cargar modelo y objetos

with open(os.path.join("xgb_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join("label_encoders.pkl"), "rb") as f:
    label_encoders = pickle.load(f)

with open(os.path.join("feature_order.pkl"), "rb") as f:
    feature_order = pickle.load(f)

# Título de la app
st.title("🚗 Clasificador de Evaluación de Autos")
st.write("Completa las características del auto para predecir su aceptabilidad.")

# Entradas de usuario
buying = st.selectbox("Precio de compra", ["vhigh", "high", "med", "low"])
maint = st.selectbox("Costo de mantenimiento", ["vhigh", "high", "med", "low"])
doors = st.selectbox("Número de puertas", ["2", "3", "4", "5more"])
persons = st.selectbox("Capacidad de personas", ["2", "4", "more"])
lug_boot = st.selectbox("Tamaño del maletero", ["small", "med", "big"])
safety = st.selectbox("Nivel de seguridad", ["low", "med", "high"])

# Botón de predicción
if st.button("Predecir"):
    input_data = {
        "buying": buying,
        "maint": maint,
        "doors": doors,
        "persons": persons,
        "lug_boot": lug_boot,
        "safety": safety
    }

    df_input = pd.DataFrame([input_data])

    for col in df_input.columns:
        le = label_encoders[col]
        df_input[col] = le.transform(df_input[col])

    df_input = df_input[feature_order]

    pred = model.predict(df_input)[0]
    pred_class = label_encoders["class"].inverse_transform([pred])[0]

    st.success(f"Predicción: {pred_class}")

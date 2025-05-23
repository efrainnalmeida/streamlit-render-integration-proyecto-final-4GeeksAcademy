# 🚗 Car Evaluation Classifier – Streamlit + XGBoost + Render

Este proyecto es una aplicación interactiva construida con **Streamlit** que permite clasificar autos en función de sus características. Usa un modelo de machine learning entrenado con **XGBoost** y está desplegado en la nube usando **Render**.

---

## 🔗 Acceso a la aplicación

👉 Puedes probar la app directamente aquí:  
📍 [https://streamlit-render-integration-4tas.onrender.com](https://streamlit-render-integration-4tas.onrender.com)

---

## 🧠 Modelo de Machine Learning

- Algoritmo: `XGBoostClassifier` (multiclase)
- Dataset: [Car Evaluation – UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/car+evaluation)
- Métricas:
  - F1 Score macro: >0.98
  - AUC OvR: 1.00
- Preprocesamiento: `LabelEncoder` aplicado a todas las variables categóricas

---

## 🖥 Estructura del proyecto

```
render_deploy/
├── app.py                  # Aplicación principal en Streamlit
├── models/
│   ├── xgb_model.pkl       # Modelo entrenado
│   ├── label_encoders.pkl  # Encoders para variables categóricas
│   └── feature_order.pkl   # Orden esperado de columnas
├── requirements_streamlit.txt
└── README.md
```

---

## ⚙️ Requisitos

```bash
pip install -r requirements_streamlit.txt
```

Contenido típico de `requirements_streamlit.txt`:
```
streamlit
xgboost
pandas
scikit-learn
numpy
```

---

## 🧪 Ejecución local

```bash
streamlit run app.py
```

Luego abre en tu navegador: [http://localhost:8501](http://localhost:8501)

---

## 🌐 Despliegue en Render

1. Crea un nuevo **Web Service** en [Render.com](https://render.com)
2. Usa este repositorio como fuente
3. Configura:
   - **Start command**: `streamlit run app.py --server.port=10000 --server.enableCORS=false`
   - **Python version**: 3.10 o superior
   - **Port environment variable**: Render lo detecta automáticamente
4. ¡Publica y comparte!

---

## 🧠 Autor

**Efraín Almeida**  
📘 [LinkedIn](https://www.linkedin.com/in/efrainnalmeida/)  
💻 [Repositorio en GitHub](https://github.com/efrainnalmeida/streamlit-render-integration)
🎓 Proyecto realizado con [4Geeks Academy](https://4geeksacademy.com/)

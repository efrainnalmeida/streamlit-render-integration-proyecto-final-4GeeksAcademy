# 🚀 Car Evaluation Classifier – Flask + XGBoost + Render

Este proyecto es una aplicación web construida con **Flask** que permite clasificar autos en función de sus características, utilizando un modelo de machine learning entrenado con **XGBoost**. La interfaz es sencilla, amigable y pensada para ser desplegada fácilmente en **Render**.

---

## 🧠 Modelo

- Algoritmo: `XGBoostClassifier` (multiclase)
- Dataset: UCI – Car Evaluation
- Métricas:
  - F1-Score macro: >0.98
  - AUC OvR: 1.00
- Codificación: `LabelEncoder` para features y target

---

## 🖥 Estructura del proyecto

```
render_deploy/
├── app.py                  # Servidor Flask
├── templates/
│   └── index.html          # Interfaz de entrada
├── xgb_model.pkl           # Modelo entrenado
├── label_encoders.pkl      # Encoders para features y clase
├── feature_order.pkl       # Orden esperado de columnas
├── requirements_deploy     # Dependencias para Render
└── explore_checkpoint.ipynb# Análisis exploratorio (opcional)
```

---

## ⚙️ Requisitos

```bash
pip install -r requirements_deploy
```

Contenido típico de `requirements_deploy`:
```
flask
gunicorn
xgboost
scikit-learn
pandas
```

---

## 🧪 Uso local

```bash
python app.py
```

Accede a: [http://localhost:10000](http://localhost:10000)

---

## 🌐 Despliegue en Render

1. Crea un nuevo servicio "Web Service"
2. Usa este repositorio como fuente
3. Configura:
   - **Start command**: `gunicorn app:app`
   - **Build command**: *(opcional)* `pip install -r requirements_deploy`
   - **Environment**: Python 3.10+
4. ¡Despliega!

---

## ✨ Demo

Formulario web para predecir si un auto es:
- `unacc` – no aceptable
- `acc` – aceptable
- `good` – bueno
- `vgood` – muy bueno

---

## 📍 Autor

**Efraín Almeida**  
[LinkedIn](https://www.linkedin.com/in/efrainnalmeida/) • [4Geeks Academy Project](https://4geeksacademy.com/)

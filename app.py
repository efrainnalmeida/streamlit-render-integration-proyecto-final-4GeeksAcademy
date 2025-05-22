from flask import Flask, request, render_template
import pickle
import pandas as pd
import os

# Inicializar la app
app = Flask(__name__)

# Cargar modelo y objetos necesarios

with open(os.path.join("xgb_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join("label_encoders.pkl"), "rb") as f:
    label_encoders = pickle.load(f)

with open(os.path.join("feature_order.pkl"), "rb") as f:
    feature_order = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    pred_class = None

    if request.method == "POST":
        input_data = {
            "buying": request.form["buying"],
            "maint": request.form["maint"],
            "doors": request.form["doors"],
            "persons": request.form["persons"],
            "lug_boot": request.form["lug_boot"],
            "safety": request.form["safety"]
        }

        # Convertir a DataFrame
        df_input = pd.DataFrame([input_data])

        # Codificar con LabelEncoder
        for col in df_input.columns:
            le = label_encoders[col]
            df_input[col] = le.transform(df_input[col])

        # Asegurar el orden correcto de columnas
        df_input = df_input[feature_order]

        # Predecir
        pred = model.predict(df_input)[0]
        pred_class = label_encoders["class"].inverse_transform([pred])[0]

    return render_template("index.html", prediction=pred_class)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

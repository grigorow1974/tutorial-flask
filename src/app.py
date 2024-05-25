
from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("best_model_random_forest", "rb"))
class_dict = {
    0: "Adicto",
    1: "No Adicto",
    }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        val1 = 1 if request.form["val1"] == "Yes" else 0
        val2 = 1 if request.form["val2"] == "Yes" else 0
        # Continuar con el resto de las variables...
        
        data = [[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]]
        prediction = model.predict(data)[0]
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction=pred_class)

if __name__ == "__main__":
    app.run(debug=True)
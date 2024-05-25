
from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("best_model_random_forest", "rb"))
class_dict = {
    1: "Adicto",
    0: "No Adicto",
    }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        val1 = 1 if request.form["val1"] == "Yes" else 0
        val2 = 1 if request.form["val2"] == "Yes" else 0
        val3 = 1 if request.form["val3"] == "Yes" else 0
        val4 = 1 if request.form["val4"] == "Yes" else 0
        val5 = 1 if request.form["val5"] == "Yes" else 0
        val6 = 1 if request.form["val6"] == "Yes" else 0
        val7 = 1 if request.form["val7"] == "Yes" else 0
        val8 = 1 if request.form["val8"] == "Yes" else 0
        val9 = 1 if request.form["val9"] == "Yes" else 0
        val10' = 1 if request.form["val10"] == "Yes" else 0
        
        
        data = [[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]]
        prediction = model.predict(data)[0]
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction=pred_class)

if __name__ == "__main__":
    app.run(debug=True)
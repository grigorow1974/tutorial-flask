
from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("best_model_random_forest", "rb"))
class_dict = {
    0: "Adicto",
    1: "No Adicto",
    }

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = request.form["val1"]
        val2 = request.form["val2"]
        val3 = request.form["val3"]
        val4 = request.form["val4"]
        val5 = request.form["val5"]
        val6 = request.form["val6"]
        val7 = request.form["val7"]
        val8 = request.form["val8"]
        val9 = request.form["val9"]
        val10 = request.form["val10"]     

        data = [[1 if val == "Yes" else 0 for val in [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]]]
        prediction = model.predict(data)[0]
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)

if __name__ == "__main__":
    app.run(debug=True)
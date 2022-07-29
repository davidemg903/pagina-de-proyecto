from re import template
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("home.html")

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/productos")
def productos():
    return render_template ("productos.html")

@app.route("/registrar")
def registrar():
    return render_template ("registrar.html")

if __name__ == "__main__":
    app.run(debug=True)

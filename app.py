from flask import Flask, render_template

app = Flask(__name__)

@app.route("/prueba")
def index():
    return "Hello World!"

@app.route("/")
def prueba():
    return render_template("carga.html")

if __name__ == "__main__":
    app.run(debug=True)
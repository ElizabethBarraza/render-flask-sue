from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Modificacion 2 para ver cambios en Render"

if __name__ == "__main__":
    app.run()

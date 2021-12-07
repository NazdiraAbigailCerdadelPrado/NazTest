from flask import Flask, render_template, send_file
import os

application = app = Flask(__name__)

baseDatos = [["28 nov 2021","ID"],["30 nov 2021","ID1"]] # Fecha, URLVideo, URLTexto

print(os.listdir("textos/"))
print("hola")

@app.route("/")
def hello_world():
    return render_template("speechRview.html", len = len(baseDatos), variables = baseDatos)

@app.route("/videoView")
def hello_worlds():
    return render_template("videoView.html")

@app.route("/textos/<path:filename>", methods=["GET","POST"])
def getTextos(filename):
    return send_file("textos/"+filename)

if __name__ == '__main__':
   
    app.run(debug=False, host='0.0.0.0')

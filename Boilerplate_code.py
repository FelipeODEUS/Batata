#Importando o módulo flask no projeto
from flask import Flask, render_template

#Crie um objeto da classe Flask
app = Flask(__name__)

#A função route() da classe  Flask
@app.route("/Batata")

# A URL ‘/’ é ligada à função first_flask.
def first_flask():
    Jorje = "Rei"
    return render_template("LarBatatas.html", Jorje = Jorje)

# Execute a aplicação no servidor local
app.run(debug = True)

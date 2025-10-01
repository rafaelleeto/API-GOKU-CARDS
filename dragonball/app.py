from flask import Flask,render_template,request
import requests

app = Flask(__name__)

app.secret_key = "Chave_não_segura"


@app.route("/")
def index():
    busca = int(request.args.get("page", 1))
    personagens = requests.get(f"https://dragonball-api.com/api/characters?page={busca}").json()
    print(busca)
    return render_template("index.html", personagens=personagens, busca=busca)


if __name__ == "__main__":
    
    app.run(debug=True, port=5000)
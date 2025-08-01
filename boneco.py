import os
from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")

def pagina_secundaria():
    return render_template("tela2.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render define a variável PORT
    app.run(host='0.0.0.0', port=port)
    
    
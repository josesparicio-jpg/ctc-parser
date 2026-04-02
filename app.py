from flask import Flask, request, jsonify, render_template_string
import fitz

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Carica CTC</title>
<h2>Carica PDF CTC</h2>
<form method=post enctype=multipart/form-data action="/upload">
  <input type=file name=file>
  <input type=submit value=Analizza>
</form>
"""

@app.route('/')
def home():
    return HTML

@app.route('/upload', methods=['POST'])
def upload_file():
    
    if 'file' in request.files:
        file = request.files['file']
        pdf = fitz.open(stream=file.read(), filetype="pdf")
    else:
        pdf = fitz.open(stream=request.data, filetype="pdf")

    testo = ""
    for pagina in pdf:
        testo += pagina.get_text()

    dati = {
        "finanziaria": ["Agos", "Compass"],
        "rata": [120, 250],
        "residuo": [3000, 8000],
        "ritardi": ["NO", "SI"]
    }

    return jsonify(dati)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
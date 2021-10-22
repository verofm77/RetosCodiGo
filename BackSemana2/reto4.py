from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "ok":True,
        "content": "",
        "message": "Mi api rest Flask"
    })

@app.route('/departamentos')
def departamentos():
    listaDepartamentos = ['Ancash', 'Ayacucho', 'Cajamarca', 'Callao', 'Cusco', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto',  'Moquegua', 'Tacna']

    return jsonify({
        "ok":True,
        "content": listaDepartamentos,
        "message": "Lista de departamentos"
    })

app.run(debug=True,port=5000)
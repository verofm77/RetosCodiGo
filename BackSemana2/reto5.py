from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'semana2'

mysql = MySQL(app)

@app.route('/alumnos')
def getAlumnos():
    cursor = mysql.connection.cursor()

    cursor.execute('select * from alumnos')
    data = cursor.fetchall()
    cursor.close()

    return jsonify({
        "ok":True,
        "content": data,
        "message": "Lista de alumnos"
    })

@app.route('/alumno',methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    email = request.json['email']

    cursor = mysql.connection.cursor()
    cursor.execute("insert into alumnos(nombre,email) values('"+ nombre +"','"+ email +"')")
    mysql.connection.commit()
    cursor.close()

    
    return jsonify({
        "ok":True,
        "content": "",
        "message": "Registro insertado exitosamente"
    })

if __name__ == '__main__':
    app.run(debug=True,port=5000)

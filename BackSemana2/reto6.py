from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'semana2'

mysql = MySQL(app)

@app.route('/tareaRead')
def getTareas():
    cursor = mysql.connection.cursor()
    cursor.execute('select * from tareas order by prioriTarea')
    data = cursor.fetchall()
    cursor.close()

    return jsonify({
        "ok":True,
        "content": data,
        "message":"Lista de Tareas"
    })

@app.route('/tareaCreate',methods=['POST'])
def setTarea():
    nombreTarea = request.json['nombreTarea']
    prioriTarea = request.json['prioriTarea']

    cursor = mysql.connection.cursor()
    cursor.execute("insert into tareas(nombreTarea,prioriTarea) values('"+ nombreTarea +"','"+ prioriTarea +"')")
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "ok":True,
        "content":"",
        "message":"Tarea registrada con exito"
    })

@app.route('/tareaUpdate',methods=['PUT'])
def actualTarea():
    id = request.json['id']
    nombreTarea = request.json['nombreTarea']
    prioriTarea = request.json['prioriTarea']

    cursor = mysql.connection.cursor()
    cursor.execute(f"update tareas set nombreTarea='{nombreTarea}', prioriTarea='{prioriTarea}' where id={id}")
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "ok":True,
        "content":"",
        "message":"Tarea actualizada con exito"
    })
    
@app.route('/tareaDelete',methods=['DELETE'])
def borrarTarea():
    id = request.json['id']
    
    cursor = mysql.connection.cursor()
    cursor.execute(f"delete from tareas where id={id}")
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "ok":True,
        "content":"",
        "message":"Tarea eliminada con exito"
    })

if __name__ == '__reto6__':
    app.run(debug=True,port=5000)
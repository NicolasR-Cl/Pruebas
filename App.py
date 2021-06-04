from flask import Flask, request
from flask.helpers import flash, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'mysql'
mysql = MySQL(app)

app.secret_key ='mysecretkey'
#ignore_missing_imports = True

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data = cur.fetchall()
    print(data)
    print(type(data))
    #return render_template('index.html', usuarios =data)
    return str(data)


@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        direccion = request.form['direcion']
        telefono = request.form['telefono']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (id, nombre, apellidos, direccion, telefono) VALUES(%s, %s, %s, %s, %s)',
                    (id, nombre, apellidos, direccion, telefono))
        mysql.connection.commit()
        flash("Usuario agregado !")
        return redirect(url_for('Index'))


@app.route('/edit/<id>')
def edit_usuario():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit-usuario.html', contact=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_usuario(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        direccion = request.form['direcion']
        telefono = request.form['telefono']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE usuarios
        SET nombre= %s,
            apellidos= %s,
            direccion= %s,
            telefono= %s,
        WHERE id = %s
    """, (nombre, apellidos, direccion, telefono, id))
    mysql.connection.commit()
    flash("usuario actualizado correctamente")
    return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete_usuario(id):
    cur = mysql.connection.cursor()
    cur.exucute('DELETE FROM usuarios WHERE id = {0}', format(id))
    mysql.connection.commit()
    flash('Usuario eliminado')
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3306, debug=True)
    
    #Comentario de prueba de version 

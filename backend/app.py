from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# conexión a la base de datos
def get_db():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="productos_db"
    )

@app.route('/productos', methods=['GET'])
def get_productos():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/productos', methods=['POST'])
def add_producto():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, precio) VALUES (%s, %s)",
        (data['nombre'], data['precio'])
    )
    conn.commit()
    conn.close()
    return {"msg": "Producto creado"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

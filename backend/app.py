from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

# Configurazione CORS super aperta per evitare qualsiasi blocco con GitHub Codespaces
CORS(app, resources={r"/*": {"origins": "*"}})

def get_db_connection():
    # Sostituisci questi parametri se i dati di accesso del tuo database locale sono diversi
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biblioteca"
    )

@app.route('/api/categorie', methods=['GET'])
def get_categorie():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, descrizione FROM generi ORDER BY nome ASC")
        categorie = cursor.fetchall()
        return jsonify(categorie), 200
    except Exception as e:
        return jsonify({"error": "Errore server", "details": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
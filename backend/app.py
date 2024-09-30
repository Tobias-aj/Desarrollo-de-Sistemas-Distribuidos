from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Ruta para crear un nuevo plan de recolección
@app.route('/api/crear-plan', methods=['POST'])
def crear_plan():
    data = request.json
    nombre_plan = data.get('nombre_plan')
    # fecha_inicio = data.get('fecha_inicio')
    # fecha_fin = data.get('fecha_fin')
    tipo_material = data.get('tipo_material')
    cantidad = ('cantidad')
    area_recoleccion = data.get('area_recoleccion')

    # Aquí interactuarías con la API de Bonita y la base de datos
    # bonita_url = 'http://bonita_api_url'  # URL de tu API de Bonita
    # payload = {
    #     "nombre_plan": nombre_plan,
    #     "fecha_inicio": fecha_inicio,
    #     "fecha_fin": fecha_fin,
    #     "tipo_material": tipo_material,
    #     "area_recoleccion": area_recoleccion,
    #     "frecuencia": frecuencia
    # }
    
    # Envío de datos a la API de Bonita
    # response = requests.post(bonita_url, json=payload)
    
    # if response.status_code == 200:
    #     return jsonify({"message": "Plan creado exitosamente"}), 200
    # else:
    #     return jsonify({"message": "Error al crear el plan"}), 400

    # Simulación de respuesta para pruebas
    return jsonify({"message": "Plan creado exitosamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)

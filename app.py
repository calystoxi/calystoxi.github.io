from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Appliquer CORS à toutes les routes

# Route pour recevoir les résultats du quiz
@app.route('/submit', methods=['POST'])
def submit_results():
    data = request.json
    print(f"Résultats reçus: {data}")
    # Ici, tu peux ajouter du code pour stocker les résultats
    return jsonify({"status": "success", "message": "Résultats reçus!"})

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ai-price-monitor-secret-2025'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Sample materials data
materials_data = [
    {"id": 1, "name": "Cement", "price": 425.50, "unit": "bag", "action": "WAIT"},
    {"id": 2, "name": "Steel TMT Bar", "price": 67.80, "unit": "kg", "action": "BUY"},
    {"id": 3, "name": "Red Bricks", "price": 8.50, "unit": "piece", "action": "VENDOR"},
    {"id": 4, "name": "Sand", "price": 1650.00, "unit": "cubic_meter", "action": "BUY"},
    {"id": 5, "name": "Concrete", "price": 4200.00, "unit": "cubic_meter", "action": "WAIT"}
]

@app.route('/')
def home():
    return jsonify({
        "message": "🤖 AI Material Price Monitor API", 
        "status": "running",
        "materials": len(materials_data)
    })

@app.route('/api/materials')
def get_materials():
    return jsonify({"materials": materials_data})

@app.route('/api/recommendations')
def get_recommendations():
    recommendations = [
        {"material": "Cement", "action": "WAIT", "confidence": 78, "reason": "Price expected to drop 5.2%"},
        {"material": "Steel TMT Bar", "action": "BUY", "confidence": 89, "reason": "Price expected to rise 8.5%"},
        {"material": "Red Bricks", "action": "VENDOR", "confidence": 72, "reason": "Compare suppliers"},
        {"material": "Sand", "action": "BUY", "confidence": 85, "reason": "Supply constraints coming"},
        {"material": "Concrete", "action": "WAIT", "confidence": 76, "reason": "Market volatility"}
    ]
    return jsonify({"recommendations": recommendations})

@app.route('/status')
def status():
    return jsonify({
        "system_status": "healthy",
        "total_materials": len(materials_data),
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


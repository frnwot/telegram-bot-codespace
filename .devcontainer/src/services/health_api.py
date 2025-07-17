from flask import Flask, jsonify
from src.utils.logger import get_logger

logger = get_logger(__name__)
app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "telegram-bot",
        "version": "1.0"
    })

def run_health_check():
    app.run(host='0.0.0.0', port=8080)

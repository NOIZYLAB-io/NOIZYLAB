# Dashboard Trigger API for NOIZYGATE
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger():
    action = request.json.get('action')
    # TODO: Implement grid action logic
    return jsonify({'status': 'triggered', 'action': action})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

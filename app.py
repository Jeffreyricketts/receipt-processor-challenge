from flask import Flask, jsonify, request
from uuid import uuid4
from receipt_processor import process_receipt, calculate_points

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Receipt Processor App'

# In-memory storage for receipts 
receipts = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipt_route():
    receipt_json = request.get_json()
    receipt_id = str(uuid4())
    
    # Store receipt data with ID
    receipts[receipt_id] = receipt_json
    
    # Process receipt 
    process_receipt(receipt_id, receipt_json)
    
    return jsonify({'id': receipt_id}), 200

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points_route(receipt_id):
    if receipt_id not in receipts:
        return jsonify({'error': 'Receipt ID not found'}), 404
    
    receipt = receipts[receipt_id]
    points = calculate_points(receipt)
    
    return jsonify({'points': points}), 200

if __name__ == '__main__':
    app.run(debug=True)

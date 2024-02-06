from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def get():
    return redirect('/process_data')

@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        data = request.get_json()
        # Process the data as needed
        result = {"message": "Data received successfully", "data": data}
        print(result['data'])
        return jsonify({"message": "vanthruchu mapla"})

if __name__ == '__main__':
    app.run(debug=True)
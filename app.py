from flask import Flask, jsonify
import sys

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    # Default port
    port = 3000
    # Check if a port number is provided as a command line argument
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    # Run the app on the specified port
    app.run(host="0.0.0.0", debug=True, port=port)

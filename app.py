from flask import Flask, Response

# Create Flask application instance
app = Flask(__name__)

# Define hostname and port to match original Node.js implementation
hostname = '127.0.0.1'
port = 3000

# Route handler for all paths, equivalent to Node.js createServer callback
# methods=['GET', 'POST', 'PUT', 'DELETE', ...] would be verbose, so we use methods parameter
# with a list of all HTTP methods to match Node.js behavior of responding to any request type
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def hello_world(path):
    # Set status code 200 and Content-Type header to 'text/plain'
    # Return 'Hello, World!\n' as the response body
    return Response('Hello, World!\n', status=200, mimetype='text/plain')

# Start the server if this file is run directly
if __name__ == '__main__':
    # Start Flask server on specified hostname and port
    # Output server URL to console, matching the Node.js implementation
    print(f'Server running at http://{hostname}:{port}/')
    app.run(host=hostname, port=port)
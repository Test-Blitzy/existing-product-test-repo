# hao-backprop-test
Test project for backprop integration using Python/Flask.

## Overview
This is a simple HTTP server implementation using Flask that returns a "Hello, World!" message. The application is designed to be lightweight and serves as a test platform with minimal configuration overhead.

## Requirements
- Python 3.9 or newer
- Flask framework

## Installation
1. Ensure you have Python 3.9+ installed on your system
2. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
Start the Flask server with the following command:
```
python app.py
```

The server will bind to localhost (127.0.0.1) on port 3000 and display a URL message in the console. You can access the application at http://127.0.0.1:3000/

## Verification
To verify the application is working correctly:
1. Access http://127.0.0.1:3000/ in your browser or using a tool like curl
2. Confirm you receive a "Hello, World!" response with a text/plain content type
3. Verify the HTTP status code is 200
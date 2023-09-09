from flask import Flask, request, jsonify
from flask_cors import CORS
from text_to_speech_arabic import text_to_speech_arabic
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # This will allow all domains to access your API

@app.after_request
def add_csp(response):
    response.headers['Content-Security-Policy'] = "script-src 'self' 'unsafe-inline'"
    return response

@app.route('/text_to_speech', methods=['POST', 'OPTIONS'])
def get_audio():
    if request.method == 'OPTIONS':
        # Pre-flight request. Reply successfully:
        return '', 200
    elif request.method == 'POST':
        text = request.json.get('text')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename_base = text[:10].replace(" ", "_") if len(text) > 10 else text.replace(" ", "_")
        filename = f"{filename_base}_{timestamp}.mp3"
        
        filepath = text_to_speech_arabic(text, filename)
        
        # Create a URL for the audio file
        file_url = request.url_root + filepath[1:]

        # Return the file URL in the JSON response
        return jsonify({"file_url": file_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

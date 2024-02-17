from flask import Flask, request, jsonify
from kani.config import create_kani_engine
from kani.resume import generate_resume
import asyncio
from flask_cors import CORS  # Import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the Kani engine
engine = create_kani_engine()

@app.route('/', methods=['POST'])
def process_info():
    data = request.json
    raw_text = data.get('resumeContent', '')

    # Since the sort_and_structure_personal_info function is asynchronous,
    # use asyncio to run it in the Flask route.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    processedContent = loop.run_until_complete(generate_resume(engine, raw_text))

    return jsonify({'processedContent': processedContent})

if __name__ == '__main__':
    app.run(debug=True)

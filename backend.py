from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests from frontend

load_dotenv()
api_key = os.getenv("AI21_API_KEY")
client = AI21Client(api_key)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    target_language = data.get('target_language')

    if not text or not target_language:
        return jsonify({'error': 'Text and target language are required'}), 400

    prompt = f"Please translate the following English sentence into {target_language}: '{text}' And also make sure that user enter any target language you must translate it (Specfic lanuage))and make sure you follow the tone of the sentense and translate it according to it.And if user write a single word you must translate it .And only send in response the translated sentense or word, no extra information send in response."
    messages = [ChatMessage(content=prompt, role="user")]

    try:
        response = client.chat.completions.create(
            messages=messages,
            model="jamba-mini"
        )
        translated_text = response.choices[0].message.content
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

gpt = OpenAI(
    api_key = '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'
)

app = Flask(__name__)
CORS(app)

# Define your AI model function

def mygpt(chat):
    r = gpt.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {
                'role' : 'user',
                'content' : chat
            }
        ]
    )

    return r.choices[0].message.content

# Define a route for receiving input and sending output
@app.route('/response', methods=['POST'])
def response():
    data = request.get_json()
    prompt = data['prompt']
    output = mygpt(prompt)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)

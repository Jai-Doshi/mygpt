# importing the libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

# flask app
app = Flask(__name__)
CORS(app)

# api key
gpt = OpenAI(
    api_key = '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'
)

# defining the AI model function

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

# defining a route for receiving input and sending output
@app.route('/response', methods=['POST'])
def response():
    data = request.get_json()
    text = data['text']
    output = mygpt(text)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)

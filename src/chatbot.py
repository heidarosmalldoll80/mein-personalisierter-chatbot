from flask import Flask, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

# NLTK Chatbot Pairings
pairs = [
    [r'Hallo|Hi', ['Hallo! Wie kann ich Ihnen helfen?']],
    [r'Wie geht es dir?', ['Mir geht es gut, danke! Und Ihnen?']],
    [r'(.*) Namen (.*)', ['Warum fragen Sie nach meinem Namen?']],
    [r'(.*) Hilfe (.*)', ['Was für eine Hilfe benötigen Sie?']],
    [r'Was ist dein Lieblingsessen?', ['Ich bin ein Chatbot, ich esse nichts!']],
    [r'(.*)', ['Es tut mir leid, ich verstehe nicht.']]
]

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    chatbot = Chat(pairs, reflections)
    bot_response = chatbot.respond(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)

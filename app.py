from flask import Flask, render_template, request, jsonify
from chatbot import ask_the_bot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Se a mensagem do usuário for uma resposta inicial, crie a resposta apropriada.
    if user_message.lower() in ['sim', 's']:
        response = "Ótimo! O que está acontecendo com você?"
    elif user_message.lower() in ['não', 'n', 'ñ', 'nao']:
        response = "Tudo bem! Se mudar de ideia, estou aqui para conversar."
    else:
        response = ask_the_bot(user_message)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

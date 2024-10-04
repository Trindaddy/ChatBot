# Import (Importar biblioteca da AI)
import google.generativeai as genai
import re

# Key API (Chave API)
GOOGLE_GEMINI_API_KEY = "AIzaSyCG04rvyg0DwxslyshttXdGb3dLVr9IG14"

# Configure API Key (Configurar Chave API)
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

# Choosing the model IA (Escolhendo o modelo de IA)
model = genai.GenerativeModel("gemini-1.5-flash-8b-exp-0924")

# Function to shorten response (if it is too long) (Função para abreviar resposta (caso seja muito longa))
def summarize_response(text):
    if len(text) > 400:  # Abrevia respostas maiores que 400 caracteres
        summarized = text[:200] + text[-200:]  # Mostra o começo e o final da resposta
        return summarized
    return text

# Function for the bot response (Função para resposta do bot)
def ask_the_bot(message):
    # Define o papel do bot
    expert_prompt = (
        "Você é um psicólogo experiente com 20 a 50 anos de prática. "
        "Por favor, responda como um profissional, focando em questões emocionais e psicológicas. "
        "Não responda a perguntas fora desse escopo."
    )

    # Combine o prompt com a mensagem do usuário
    full_message = f"{expert_prompt}\n\n{message}"
    
    chat = model.start_chat(history=[])
    response = chat.send_message(full_message)

    # Remove qualquer asterisco ou caractere especial não desejado
    clean_response = re.sub(r'[*]', '', response.text)
    
    # Se a mensagem do usuário incluir bullying ou cyberbullying, aplica a abreviação
    if "bullying" in message.lower() or "cyberbullying" in message.lower() or "racismo" in message.lower() or "homofobia" in message.lower():
        clean_response = summarize_response(clean_response)
    
    return clean_response


# Function to format the bot's response (Função para formatar a resposta do bot)
def format_bot_response(text):
    return f"\033[1;34m{text}\033[0m"

# Receive user prompt (Receber comando do usuário)
def chat_with_the_user():
    print("Olá, eu sou seu amigo PsicoBot e estou aqui para te ajudar. Você gostaria de conversar sobre como se sente? (sim/não)")
    response = input().strip().lower()
    
    if response in ['sim', 's']:
        while True:  # Loop para manter a conversa
            sentiment = input("Me conte um pouco do que está acontecendo com você: ")
            # Gerar resposta como psicólogo
            mensage_psychologist = f"Você disse que está se sentindo {sentiment}. Falar sobre isso é um bom começo. Lembre-se de cuidar de você e, se possível, converse com alguém de confiança."
            response_ia = ask_the_bot(mensage_psychologist)
            
            # Formata e exibe a resposta do bot
            print(format_bot_response(f"\nComo seu amigo PsicoBot: {response_ia}"))

            # Pergunta se o usuário quer continuar a conversa
            response_final = input("\nQuer conversar mais um pouco? (sim/não): ").strip().lower()
            if response_final in ['não', 'n', 'ñ']:
                print("Tudo bem! Se mudar de ideia, estou aqui para conversar.")
                # Sugestão de contato com o CVV
                print(format_bot_response("\nLembre-se, é muito importante falar com alguém que possa te ajudar diretamente. Sugiro que entre em contato com o CVV (Centro de Valorização da Vida) pelo número 188 ou pelo site https://www.cvv.org.br."))
                break  # Encerra o loop se a resposta for não
    else:
        print("Tudo bem! Se mudar de ideia, estou aqui para conversar.")

if __name__ == '__main__':
    chat_with_the_user()
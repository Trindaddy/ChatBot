# Bibliotecas usadas pip install flask, re, google-generativeai
Diário de Bordo do chatbot Ant-bullying

#Início do Projeto
- Data e Hora: O projeto começou às 22:30 do dia 04/10 e foi até às 2:30 da madrugada do dia 05/10, com um segundo período de uso das 08:00 até as 12:00 do dia 05/10.
- Objetivo Inicial: O foco principal era criar um chatbot que agisse como um psicólogo com 20-30 anos de experiência, utilizando o Google Generative AI para fornecer respostas humanizadas e direcionadas ao combate de bullying e cyberbullying.

# Desenvolvimentos Iniciais
- Configuração do Modelo: Implementação do modelo "gemini-1.5-flash-8b-exp-0924" da Google Generative AI, usando uma API Key fornecida pela Google. O modelo foi ajustado para dar respostas focadas em saúde mental, fornecendo conselhos psicológicos de acordo com o contexto do usuário.

# Funções Criadas:
- Função principal para interagir com o bot e receber respostas em tempo real.
- Uso de expressões regulares para remover caracteres indesejados, como asteriscos, das respostas.
- Inicialmente, o foco estava em permitir uma interação simples onde o usuário pudesse contar sobre seus problemas, e o chatbot respondia com sugestões de apoio psicológico.
  
# Modificações e Melhorias
- Restrições de Conhecimento: Ao longo do desenvolvimento, uma das necessidades foi restringir o chatbot para atuar exclusivamente como um psicólogo, evitando respostas sobre tópicos fora da área de saúde mental. O bot passou a rejeitar perguntas que não fossem relacionadas ao contexto psicológico ou ao combate de bullying/cyberbullying.
- Abreviação de Respostas Longas: Outra melhoria significativa foi a introdução de um sistema de abreviação automática para respostas que excedem 400 caracteres. Isso foi feito para tornar as respostas mais acessíveis e fáceis de ler, especialmente em diálogos mais longos.
- Responsividade do Chat: Com o desenvolvimento da interface de chat, foi implementado um CSS mais aprimorado, que tornou o layout responsivo e adaptado a diferentes tamanhos de tela. O chat foi estilizado para ter um design de chatbot profissional, com botões de envio posicionados ao lado do campo de entrada, e o chatbox foi expandido para maior largura.

# Etapas Finais
- Pergunta de Continuidade: Para melhorar a interação, o bot agora pergunta ao usuário se deseja continuar a conversa ao final de cada interação. Se o usuário escolher não continuar, o bot finaliza a conversa com uma mensagem motivacional e recomenda que o usuário entre em contato com o CVV (Centro de Valorização da Vida).
- Integração de CVV: O bot foi programado para fornecer informações sobre o CVV, como o número de telefone 188 e o site oficial, para casos onde o usuário precise de suporte adicional.

# Conclusão
- O desenvolvimento do chatbot evoluiu de uma simples interface de interação para um sistema completo e responsivo, focado em saúde mental. O bot foi ajustado para agir como um psicólogo experiente, dar conselhos personalizados e saber quando encerrar a conversa de maneira adequada. O design do chat também foi aperfeiçoado, proporcionando uma experiência amigável e eficiente para os usuários.

- Esses foram os principais desenvolvimentos e aprimoramentos feitos desde o início até o fim do projeto.

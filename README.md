MeskGPT
MeskGPT é uma aplicação web em Python que integra múltiplas ferramentas de IA utilizando Streamlit e APIs Hugging Face. Com ela, você pode gerar textos, resumir conteúdos e conversar com um assistente virtual personalizado.

Funcionalidades
Gerar Texto: Crie textos automaticamente a partir de um prompt.
Resumir Texto: Resuma qualquer texto colado na caixa de entrada.
Abrir Chat: Converse com uma IA que responde de forma divertida e personalizada.
Tecnologias Utilizadas
Python
Streamlit
Hugging Face API
Como Executar
Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Crie e ative um ambiente virtual:

python -m venv .venv
.venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Execute a aplicação:

streamlit run main.py

Estrutura do Projeto:

├── main.py
├── hfapi_chatcompletion.py
├── hfapi_summarization.py
├── hfapi_textgeneration.py
├── text2image.py
├── text2speech.py
├── .env
├── .gitignore
└── __pycache__/

Configuração
Crie um arquivo .env com suas chaves de API do Hugging Face, se necessário.
As dependências devem estar listadas em requirements.txt.

by Rodrigo Mesk

# Bot de Automação de Mensagens do WhatsApp

Este script em Python automatiza o envio de mensagens pelo WhatsApp, utilizando dados de uma planilha Excel. Ele é especialmente útil para lembrar clientes sobre vencimentos de boletos, por exemplo.

## Funcionalidades

- Envio automatizado de mensagens via WhatsApp para uma lista de contatos.
- Mensagem personalizada com nome do cliente e data de vencimento.
- Registro de erros em um arquivo CSV.

## Requisitos

Para executar este projeto, você precisa ter Python 3 instalado e as seguintes bibliotecas:

- `openpyxl`: Para manipulação de arquivos Excel.
- `urllib`: Biblioteca padrão do Python para manipulação de URLs.
- `webbrowser`: Biblioteca padrão do Python para abrir URLs no navegador.
- `time`: Biblioteca padrão do Python para manipulação de tempo (sleep).
- `pyautogui`: Para automação de interface gráfica.

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/bot-whatsapp-automacao.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd bot-whatsapp-automacao
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

4. Instale as dependências:
    ```sh
    pip install openpyxl pyautogui
    ```

## Como usar

1. Prepare a planilha `PlanilhaContatos.xlsx` com os seguintes campos:
    - Nome
    - Telefone (com código do país, por exemplo, 5511999999999)
    - Data de vencimento (no formato `YYYY-MM-DD`)

2. Abra o WhatsApp Web no seu navegador.

3. Execute o script principal:
    ```sh
    python bot_whatsapp.py
    ```

4. O script abrirá o WhatsApp Web, lerá os dados da planilha e enviará mensagens automaticamente.

## Estrutura do Projeto

- `bot_whatsapp.py`: Script principal que contém o código do bot de automação.

## Observações

- O script usa o `pyautogui` para clicar no botão de envio da mensagem. Certifique-se de ter a imagem `send.png` do botão de envio no mesmo diretório do script.
- Certifique-se de que o WhatsApp Web esteja logado e visível no navegador antes de executar o script.
- O tempo de espera (`sleep`) pode precisar ser ajustado dependendo da velocidade da sua conexão com a internet.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.



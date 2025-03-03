# Projeto de Testes de API

Este projeto contém testes automatizados para a API pública `https://jsonplaceholder.typicode.com/posts`. Os testes foram desenvolvidos em Python utilizando a biblioteca `requests` e o framework `pytest`.

## Funcionalidades

- **Testes para o endpoint GET /posts**:
  - Valida o status code da resposta.
  - Verifica se a resposta contém uma lista de posts.
- **Testes para o endpoint POST /posts**:
  - Gera dados aleatórios para o corpo da requisição.
  - Valida o status code da resposta.
  - Verifica se a resposta contém um ID único.

## Pré-requisitos

Antes de executar o projeto, certifique-se de que você possui os seguintes requisitos instalados:

- **Python 3.8 ou superior**:
  - Verifique a instalação do Python executando no terminal:
    ```bash
    python --version
    ```
  - Caso não tenha o Python instalado, baixe e instale a partir do [site oficial](https://www.python.org/downloads/).

- **Pip (gerenciador de pacotes do Python)**:
  - O Pip geralmente já vem instalado com o Python. Verifique a instalação executando:
    ```bash
    pip --version
    ```

## Passos para Configuração e Execução

Siga os passos abaixo para configurar o projeto e executar os testes.

- **1. Clone o Repositório**

Clone o repositório do projeto para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/projeto-api-tests.git
```
Navegue até a pasta do projeto:

```bash
cd projeto-api-tests
```

- **2. Crie e Ative um Ambiente Virtual (Opcional, mas Recomendado)**:
Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```
Ative o ambiente virtual:
No Windows:

```bash
venv\Scripts\activate
```

No macOS/Linux:

```bash
source venv/bin/activate
```

- **3. Instale as Dependências**:
Instale as bibliotecas necessárias listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

As dependências instaladas incluem:

requests: Para fazer requisições HTTP.
pytest: Framework para execução de testes.
pytest-html: Para gerar relatórios HTML dos testes.

- **4. Executando os Testes**:
Para executar todos os testes, use o seguinte comando:

```bash
python run_tests.py
```

Isso fará o seguinte:

Executará os testes na pasta tests/.
Exibirá os resultados no terminal.
Gerará um relatório HTML na pasta reports/.

- **5. Visualizando o Relatório HTML**:
Após a execução dos testes, um relatório HTML será gerado na pasta reports/. Para visualizá-lo:

Abra o arquivo report.html no navegador.

Analise os resultados dos testes, incluindo quais passaram ou falharam.

- **6. Executando Testes Individuais**:
Se desejar executar um teste específico, use o comando pytest diretamente. Por exemplo:

```bash
pytest tests/test_get_posts.py -v
```

Ou:

```bash
pytest tests/test_create_post.py -v
```


A opção -v ativa o modo verboso, exibindo detalhes sobre a execução dos testes.

# Projeto PYTHON-REQUESTS-AUTOMATION

## Python Requests Automation  
Este é um projeto de automação de testes para APIs, utilizando Python, `requests` e `pytest`, focado em validar os endpoints de criação (`POST /posts`) e recuperação (`GET /posts`) de posts. A pipeline CI/CD foi configurada com GitHub Actions para execução automatizada e geração de relatórios.

---

## 1. Sobre o Projeto  
O `PYTHON-REQUESTS-AUTOMATION` automatiza testes de integração para APIs, garantindo que os endpoints de criação e recuperação de posts funcionem corretamente. Os testes são escritos em Python com `pytest`, utilizando `requests` para fazer chamadas HTTP, e incluem geração de logs e relatórios HTML para análise.

### Principais Características  
- Testa os endpoints `POST /posts` (criação de posts) e `GET /posts` (recuperação de posts).  
- Utiliza `requests` para chamadas HTTP e `pytest` para estruturação e execução dos testes.  
- Gera relatórios HTML para visualização dos resultados dos testes.  
- Integração com GitHub Actions para CI/CD automatizado.  

---

## 2. Descrição dos Arquivos Principais  
- **`test_create_post.py`**: Contém o teste para o endpoint `POST /posts`, que gera dados aleatórios, faz uma requisição POST, e valida a resposta (status 201, unicidade de IDs, tipos de dados, e correspondência dos dados enviados e retornados).  
- **`test_get_posts.py`**: Contém o teste para o endpoint `GET /posts`, que valida a lista de posts (status 200, estrutura da resposta, unicidade de IDs, tipos de dados, e presença de campos obrigatórios).  
- **`requirements.txt`**: Lista as dependências do projeto, como `requests`, `pytest`, e `pytest-html` para geração de relatórios.  
- **`ci_cd.yml`**: Arquivo de configuração da pipeline CI/CD no GitHub Actions para execução automatizada dos testes com `pytest`.  
- **`settings.py` (em config/)**: Contém configurações do projeto, como o `BASE_URL` da API testada.  
- **`data_generator.py` e `logger.py` (em utils/)**: Módulos utilitários para geração de dados aleatórios e log de informações/validações durante os testes.  

---

## 3. Pré-requisitos  
Antes de configurar e executar o projeto localmente, certifique-se de ter instalado: 
- **python3** (versão 3.13 recomendada).  
- **pip** (gerenciado pelo Python).  
- **Git** (para clonagem do repositório). 

## 4. Configuração do Projeto  

### 4.1 Clonar o Repositório  
1. Clone o repositório do GitHub:  
   ```bash
   git clone https://github.com/joao-314/CYPRESS-AMAZON-TEST.git
   cd CYPRESS-AMAZON-TEST

### 4.2 Criar e Ativar um Ambiente Virtual
1. Crie um ambiente virtual para isolar as dependências do projeto
   ```bash
   python -m venv venv

2. Ative o ambiente virtual(Em Windows):
   ```bash
   venv\Scripts\activate

### 4.3 Instalar Dependências
1. Instale as dependências listadas no requirements.txt:
   ```bash
   pip install -r requirements.txt

## 5. Executando os Testes Localmente

### 5.1 Executar Testes com pytest
1. Execute todos os testes no diretório tests/ usando pytest
  ```bash
  pytest tests/ -v --html=reports/report.html --self-contained-html

2. Os resultados serão exibidos no terminal e o relatório HTML estará disponível em reports/report.html.

## 6. Validação da Pipeline

### 6.1 Verificar o Disparo Automático dos Testes
1. Faça um push para o branch main ou abra um pull request para o branch main.

2. Acesse a aba "Actions" no GitHub para verificar se o pipeline foi acionado automaticamente.

### 6.2 Verificar Relatórios de Falhas
1. Simule uma falha nos testes (ex.: altere o BASE_URL em config/settings.py para um valor inválido ou force um erro, como o comentário #Erro forçado em test_create_post.py).

2. Verifique se o relatório HTML (reports/report.html)

### 6.3 Verificar Paralelismo
1. Para executar os testes em paralelo, ajuste o ci_cd.yml para usar uma ação como pytest-actions/annotate-failures:
    ```bash
    name: Run pytest tests in parallel
    uses: pytest-actions/annotate-failures@v3
    with:
      test-dir: tests/
      parallel: true
      report-file: reports/report.html

2. Verifique se os testes são executados em paralelo e se o tempo de execução é reduzido.

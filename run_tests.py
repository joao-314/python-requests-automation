import pytest

if __name__ == "__main__":
    # Executa todos os testes na pasta "tests/"
    # Adiciona a opção "-v" para exibir detalhes no terminal
    # Gera um relatório HTML na pasta "reports/"
    pytest.main(["-v", "--html=reports/report.html"])
import pytest
import requests
import json

from config.settings import BASE_URL
from utils.data_generator import generate_random_data
from utils.logger import print_section, print_validation  # Importando as funções do módulo utils



def test_create_post():
    """
    Testa o endpoint POST /posts.
    Gera dados aleatórios, faz uma requisição POST e valida a resposta.
    """
    # Lista para armazenar IDs gerados
    generated_ids = []
    
    # Gera dados aleatórios para o POST
    data = generate_random_data()
    headers = {"Content-Type": "application/json; charset=UTF-8"}

    # Exibe os dados enviados
    print_section("Dados Enviados")
    print(json.dumps(data, indent=4))  # Formata o JSON para melhor legibilidade

    # Faz a requisição POST
    response = requests.post(BASE_URL, data=json.dumps(data), headers=headers)

    # Exibe a resposta da API
    print_section("Resposta da API")
    print(json.dumps(response.json(), indent=4))  # Formata o JSON para melhor legibilidade

    # Validações básicas
    print_section("Validações Básicas")
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    print_validation("Status code is 201")

    # Converte a resposta para JSON
    response_data = response.json()

    # Valida se o ID é único
    assert response_data["id"] not in generated_ids, f"ID {response_data['id']} is not unique"
    generated_ids.append(response_data["id"])
    print_validation(f"ID {response_data['id']} is unique") #Erro forçado

    # Verifica se a resposta contém um ID único
    assert "id" in response_data, "Expected 'id' in the response, but it was not found"
    print_validation("Response contains 'id'")
    
    assert isinstance(response_data["id"], int), "Expected 'id' to be an integer"
    print_validation("'id' is an integer")

    # Validações se os dados enviados correspondem aos dados retornados
    print_section("Validações de Dados Enviados vs Retornados")
    assert response_data["title"] == data["title"], "Title does not match the sent data"
    print_validation("Title matches the sent data")

    assert response_data["body"] == data["body"], "Body does not match the sent data"
    print_validation("Body matches the sent data")

    assert response_data["userId"] == data["userId"], "User ID does not match the sent data"
    print_validation("User ID matches the sent data")

    # Validações adicionais de estrutura e tipos de dados
    print_section("Validações de Estrutura e Tipos de Dados")
    assert isinstance(response_data, dict), "Response data should be a dictionary"
    print_validation("Response data is a dictionary")

    # Valida se cada campo requerido está presente
    required_fields = ['userId', 'id', 'title', 'body']
    for field in required_fields:
        assert field in response_data, f"Response is missing '{field}'"
        print_validation(f"Response has '{field}'")

    # Validações dos tipos e restrições
    assert isinstance(response_data['userId'], int), "userId should be an integer"
    print_validation("'userId' is an integer")

    assert isinstance(response_data['id'], int), "id should be an integer"
    print_validation("'id' is an integer")

    assert isinstance(response_data['title'], str) and response_data['title'].strip(), "title should be a non-empty string"
    print_validation("'title' is a non-empty string")
    
    assert isinstance(response_data['body'], str) and response_data['body'].strip(), "body should be a non-empty string"
    print_validation("'body' is a non-empty string")
    
    print_section("Resultado Final")
    print_validation("POST /posts test passed successfully!", status="PASS")

# Execução do teste (opcional, apenas para rodar este arquivo individualmente)
if __name__ == "__main__":
    pytest.main([__file__])
import requests
import pytest
import json

from config.settings import BASE_URL
from utils.logger import print_section, print_validation  # Importando as funções do módulo utils

def test_get_posts():
    unique_ids = set()  # Usando um conjunto para rastrear IDs únicos
    
    # Faz a requisição GET
    response = requests.get(BASE_URL)

    # Validações básicas
    print_section("Validações Básicas")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    print_validation("Status code is 200")

    posts = response.json()
    assert isinstance(posts, list), "Expected response to be a list"
    print_validation("Response is a list")

    assert len(posts) > 0, "Expected at least one post, but got an empty list"
    print_validation(f"Number of posts: {len(posts)}")

    # Validações da estrutura de cada post
    for post in posts:
        print_section(f"Post {post['id']} validations")

        # Exibe o JSON do post atual
        print("Dados do Post:")
        print(json.dumps(post, indent=4))  # Formata o JSON para melhor legibilidade

        # Valida se o ID é único ou não
        assert post['id'] not in unique_ids, f"Duplicate ID found: {post['id']}"
        unique_ids.add(post['id'])
        print_validation("Post ID is unique")
        
        assert isinstance(post, dict), "Each post should be a dictionary"
        print_validation("Post is a dictionary")

        assert 'userId' in post, "Post is missing 'userId'"
        print_validation("Post has 'userId'")

        assert 'id' in post, "Post is missing 'id'"
        print_validation("Post has 'id'")

        assert 'title' in post, "Post is missing 'title'"
        print_validation("Post has 'title'")

        assert 'body' in post, "Post is missing 'body'"
        print_validation("Post has 'body'")

        # Validações dos tipos e restrições
        assert isinstance(post['userId'], int), "userId should be an integer"
        print_validation("'userId' is an integer")

        assert isinstance(post['id'], int), "id should be an integer"
        print_validation("'id' is an integer")

        assert isinstance(post['title'], str) and post['title'].strip(), "title should be a non-empty string"
        print_validation("'title' is a non-empty string")

        assert isinstance(post['body'], str) and post['body'].strip(), "body should be a non-empty string"
        print_validation("'body' is a non-empty string")

    print_section("Resultado Final")
    print_validation("GET /posts test passed successfully!", status="PASS")

# Execução do teste (opcional, apenas para rodar este arquivo individualmente)
if __name__ == "__main__":
    pytest.main([__file__])
import random
import string

def generate_random_data():
    """
    Gera dados aleatórios para o corpo de uma requisição POST.
    
    Retorna:
        dict: Um dicionário contendo um título, corpo e userId aleatórios.
    """
    # Gera um título aleatório com 10 caracteres
    title = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    # Gera um corpo aleatório com 50 caracteres
    body = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
    
    # Gera um userId aleatório entre 1 e 10
    user_id = random.randint(1, 10)
    
    return {
        "title": title,
        "body": body,
        "userId": user_id
    }
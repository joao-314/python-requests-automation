def print_section(title):
    """
    Função para imprimir um título de seção formatado.
    
    Args:
        title (str): O título da seção.
    """
    print(f"\n{'=' * 50}")
    print(f"{title.upper()}")
    print(f"{'=' * 50}")

def print_validation(message, status="OK"):
    """
    Função para imprimir mensagens de validação formatadas.
    
    Args:
        message (str): A mensagem a ser exibida.
        status (str): O status da validação (padrão é "OK").
    """
    print(f"[{status}] {message}")
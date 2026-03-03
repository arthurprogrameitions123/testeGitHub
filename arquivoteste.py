import random
import string

def gerar_senha(tamanho=12):
    # Define os caracteres possíveis: letras, números e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Escolhe caracteres aleatórios e os junta em uma string
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    return senha

# --- Execução do Programa ---
print("--- GERADOR DE SENHAS SEGURO ---")
try:
    qtd = int(input("Digite o comprimento da senha: "))
    nova_senha = gerar_senha(qtd)
    print(f"\nSua nova senha é: {nova_senha}")
    print("Guarde-a em local seguro!")
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")


#teste de commit

# exemplo_1.py
# Manipulação de dados com dicionário
usuarios = []

def cadastrar_usuario(nome):
    usuarios.append({"nome": nome})
    print(f"Usuário '{nome}' cadastrado com sucesso!")

def listar_usuarios():
    print("Usuários cadastrados:")
    for usuario in usuarios:
        print(f"- {usuario['nome']}")

# Execução de teste
cadastrar_usuario("Lais")
listar_usuarios()

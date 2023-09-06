# Dados iniciais (simulando informações de pontos e níveis dos usuários)
usuarios = {
    "João": {"pontos": 100, "nivel": 1},
    "Maria": {"pontos": 50, "nivel": 1},
    "Pedro": {"pontos": 75, "nivel": 1}
}

# Função para adicionar um novo usuário
def adicionar_usuario(usuario):
    if usuario not in usuarios:
        usuarios[usuario] = {"pontos": 0, "nivel": 1}
        print(f"Usuário {usuario} adicionado com sucesso.")
    else:
        print("Usuário já existe.")

# Função para realizar a reciclagem
def reciclar(usuario, peso_quilos):
    if usuario in usuarios:
        pontos_ganhos = peso_quilos * 10  # Conversão simples de quilos para pontos (10 pontos por quilo)
        usuarios[usuario]["pontos"] += pontos_ganhos
        atualizar_nivel(usuario)  # Verificar e atualizar o nível do usuário
        print(f"{peso_quilos} quilos de lixo reciclado por {usuario} resultaram em {pontos_ganhos} pontos.")
    else:
        print("Usuário não encontrado.")

# Função para verificar e atualizar o nível do usuário
def atualizar_nivel(usuario):
    if usuarios[usuario]["pontos"] >= 150:
        usuarios[usuario]["nivel"] = 2

# Loop principal
while True:
    print("\nMenu:")
    print("1. Realizar reciclagem")
    print("2. Exibir pontos e níveis dos usuários")
    print("3. Adicionar novo usuário")
    print("4. Encerrar programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuarios_cadastrados = ", ".join(usuarios.keys())
        mensagem_input = f"Informe o nome do usuário que está realizando a reciclagem ({usuarios_cadastrados}): "
        usuario = input(mensagem_input)
        peso_quilos = float(input("Informe o peso em quilos do lixo reciclado: "))
        reciclar(usuario, peso_quilos)
    
    elif opcao == "2":
        print("\nPontuação e Níveis dos Usuários:")
        for usuario, dados in usuarios.items():
            print(f"{usuario}: Pontos: {dados['pontos']} - Nível: {dados['nivel']}")
    
    elif opcao == "3":
        novo_usuario = input("Informe o nome do novo usuário: ")
        adicionar_usuario(novo_usuario)
    
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

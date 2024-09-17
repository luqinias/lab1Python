nome = input("Digite seu nome: ");
numero_aleatorio = hash(nome) % 100;
tentativas = 0;

while True:    
    chute = int(input("Adivinhe o número (de 0 a 99): "));
    tentativas += 1;
    
    if chute == numero_aleatorio:
        print(f"Acertou o número {numero_aleatorio} em {tentativas} tentativas!");
        break;
    elif chute < numero_aleatorio:
        print("É menor");
    else:
        print("É maior");

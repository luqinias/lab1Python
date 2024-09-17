numero = int(input("Informe um número inteiro para verificar se é perfeito: "));
soma_divisores = 0;
divisores = [];

for i in range(1, numero):
    if numero % i == 0:
        divisores.append(i);
        soma_divisores += i;

for i in divisores: print(f"Divisor: {i}");

if soma_divisores == numero:
    print(f"O número {numero} é perfeito, sendo igual à soma de seus divisores próprios!");
else:
    print(f"O número {numero} não é igual à soma de seus divisores próprios ({soma_divisores}).");

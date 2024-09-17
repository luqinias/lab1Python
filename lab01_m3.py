numero = int(input("Informe o número não negativo para o cálculo do fatorial: "));

if numero < 0:
    print("O número deve ser não negativo.");
else:
    fatorial = 1;
    if numero == 0 or numero == 1:
        fatorial = 1
    else:
        for i in range(2, numero + 1):
            fatorial *= i
    
    print(f"{numero}! = {fatorial}")

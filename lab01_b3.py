peso = float(input("Digite o seu peso (em kg): "));
altura = float(input("Digite a sua altura (em metros): "));
imc = float(peso/(altura*altura));

if imc >= 30:
    print(f"Seu IMC é: {imc:0.1f}\nAtenção! Índice indica obesidade.");
elif imc <= 16.4:
    print(f"Seu IMC é: {imc:0.1f}\nAtenção! Índice indica magreza.");
else: 
    print(f"Seu IMC é: {imc:0.1f}");

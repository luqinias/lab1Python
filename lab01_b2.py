num1 = int(input("Digite o primeiro número inteiro: "));
num2 = int(input("Digite o segundo número inteiro: "));

soma = num1 + num2;
subtra = num1 - num2;
multipli = num1 * num2;
divi = float(num1 / num2);
diviInt = int(num1 / num2);
resto = num1 % num2;
potenc = num1 ** num2;

print(f"""
      Soma: {soma},
      Subtração: {subtra},
      Multiplicação: {multipli},
      Divisão: {divi},
      Divisão inteira: {diviInt},
      Resto da divisão: {resto},
      Potenciação: {potenc}
    """);


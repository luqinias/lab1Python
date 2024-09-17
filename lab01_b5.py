sigla = input("Deseja converter de Celsius ou Fahrenheit [C/F]? ");

if sigla.upper() == "C":
    temp = float(input("Digite a temperatura em °C: "));
    temp = (temp * 1.8)+32;
    print(f"Temperatura em Fahrenheit: {temp:0.2f}");

elif sigla.upper() == "F":
    temp = float(input("Digite a temperatura em Fahrenheit: "));
    temp = (temp-32)/1.8;
    print(f"Temperatura em °C: {temp:0.2f}");
else: 
    print("Verifique se digitou conforme a instrução!");



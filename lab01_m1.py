import sys;

try: 

    a = float(input("Informe o lado A do triângulo: "));
    b = float(input("Informe o lado B do triângulo: "));
    c = float(input("Informe o lado C do triângulo: "));

except ValueError:
    print("Digite somente números para as medidas A, B e C!");
    sys.exit(1);
if a<=0 or b<=0 or c<=0 :
   print("Os lados fornecidos violam a condição de existência de um triângulo.");
   sys.exit();

if a>=b+c or b>=c+a or c>=a+b :
   print("Os lados fornecidos violam a condição de existência de um triângulo.");
   sys.exit();

if a==b and b==c :
   print("É um triangulo equilátero.");
    
elif a==b or b==c or c==a :
   print("É um triangulo isósceles.");

else:
   print("É um triângulo escaleno.");
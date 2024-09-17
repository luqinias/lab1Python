numero = int(input("Informe a tabuada de qual número deseja saber: "));
tabuada = {0,1,2,3,4,5,6,7,8,9,10};
for i in tabuada:
    result = i * numero;
    print(f"{i} X {numero} = {result}");
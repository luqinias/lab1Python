nota = float(input("Digite sua nota (entre 0 e 100): "));

if nota >= 90:
    print(f"A nota {nota} traduz-se para o conceito 'A'");
elif nota >= 75 and nota < 90:
    print(f"A nota {nota} traduz-se para o conceito 'B'");
elif nota >= 60 and nota < 75:
    print(f"A nota {nota} traduz-se para o conceito 'C'");
elif nota >= 40 and nota < 60:
    print(f"A nota {nota} traduz-se para o conceito 'D'");
else:
    print(f"A nota {nota} traduz-se para o conceito 'F'");

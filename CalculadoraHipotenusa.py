def hipotenusa(a,b):
    return (a**2+b**2)**0.5
co = int(input("Informe o cateto oposto: "))
ca = int(input("Informe o cateto adjacente: "))
res = hipotenusa(co,ca)
print(f"A hipotenusa é igual a {res}.")
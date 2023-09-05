# leia o tamanho dos arranjos
# ============================>
tam = int(input())

# leia o arranjo a
# ============================>
a=[0]*tam
a=list(map(int, input().split()))[:tam]

# leia o arranjo b
# ===========================>
b=[0]*tam
b=list(map(int, input().split()))[:tam]

# calcule a soma dos arranjos
# ===========================>
soma=[0]*tam
for i in range(0, tam):
    soma[i] =a[i] + b[i]
# imprima o arranjo da soma
# ===========================>
print(soma)

arcoiris = ("rojo","naranja","amarillo","verde")
print(arcoiris)

print("")
print("--logitud arcoiris--")
print(len(arcoiris))

print("")
animales=("pantera",20,"estatura",1.7)
print(animales)

print("")
print("elementos de la tupla")
print(animales[2])

print("")
rateros = ("juan", "ana", "pedro")
y= list(rateros)
y[1] = "polainas"
x=tuple(y)
print(x)

print("")
print("Agregando elementos")
Nanimal=("boby","cheetos")
y= list(Nanimal)
print(y)
y.append("tontolin")
otratupla=tuple(y)
print(otratupla)

print("")
print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)
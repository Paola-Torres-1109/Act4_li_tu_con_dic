# ejemplo de uso de listas 
misnovios = ["rauw alejandro", "gabito ballesteros", "peso pluma"]
misnumeros= ["28", "7", "1"]

#mostrando mis novios
print(misnovios)

#mostrando mis numeros
print(misnumeros)

print("")
print("--- accediendo a los elementos de la lista ---")
print(misnovios[1])


print("")
if "rauw" in misnovios:
    print("Si, 'rauw alejandro' esta en la lista de mis novios")
else: 
    print("Chale no es mi novio")


print("")
print("Numero de novios")
nnovios=len(misnovios)
print(f"Numero de novios {nnovios}")


posicion=0
print("")
print("ciclo for en listas")
for medianaranja in misnovios:
    print(posicion,"",medianaranja)
    posicion=posicion+1
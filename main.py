casos = int(input())

resultados = []

for i in range(casos):
    entrada = input()
    pares = entrada.split(";")

    diccionario = {}

    # 1. Inicializar todos los nodos en 0
    for par in pares:
        nodo = par.split(":")[0]
        diccionario[nodo] = 0

    # 2. Contar conexiones
    for par in pares:
        izquierda, derecha = par.split(":")

        # conexiones salientes del nodo
        diccionario[izquierda] += len(derecha)

        # conexiones entrantes desde otros nodos
        for letra in derecha:
            if letra in diccionario:
                diccionario[letra] += 1

    # 3. Formatear salida
    linea = []
    for clave in sorted(diccionario):
        linea.append(f"{clave}: {diccionario[clave]}")

    resultados.append(" ".join(linea))

print("\nResultados:")
for resultado in resultados:
    print(resultado)

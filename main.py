# importando a biblioteca threading do Python para trabalhar com threads
import threading

# método que será executado por cada thread, contém a lista de números a serem somados, o resultado da soma e o índice do resultado a ser armazenado
def soma_parcial(lista, resultado, indice):
    resultado[indice] = sum(lista)

# lista de números a serem somados
numeros = [33, 23, 3, 44, 400, 10]

# dividir a lista de números em partes
parte1 = numeros[:2]
parte2 = numeros[2:4]
parte3 = numeros[4:]

# lista para armazenar os resultados
resultado = [0, 0, 0]

# criando as threads
thread1 = threading.Thread(target=soma_parcial, args=(parte1, resultado, 0))
thread2 = threading.Thread(target=soma_parcial, args=(parte2, resultado, 1))
thread3 = threading.Thread(target=soma_parcial, args=(parte3, resultado, 2))

# iniciando as threads
thread1.start()
thread2.start()
thread3.start()

# esperando as threads terminarem
thread1.join()
thread2.join()
thread3.join()

# calcula a soma total
soma_total = sum(resultado)

print(f"A soma total é: {soma_total}")
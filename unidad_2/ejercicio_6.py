# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular mode, median y mean de dichos números. Un ejemplo de su uso es el
# siguiente:

# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)

# Escribir un programa que tome la lista
# numeros_aleatorios, calcule su mode, median y mean y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:

# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

import random
from statistics import mode, median, mean

random_numbers = [random.randint(1, 100) for i in range(50)]

modeValue = mode(random_numbers)
medianValue = median(random_numbers)
meanValue = mean(random_numbers)

positive_bias = meanValue > medianValue and medianValue > modeValue;
negative_bias = meanValue < medianValue and medianValue > modeValue;
unbiased = meanValue == medianValue == modeValue;

print(f"sesgo positivo?: {positive_bias}")
print(f"sesgo negativo?: {negative_bias}")
print(f"sin sego?: {unbiased}")
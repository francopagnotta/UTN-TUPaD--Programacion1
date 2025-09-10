# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# - Menor que 3: "Muy leve" (imperceptible).
# - Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# - Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# - Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# - Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# - Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

def getRichterScaleOfEarthquakeMagnitude():
	magnitude = float(input("ingrese la magnitud del terremoto: "))

	if magnitude >= 3 and magnitude < 4:
		print("leve, ligeramente perceptible")
	elif magnitude >= 4 and magnitude < 5:
		print("moderado, sentido por personas, pero generalmente no causa danios")
	elif magnitude >= 5 and magnitude < 6:
		print("fuerte, puede causar danos en estructuras debiles")
	elif magnitude >= 6 and magnitude < 7:
		print("muy fuerte, puede causar danios significativos")
	elif  magnitude >= 7:
		print("extremo, puede causar grandes danios a gran escala")
	else:
		print("muy leve, imperceptible")
  
getRichterScaleOfEarthquakeMagnitude()
    
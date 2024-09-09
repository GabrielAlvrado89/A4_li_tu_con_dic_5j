print("Ejemplos de tuplas")
canciones=("Te amo", "El noa noa", "amor eterno")
print(canciones)

y = list(canciones)
y[1] = "La puerta negra"
x = tuple(y)
print(x)

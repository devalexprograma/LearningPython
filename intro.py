nombre = "Edward"
edad = 18
if edad <= 18:
    print(nombre+"Soy mayor de edad ")


Texto = """Hola me llamo
edward y estuduio informatica
soy experto"""

# Ejemplo Prefix y Suffix - Quita los prefijos y sufijos

producto1 = "0001 - Manzana Mordida"
producto2 = "Manzana Mordida - 0001"

print(producto1.removeprefix("0001 -"))
print(producto2.removesuffix("- 0001"))

# Indexing - Muestra un caracter de la cadena
print(producto2[2])
# Slicing
telefono = "4-5-3-3-4-5-6-7-7"
print(producto2[0:4])
print(telefono[::2])  # Establece salto de dos
# Slicing Negativo
print(producto1[-6:-1])

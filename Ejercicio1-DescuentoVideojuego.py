#Calcular el precio final de una venta. 
#Solicitar: el precio del videojuego y si el cliente es miembro VIP.
#Si el precio del videojuego es mayor o igual a Q500, se aplica un descuento del 10%.
#Si el cliente es miembro VIP, se aplica un descuento ADICIONAL del 15% sobre el precio ya rebajado.
#El sistema debe mostrar el precio final que debe pagar el cliente.

Precio = float(input("Ingrese el precio del videojuego: "))
VIP = input("¿El cliente es miembro VIP? (Sí/No): ")
if Precio >= 500:
    Precio = Precio * 0.90  # Aplica descuento del 10%
if VIP.lower() == "sí":
    Precio = Precio * 0.85  # Aplica descuento adicional del 15%
print(f"El precio final que debe pagar el cliente es: Q{Precio:.2f}")

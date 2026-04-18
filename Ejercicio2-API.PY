#Petición API: Realizar una petición GET al endpoint proporcionado.
#Validación: Utilizar un if para verificar si la petición fue exitosa (código de estado 200). Si falla, mostrar un mensaje de error y terminar.
#Iteración: Si la petición es exitosa, procesar la respuesta JSON. Usar un ciclo for para recorrer la lista de pokemones obtenidos (que se encuentra en la llave results del JSON).
#Lógica y Condicional: Dentro del ciclo, para cada pokemón, deberás imprimir su nombre. Sin embargo, hay una regla especial:
#Si el nombre del pokemón comienza con la letra 'b' (mayúscula o minúscula), debes imprimir: [ESPECIAL] NombreDelPokemon.
#De lo contrario, simplemente imprime: Nombre: NombreDelPokemon.


import requests
 
def obtener_lista_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon"
   
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            datos = response.json()
            
            # "results" contiene la lista de Pokémon
            lista_pokemon = datos['results']
            
            print("Lista de Pokémon:\n")
            
            for pokemon in lista_pokemon:
                nombre = pokemon['name']
                if nombre.lower().startswith("b"):
                    print("Nombre: [ESPECIAL]", nombre)
                else:
                    print("Nombre:", nombre)
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejecutar función
obtener_lista_pokemon()
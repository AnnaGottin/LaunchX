planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
planet = input( "Inserta planeta:" )
planetX = planets.index(planet)
if(planetX > -1):
    print("El indice del planeta es: ", planetX)
    print(f"Los planetas mas cercanos desde {planet} son: ", planets[:planetX] )
    print("Los planetas mas lejanos desde {planet} son: ", planets[planetX+1:] )
else:
    print("Planeta no encontrado")

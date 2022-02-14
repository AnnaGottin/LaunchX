def promedio(t1, t2, t3):
    return (t1+t2+t3)/3

def informes(t1, t2, t3):
    return f""" Promedio: {promedio(t1,t2,t3) }
    Lectura Tanque 1: {t1}
    Lectura Tanque 2: {t2}
    Lectura Tanque 3: {t3}
    """

print(informes(5,8,10))

def informe(destino, *time  ,**fuel_reservoirs):
    return f"""
    Destino: {destino}
    Tiempo de vuelo: {sum(time)}
    Total de combustible: {sum(fuel_reservoirs.values() )}
    """

print(informe('Moon', 1,2,3, t1=10,t2=15,t3=20   )  )